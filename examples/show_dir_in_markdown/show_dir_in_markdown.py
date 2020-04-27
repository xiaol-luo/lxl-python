import sys
import os
import collections
import codecs

DirMeta = collections.namedtuple("DirMeta", "path, name, sub_dirs")


def extract_dirs(dir_path, out_list, max_depth, depth):
    if depth > max_depth:
        return
    new_dir_meta_list = []
    if os.path.isdir(dir_path):
        for cur_dir_path, dir_names, files in os.walk(dir_path):
            for dir_name in dir_names:
                new_dir_meta = DirMeta(
                    os.path.join(os.path.join(cur_dir_path, dir_name)),
                    dir_name,
                    [],
                )
                out_list.append(new_dir_meta)
                new_dir_meta_list.append(new_dir_meta)
    for dir_meta in new_dir_meta_list:
        extract_dirs(dir_meta.path, dir_meta.sub_dirs, max_depth, depth + 1)


def print_dir_meta_help(dir_meta, depth):
    if depth <= 0:
        return
    line_str = "{}- {}".format("    " * (depth - 1), dir_meta.name)
    print(line_str)
    #print(codecs.encode(line_str))
    for sub_dir_meta in dir_meta.sub_dirs:
        print_dir_meta_help(sub_dir_meta, depth + 1)


if __name__ == "__main__":
    ret_dirs = []
    root_dir = os.path.abspath(os.path.curdir)
    extract_depth = 5
    if len(sys.argv) > 1:
        root_dir = os.path.abspath(sys.argv[1])
    if len(sys.argv) > 2:
        extract_depth = int(sys.argv[2])
    root_dir_meta = DirMeta(root_dir, root_dir, [])
    extract_dirs(root_dir_meta.path, root_dir_meta.sub_dirs, extract_depth, 1)
    print_dir_meta_help(root_dir_meta, 1)



