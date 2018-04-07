from cppluabind.parse import do_parse, do_parse_ex, path_set
import os
import sys
import argparse
import json
import argparse
import codecs


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

    ins = path_set()
    ins.root = curr_dir
    ins.paths.append("data")

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", '--file',  help='json config file')
    args = parser.parse_args()

    json_file = args.file
    with codecs.open(json_file, 'r', encoding='utf-8') as f:
        cfg = json.load(f)

    include_paths = []
    for item in cfg["include_paths"]:
        ps = path_set()
        ps.root = item[0]
        ps.paths.extend(item[1])
        include_paths.append(ps)
    parse_paths = []
    for item in cfg["parse_paths"]:
        ps = path_set()
        ps.root = item[0]
        ps.paths.extend(item[1])
        parse_paths.append(ps)
    exclude_paths = []
    for item in cfg["exclude_paths"]:
        ps = path_set()
        ps.root = item[0]
        ps.paths.extend(item[1])
        exclude_paths.append(ps)
    do_parse_ex(cfg["opts"], cfg["out_dir"], include_paths, parse_paths, cfg["parse_subfixs"], exclude_paths)

if __name__ == "__main__":
    main()