
from .defines import *
from . import render_cpp
from clang import cindex
from clang.cindex import TranslationUnit, Config
import jinja2
import os
import codecs
import collections

def do_parse(file_path, opts, parse_files, outdir):
    index = cindex.Index.create()
    tu = index.parse(file_path, opts, \
            options= 0 + \
            #+ TranslationUnit.PARSE_INCLUDE_BRIEF_COMMENTS_IN_CODE_COMPLETION \
            + TranslationUnit.PARSE_SKIP_FUNCTION_BODIES \
            + TranslationUnit.PARSE_INCOMPLETE \
            # + TranslationUnit.PARSE_CACHE_COMPLETION_RESULTS \
            )
    root_ns = descript_namespace()
    root_ns.cursor = tu.cursor
    descript_base.try_parse_child_ast(tu.cursor, root_ns, parse_files)
    render_cpp.do_render(root_ns, outdir)


class path_set(object):
    def __init__(self):
        self.root = ""
        self.paths = []
        self.abspaths = None
        self.abspath_path_map = None
        self.path_abspath_map = None

    def gen_path_map(self):
        self.abspath_path_map = {}
        self.path_abspath_map = {}
        self.abspaths = set()

        if not self.root:
            for item in self.paths:
                assert(os.path.isabs(item))
                abspath = item.replace('\\', '/')
                self.abspath_path_map[abspath] = abspath
                self.path_abspath_map[abspath] = abspath
                self.abspaths.add(abspath)
        else:
            root_abspath = os.path.abspath(self.root)
            for item in self.paths:
                assert(not os.path.isabs(item))
                relative_path = item.replace('\\', '/')
                abspath = os.path.abspath(os.path.join(root_abspath, relative_path)).replace('\\', '/')
                self.abspath_path_map[abspath] = relative_path
                self.path_abspath_map[relative_path] = abspath
                self.abspaths.add(abspath)
    

def find_all_files(abspath, subfixs):
    if not os.path.exists(abspath):
        return []
    if not os.path.isdir(abspath):
        return [abspath]
    ret = []
    for root, dirs, files in os.walk(abspath, followlinks=True):
        for f in files:
            file_path = os.path.abspath(os.path.join(root, f)).replace('\\', '/')
            subfix = os.path.splitext(file_path)
            if subfix[1] in subfixs:
                ret.append(file_path)
    return ret  

def find_struct_define_hfile_path(root_cursor, usr):
    waiting_cursors = collections.deque()
    waiting_cursors.append(root_cursor)
    while waiting_cursors:
        curr_cursor = waiting_cursors.pop()
        waiting_cursors.extend(curr_cursor.get_children())
        if usr != curr_cursor.get_usr():
            continue
        if not curr_cursor.is_definition():
            continue
        if not curr_cursor.location.file:
            continue
        file_path = curr_cursor.location.file.name.replace('\\', '/')
        return file_path
    return None

def do_parse_ex(opts, out_dir, cpp_include_sets, source_root_sets, parse_sets, fake_sets, \
        parse_subfixs=set([".h", ".hpp"]), exclude_sets=[], fake_exclude_sets=[]):
    all_fake_parse_files = set()
    source_roots = set()
    for item in source_root_sets:
        item.gen_path_map()
        for abspath in item.abspaths:
            source_roots.add(abspath)
    include_file_paths = set()
    include_paths = set()
    for item in cpp_include_sets:
        item.gen_path_map()
        for abspath in item.abspaths:
            include_paths.add(abspath)
            files = find_all_files(abspath, parse_subfixs)
            include_file_paths = include_file_paths.union(set(files))
    all_fake_parse_files = all_fake_parse_files.union(include_file_paths)
    #cal parse files start
    parse_files = set()
    for parse_set in parse_sets:
        parse_set.gen_path_map()
        for item in parse_set.abspaths:
            files = find_all_files(item, parse_subfixs)
            parse_files = parse_files.union(set(files)) 
    all_fake_parse_files = all_fake_parse_files.union(parse_files)
    exclude_paths = set()
    for item in exclude_sets:
        item.gen_path_map()
        for abspath in item.abspaths:
            exclude_paths.add(abspath)
    remove_files = []
    for parse_item in parse_files:
        for exclude_item in exclude_paths:
            if parse_item.startswith(exclude_item):
                remove_files.append(parse_item)
                break    
    for item in remove_files:
        parse_files.discard(item)
    #cal parse files start
    #cal fake files start
    fake_files = set()
    fake_files = fake_files.union(parse_files)
    fake_files = fake_files.union(include_file_paths)
    for item in fake_sets:
        item.gen_path_map()
        for abspath in item.abspaths:
            files = find_all_files(abspath, parse_subfixs)
            fake_files = fake_files.union(set(files))
    all_fake_parse_files = all_fake_parse_files.union(fake_files)
    fake_exclude_paths = set()
    for item in fake_exclude_sets:
        item.gen_path_map()
        for abspath in item.abspaths:
            fake_exclude_paths.add(abspath)
    remove_files = []
    for fake_item in fake_files:
        for exclude_item in fake_exclude_paths:
            if fake_item.startswith(exclude_item):
                remove_files.append(fake_item)
                break    
    for item in remove_files:
        fake_files.discard(item)
    #cal fake files end
    #gen fake.h and use clang parse it
    fake_h_name = "fake.h"
    fake_h_content = ""
    for item in fake_files.union(parse_files):
        fake_h_content += "#include <{0}>\n".format(item)
    for item in include_paths:
        opts.append("-I{0}".format(item))
    tu = TranslationUnit.from_source(fake_h_name, opts, [(fake_h_name, fake_h_content)], \
        options= 0 + \
            #+ TranslationUnit.PARSE_INCLUDE_BRIEF_COMMENTS_IN_CODE_COMPLETION \
            + TranslationUnit.PARSE_SKIP_FUNCTION_BODIES \
            + TranslationUnit.PARSE_INCOMPLETE \
            # + TranslationUnit.PARSE_CACHE_COMPLETION_RESULTS \
            )
    # get usr location(hfile), hfile undeclare usrs
    struct_usr_locate_path_map = {} # usr map to h file abspath
    hfile_undeclare_struct_map = {} # hfile include undeclare usrs
    for curr_cursor in tu.cursor.walk_preorder(): 
        cursor_kind = curr_cursor.kind
        is_concern = CursorKind.STRUCT_DECL ==  cursor_kind\
            or CursorKind.CLASS_DECL == cursor_kind \
            or CursorKind.TYPE_REF == cursor_kind
        if not is_concern:
            continue
        location_file = curr_cursor.location.file
        if not location_file:
            continue
        file_path = location_file.name.replace('\\', '/')
        if curr_cursor.is_definition():
            struct_usr_locate_path_map[curr_cursor.get_usr()] = file_path
            continue
        if file_path not in  parse_files:
            continue
        struct_usrs = hfile_undeclare_struct_map.get(file_path)
        if not struct_usrs:
            struct_usrs = set()
            hfile_undeclare_struct_map[file_path] = struct_usrs
        if not CursorKind.TYPE_REF == cursor_kind:
            struct_usrs.add(curr_cursor.get_usr())
        else:
            if curr_cursor.get_definition():
                struct_usrs.add(curr_cursor.get_definition().get_usr())
    # hfile need to include other hfiles to get undeclare usrs's definition
    hfile_struct_define_hfile_map = {} 
    for hfile, struct_usrs in hfile_undeclare_struct_map.items():
        files = set()
        for usr in struct_usrs:
            relate_path = struct_usr_locate_path_map.get(usr)
            if relate_path:
                files.add(relate_path)
        hfile_struct_define_hfile_map[hfile] = files
    #gen abs path to relate_path map
    abspath_relative_path_map = {}
    for item in all_fake_parse_files:
        for include_item in include_paths:
            if item.startswith(include_item):
                abspath_relative_path_map[item] = item[len(include_item):].strip('/')
                break
    # gen fake.h and parse it
    root_ns = descript_namespace()
    for item in parse_files:
        fake_h_content = "#include <{0}>\n".format(item)
        for extra_hfile in hfile_struct_define_hfile_map.get(item, []):
            fake_h_content += "#include <{0}>\n".format(item)
        tu_parse = TranslationUnit.from_source(fake_h_name, opts, [(fake_h_name, fake_h_content)], \
            options= 0 + \
                + TranslationUnit.PARSE_INCLUDE_BRIEF_COMMENTS_IN_CODE_COMPLETION \
                + TranslationUnit.PARSE_SKIP_FUNCTION_BODIES \
                + TranslationUnit.PARSE_INCOMPLETE 
                # + TranslationUnit.PARSE_CACHE_COMPLETION_RESULTS \
                )
        root_ns.cursor = tu_parse.cursor
        descript_base.try_parse_child_ast(root_ns.cursor, root_ns, parse_files)
    render_cpp.do_render(root_ns, abspath_relative_path_map, hfile_struct_define_hfile_map, source_roots, out_dir)





