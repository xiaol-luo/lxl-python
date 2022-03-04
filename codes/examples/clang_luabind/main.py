from .cppluabind.parse import do_parse_ex, path_set
from .clang.cindex import Config
import json
import argparse
import codecs

def main():
    Config.set_library_file(r"D:\tools\LLVM\bin\libclang.dll")

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
    source_roots = []
    for item in cfg["source_roots"]:
        ps = path_set()
        ps.root = item[0]
        ps.paths.extend(item[1])
        source_roots.append(ps)
    parse_paths = []
    for item in cfg["parse_paths"]:
        ps = path_set()
        ps.root = item[0]
        ps.paths.extend(item[1])
        parse_paths.append(ps)
    parse_exclude_paths = []
    for item in cfg["exclude_paths"]:
        ps = path_set()
        ps.root = item[0]
        ps.paths.extend(item[1])
        parse_exclude_paths.append(ps)
    fake_paths = []
    for item in cfg["fake_paths"]:
        ps = path_set()
        ps.root = item[0]
        ps.paths.extend(item[1])
        fake_paths.append(ps)
    fake_exclude_paths = []
    for item in cfg["fake_exclude_paths"]:
        ps = path_set()
        ps.root = item[0]
        ps.paths.extend(item[1])
        fake_exclude_paths.append(ps)
    do_parse_ex(cfg["opts"], cfg["out_dir"], include_paths, source_roots, parse_paths, fake_paths,\
        cfg["parse_subfixs"], parse_exclude_paths, fake_exclude_paths)


if __name__ == "__main__":
    main()