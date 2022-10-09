
import codecs
import os

def write_file(file_path, content, mode="w", encoding=None):
    ret = 0
    with codecs.open(file_path, mode=mode, encoding=encoding) as f:
        ret = f.write(content)
    return ret

def read_file(file_path, encoding=None):
    ret = None
    with codecs.open(file_path, encoding=encoding) as f:
        ret = f.read()
    return ret

def read_all_lines(file_path, encoding=None):
    ret = None
    with codecs.open(file_path, encoding=encoding) as f:
        ret = list(f.readlines())
    return ret

def extract_file_paths(root_dir_path):
    ret = []
    for dir_path, dirs, files in os.walk(root_dir_path):
        for elem in files:
            ret.append(os.path.join(dir_path, elem))
    return  ret

def extract_dir_paths(root_dir_path):
    ret = []
    for dir_path, dirs, files in os.walk(root_dir_path):
        for elem in dirs:
            ret.append(os.path.join(dir_path, elem))
    return  ret