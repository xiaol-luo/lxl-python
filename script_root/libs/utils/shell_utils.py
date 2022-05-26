import os
import shutil
import filecmp

def copy_dir(src_dir, dest_dir, is_replace=False):
    src_abs_dir = os.path.abspath(src_dir)
    dest_abs_dir = os.path.abspath(dest_dir)
    if not os.path.isdir(src_abs_dir):
        return
    if os.path.exists(dest_abs_dir) and not os.path.isdir(dest_abs_dir):
        return
    copy_dirs = []
    copy_files = []
    if not os.path.exists(dest_abs_dir):
        copy_dirs.append(".")
    else:
        related_dirs = []
        related_dirs.append(".")
        for root, dirs, files in os.walk(src_abs_dir):
            for dir in dirs:
                related_dir = os.path.abspath(os.path.join(root, dir)).replace(src_abs_dir, "").lstrip(os.sep)
                related_dirs.append(related_dir)
        for related_dir in related_dirs:
            tmp_src_dir = os.path.abspath(os.path.join(src_abs_dir, related_dir))
            tmp_dest_dir = os.path.abspath(os.path.join(dest_abs_dir, related_dir))
            if not os.path.exists(tmp_dest_dir) or not os.path.isdir(tmp_dest_dir):
                continue
            dir_cmp = filecmp.dircmp(tmp_src_dir, tmp_dest_dir)
            for left_item in dir_cmp.left_only:
                item_path = os.path.join(tmp_src_dir, left_item)
                if os.path.isdir(item_path):
                    copy_dirs.append(os.path.join(related_dir, left_item))
                if os.path.isfile(item_path):
                    copy_files.append(os.path.join(related_dir, left_item))
            if is_replace:
                for left_item in dir_cmp.common_files:
                    copy_files.append(os.path.join(related_dir, left_item))
    for copy_dir in copy_dirs:
        shutil.copytree(os.path.join(src_abs_dir, copy_dir), os.path.join(dest_abs_dir, copy_dir))
    for copy_file in copy_files:
        src_file = os.path.join(src_abs_dir, copy_file)
        dest_file = os.path.join(dest_abs_dir, copy_file)
        if not os.path.exists(os.path.dirname(dest_file)):
            os.makedirs(os.path.dirname(dest_dir))
        shutil.copyfile(src_file, dest_file)
