
from .defines import *
from . import render_cpp
from clang import cindex
from clang.cindex import TranslationUnit
import jinja2

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





