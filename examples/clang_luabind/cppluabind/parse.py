
from .defines import *
from . import render_cpp
from clang import cindex
from clang.cindex import TranslationUnit
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

def do_parse_ex(opts, out_dir, cpp_include_sets, parse_sets, parse_subfixs=set([".h", ".hpp"]), exclude_sets=[]):
    include_paths = set()
    for item in cpp_include_sets:
        item.gen_path_map()
        for abspath in item.abspaths:
            include_paths.add(abspath)
    exclude_paths = set()
    for item in exclude_sets:
        item.gen_path_map()
        for abspath in item.abspaths:
            exclude_paths.add(abspath)
    parse_files = set()
    for parse_set in parse_sets:
        parse_set.gen_path_map()
        for item in parse_set.abspaths:
            files = find_all_files(item, parse_subfixs)
            parse_files = parse_files.union(set(files)) 
    remove_files = []
    for parse_item in parse_files:
        for exclude_item in exclude_paths:
            if parse_item.startswith(exclude_item):
                remove_files.append(parse_item)
                break    
    for item in remove_files:
        parse_files.discard(item)
    abspath_relative_path_map = {}
    for parse_item in parse_files:
        relative_path = ""
        for include_item in include_paths:
            if parse_item.startswith(include_item):
                relative_path = parse_item[len(include_item):].strip('/')
                break
        assert(relative_path)
        abspath_relative_path_map[parse_item] = relative_path
    fake_h_name = "fake.h"
    fake_h_content = ""
    for item in include_paths:
        opts.append("-I{0}".format(item))
    for item in abspath_relative_path_map.values():
        fake_h_content += "#include <{0}>\n".format(item)
    tu = TranslationUnit.from_source(fake_h_name, opts, [(fake_h_name, fake_h_content)], \
        options= 0 + \
            #+ TranslationUnit.PARSE_INCLUDE_BRIEF_COMMENTS_IN_CODE_COMPLETION \
            + TranslationUnit.PARSE_SKIP_FUNCTION_BODIES \
            + TranslationUnit.PARSE_INCOMPLETE \
            # + TranslationUnit.PARSE_CACHE_COMPLETION_RESULTS \
            )
    
    hfile_undeclare_struct_map = {}
    undefine_structs = set()
    waiting_cursors = collections.deque()
    waiting_cursors.append(tu.cursor)
    while waiting_cursors:
        curr_cursor = waiting_cursors.pop()
        waiting_cursors.extend(curr_cursor.get_children())
        if CursorKind.STRUCT_DECL != curr_cursor.kind and CursorKind.CLASS_DECL != curr_cursor.kind:
            continue
        if curr_cursor.is_definition():
            continue
        if not curr_cursor.location.file:
            continue
        file_path = curr_cursor.location.file.name.replace('\\', '/')
        if file_path not in  parse_files:
            continue
        struct_usrs = hfile_undeclare_struct_map.get(file_path, None)
        if not struct_usrs:
            struct_usrs = set()
            hfile_undeclare_struct_map[file_path] = struct_usrs
        struct_usrs.add(curr_cursor.get_usr())
        undefine_structs.add(curr_cursor.get_usr())
    struct_usr_locate_path_map = {}
    for usr in undefine_structs:
        locate_path = find_struct_define_hfile_path(tu.cursor, usr)
        if locate_path:
            struct_usr_locate_path_map[usr] = locate_path
    hfile_struct_define_hfile_map = {}
    for hfile, struct_usrs in hfile_undeclare_struct_map.items():
        hfile_struct_define_hfile_map[hfile] = []
        for usr in struct_usrs:
            hfile_struct_define_hfile_map[hfile].append(struct_usr_locate_path_map[usr])

    root_ns = descript_namespace()
    root_ns.cursor = tu.cursor
    descript_base.try_parse_child_ast(tu.cursor, root_ns, parse_files)
    render_cpp.do_render(root_ns, abspath_relative_path_map, hfile_struct_define_hfile_map, out_dir)





