from cppluabind.parse import do_parse, do_parse_ex, path_set
import os
import sys
import argparse


def main():
    curr_dir = os.path.dirname(__file__)
    file_path = os.path.abspath(os.path.join(curr_dir, "data/heads.h"))
    include_dir = os.path.abspath(os.path.join(curr_dir, "data")).replace('\\', '/')

    ps = path_set()
    ps.root = curr_dir
    ps.paths.append("data")

    eps = path_set()
    eps.root = curr_dir
    eps.paths.append("data/AutoBind")
    
    do_parse_ex(curr_dir, [], [ps], [eps])

    do_parse(file_path, 
        ['-x', 'c++', '-std=c++11', '-D__CODE_GENERATOR__', "-I{0}".format(include_dir)], 
        {
            os.path.abspath(os.path.join(include_dir, "AutoBind/AutoHead.h")).replace('\\', '/'),
            #os.path.abspath(os.path.join(include_dir, "AutoBind/AutoHeadOther.h")).replace('\\', '/'),
        },
        curr_dir)

if __name__ == "__main__":
    main()