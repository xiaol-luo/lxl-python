#!/usr/bin/env python

#===- cindex-dump.py - cindex/Python Source Dump -------------*- python -*--===#
#
#                     The LLVM Compiler Infrastructure
#
# This file is distributed under the University of Illinois Open Source
# License. See LICENSE.TXT for details.
#
#===------------------------------------------------------------------------===#

"""
A simple command line tool for dumping a source file using the Clang Index
Library.

"""

from clang.cindex import Config
Config.set_compatibility_check(False)
from clang.cindex import TypeKind, CursorKind

def get_diag_info(diag):
    return { 'severity' : diag.severity,
             'location' : diag.location,
             'spelling' : diag.spelling,
             'ranges' : diag.ranges,
             'fixits' : diag.fixits }

def get_cursor_id(cursor, cursor_list = []):
    if cursor is None:
        return None

    # FIXME: This is really slow. It would be nice if the index API exposed
    # something that let us hash cursors.
    for i,c in enumerate(cursor_list):
        if cursor == c:
            return i
    cursor_list.append(cursor)
    return len(cursor_list) - 1

def get_info(node, depth=0):
    usr = node.get_usr()
    if node.kind == CursorKind.CXX_METHOD:
        tmp = node.type.kind
        tmp = node.type.argument_types()
        tmp = node.type.get_typedef_name()
        tmp = node.type.get_address_space()
        tmp = node.type.get_result()
        tmp = node.type.get_result()
    if node.raw_comment:
        tmp = node.type.kind
    if node.get_definition():
        tmp = node.get_definition()

    children = [get_info(c, depth+1)
                for c in node.get_children()]
    return [ {'id' : get_cursor_id(node)},
             {'cursor_kind' : node.kind},
             {'type_kind' : node.type.kind},
             {'usr' : node.get_usr()},
             {'spelling' : node.spelling},
             {'displayname' : node.displayname},
             {'location' : node.location},
             {'extent.start' : node.extent.start},
             {'extent.end' : node.extent.end},
             {'is_definition' : node.is_definition()},
             {'definition id' : get_cursor_id(node.get_definition())},
             {'children' : children }]

def main():
    from clang.cindex import Index
    from clang.cindex import TranslationUnit
    from pprint import pprint

    from optparse import OptionParser, OptionGroup

    global opts

    #parser = OptionParser("usage: %prog [options] {filename} [clang-args*]")
    #parser.add_option("", "--show-ids", dest="showIDs",
    #                  help="Compute cursor IDs (very slow)",
    #                  action="store_true", default=False)
    #parser.add_option("", "--max-depth", dest="maxDepth",
    #                  help="Limit cursor expansion to depth N",
    #                  metavar="N", type=int, default=None)
    #parser.disable_interspersed_args()
    #(opts, args) = parser.parse_args()

    #if len(args) == 0:
    #    parser.error('invalid number arguments')

    import os
    index = Index.create()
    tu = index.parse("E:/git-dir/Utopia/Code/TrySol/AutoBind/fake.h", ['-x', 'c++', '-std=c++11', '-D__CODE_GENERATOR__', "-IE:/git-dir/Utopia/Code/TrySol"], \
        options= 0 + \
            + TranslationUnit.PARSE_INCLUDE_BRIEF_COMMENTS_IN_CODE_COMPLETION \
            + TranslationUnit.PARSE_SKIP_FUNCTION_BODIES \
            + TranslationUnit.PARSE_INCOMPLETE \
            + TranslationUnit.PARSE_CACHE_COMPLETION_RESULTS \
            )
    if not tu:
        parser.error("unable to load input")

    tokens = tu.get_tokens()
    pprint(('diags', map(get_diag_info, tu.diagnostics)))
    pprint(('nodes', get_info(tu.cursor)))
    



if __name__ == '__main__':
    main()

