
from .defines import *
from . import render_cpp
from clang import cindex
from clang.cindex import TranslationUnit
import jinja2
import os

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
    

def find_all_files(abspath):
    if not os.path.exists(abspath):
        return []
    if not os.path.isdir(abspath):
        return [abspath]
    ret = []
    for root, dirs, files in os.walk(abspath, followlinks=True):
        for f in files:
            file_path = os.path.abspath(os.path.join(root, f)).replace('\\', '/')
            ret.append(file_path)
    return ret


def do_parse_ex(out_dir, cpp_include_dir, parse_paths, exclude_paths):
    for item in cpp_include_dir:
        item.gen_path_map()
    for item in parse_paths:
        item.gen_path_map()
    for item in exclude_paths:
        item.gen_path_map()
    
    parse_files = set()
    for parse_path in parse_paths:
        for item in parse_path.abspaths:
            files = find_all_files(item)
            parse_files = parse_files.union(set(files))






