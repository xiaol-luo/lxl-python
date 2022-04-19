
import codecs

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