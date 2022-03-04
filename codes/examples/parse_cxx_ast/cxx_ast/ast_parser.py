from .ast_define import *
from ..clang.cindex import TranslationUnit
import os


class AstPathSet(object):
    '''
    root： 空或绝对路径，根目录路径
    paths：相对路径，子目录路径，可多层。如 . a a/b a/b/c等
    abspaths：绝对路径，root+paths[*]
    abspath_path_map: 相对路径映射绝对路径
    path_abspath_map：绝对路径映射相对路径
    '''
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
                assert (os.path.isabs(item))
                abspath = item.replace('\\', '/')
                self.abspath_path_map[abspath] = abspath
                self.path_abspath_map[abspath] = abspath
                self.abspaths.add(abspath)
        else:
            root_abspath = os.path.abspath(self.root)
            for item in self.paths:
                assert (not os.path.isabs(item))
                relative_path = item.replace('\\', '/')
                abspath = os.path.abspath(os.path.join(root_abspath, relative_path)).replace('\\', '/')
                self.abspath_path_map[abspath] = relative_path
                self.path_abspath_map[relative_path] = abspath
                self.abspaths.add(abspath)


class AstParseResult(object):
    '''
    '''
    def __init__(self):
        self.ast_root: typing.Optional[AstDescNamespace] = None
        self.path_map_abs_to_relative: typing.Dict[str, str] = {}
        self.path_map_struct_to_file_set: typing.Dict[str, typing.Set[str]] = {}
        self.path_map_source_root: typing.Set[str] = set()


def find_all_files(abspath, subfixs):
    if not os.path.exists(abspath):
        return []
    if not os.path.isdir(abspath):
        return [abspath]
    ret = []
    for root, dirs, files in os.walk(abspath, followlinks=True):
        for f in files:
            file_path = os.path.abspath(os.path.join(root, f)).replace('\\', '/')
            subfix = os.path.splitext(file_path)
            if subfix[1] in subfixs:
                ret.append(file_path)
    return ret


def do_parse(
        opts: typing.List[str],
        cpp_include_sets: typing.List[AstPathSet],
        source_root_sets: typing.List[AstPathSet],
        parse_sets: typing.List[AstPathSet],
        fake_sets: typing.List[AstPathSet],
        parse_subfixs=set([".h", ".hpp"]),
        exclude_sets: typing.List[AstPathSet]=[],
        fake_exclude_sets: typing.List[AstPathSet]=[]) -> AstParseResult:
    all_fake_parse_files = set()
    path_set_source_root = set()
    for item in source_root_sets:
        item.gen_path_map()
        for abspath in item.abspaths:
            path_set_source_root.add(abspath)
    include_file_paths = set()
    include_paths = set()
    for item in cpp_include_sets:
        item.gen_path_map()
        for abspath in item.abspaths:
            include_paths.add(abspath)
            files = find_all_files(abspath, parse_subfixs)
            include_file_paths = include_file_paths.union(set(files))
    all_fake_parse_files = all_fake_parse_files.union(include_file_paths)
    # cal parse files start
    parse_files = set()
    for parse_set in parse_sets:
        parse_set.gen_path_map()
        for item in parse_set.abspaths:
            files = find_all_files(item, parse_subfixs)
            parse_files = parse_files.union(set(files))
    all_fake_parse_files = all_fake_parse_files.union(parse_files)
    exclude_paths = set()
    for item in exclude_sets:
        item.gen_path_map()
        for abspath in item.abspaths:
            exclude_paths.add(abspath)
    remove_files = []
    for parse_item in parse_files:
        for exclude_item in exclude_paths:
            if parse_item.startswith(exclude_item):
                remove_files.append(parse_item)
                break
    for item in remove_files:
        parse_files.discard(item)
    # cal parse files end
    # cal fake files start
    fake_files = set()
    fake_files = fake_files.union(parse_files)
    fake_files = fake_files.union(include_file_paths)
    for item in fake_sets:
        item.gen_path_map()
        for abspath in item.abspaths:
            files = find_all_files(abspath, parse_subfixs)
            fake_files = fake_files.union(set(files))
    all_fake_parse_files = all_fake_parse_files.union(fake_files)
    fake_exclude_paths = set()
    for item in fake_exclude_sets:
        item.gen_path_map()
        for abspath in item.abspaths:
            fake_exclude_paths.add(abspath)
    remove_files = []
    for fake_item in fake_files:
        for exclude_item in fake_exclude_paths:
            if fake_item.startswith(exclude_item):
                remove_files.append(fake_item)
                break
    for item in remove_files:
        fake_files.discard(item)
    # cal fake files end
    # gen fake.h and use clang parse it
    fake_h_name = "fake.h"
    fake_h_content = ""
    for item in fake_files.union(parse_files):
        fake_h_content += "#include <{0}>\n".format(item)
    for item in include_paths:
        opts.append("-I{0}".format(item))
    tu = TranslationUnit.from_source(
        fake_h_name, opts, [(fake_h_name, fake_h_content)], \
        options=0 + \
                # + TranslationUnit.PARSE_INCLUDE_BRIEF_COMMENTS_IN_CODE_COMPLETION \
                + TranslationUnit.PARSE_SKIP_FUNCTION_BODIES \
                + TranslationUnit.PARSE_INCOMPLETE \
        # + TranslationUnit.PARSE_CACHE_COMPLETION_RESULTS \
    )
    # get usr location(hfile), hfile undeclare usrs
    struct_usr_locate_path_map = {}  # usr map to h file abspath
    hfile_undeclare_struct_map = {}  # hfile include undeclare usrs
    for curr_cursor in tu.cursor.walk_preorder():
        try:
            cursor_kind = curr_cursor.kind
        except Exception:
            continue
        is_concern = CursorKind.STRUCT_DECL == cursor_kind \
                     or CursorKind.CLASS_DECL == cursor_kind \
                     or CursorKind.TYPE_REF == cursor_kind
        if not is_concern:
            continue
        location_file = curr_cursor.location.file
        if not location_file:
            continue
        file_path = location_file.name.replace('\\', '/')
        if curr_cursor.is_definition():
            struct_usr_locate_path_map[curr_cursor.get_usr()] = file_path
            continue
        if file_path not in parse_files:
            continue
        struct_usrs = hfile_undeclare_struct_map.get(file_path)
        if not struct_usrs:
            struct_usrs = set()
            hfile_undeclare_struct_map[file_path] = struct_usrs
        if not CursorKind.TYPE_REF == cursor_kind:
            struct_usrs.add(curr_cursor.get_usr())
        else:
            if curr_cursor.get_definition():
                struct_usrs.add(curr_cursor.get_definition().get_usr())
    # hfile need to include other hfiles to get undeclare usrs's definition
    path_map_struct_to_file_set = {}
    for hfile, struct_usrs in hfile_undeclare_struct_map.items():
        files = set()
        for usr in struct_usrs:
            relate_path = struct_usr_locate_path_map.get(usr)
            if relate_path:
                files.add(relate_path)
        path_map_struct_to_file_set[hfile] = files
    # gen abs path to relate_path map
    path_map_abs_to_relative = {}
    for item in all_fake_parse_files:
        for include_item in include_paths:
            if item.startswith(include_item):
                path_map_abs_to_relative[item] = item[len(include_item):].strip('/')
                break
    # gen fake.h and parse it
    root_ns = AstDescNamespace()
    for item in parse_files:
        fake_h_content = "#include <{0}>\n".format(item)
        for extra_hfile in path_map_struct_to_file_set.get(item, []):
            fake_h_content += "#include <{0}>\n".format(item)
        tu_parse = TranslationUnit.from_source(
            fake_h_name, opts, [(fake_h_name, fake_h_content)], \
            options=0 + \
                    + TranslationUnit.PARSE_INCLUDE_BRIEF_COMMENTS_IN_CODE_COMPLETION \
                    + TranslationUnit.PARSE_SKIP_FUNCTION_BODIES \
                    + TranslationUnit.PARSE_INCOMPLETE
            # + TranslationUnit.PARSE_CACHE_COMPLETION_RESULTS \
        )
        root_ns.cursor = tu_parse.cursor
        parse_ast(root_ns, root_ns.cursor, parse_files)
    ret = AstParseResult()
    ret.ast_root = root_ns
    ret.path_map_source_root = path_set_source_root
    ret.path_map_abs_to_relative = path_map_abs_to_relative
    ret.path_map_struct_to_file_set = path_map_struct_to_file_set
    return ret
