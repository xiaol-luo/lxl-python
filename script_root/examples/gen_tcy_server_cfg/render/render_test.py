import tt
import typing
import script_root.libs.utils.file_utils as file_utils
import os
import pathlib

from . import export_file


def export_test_file(out_root_dir:str, zone:typing.Dict[str, typing.Dict[str, str]], ext_params):
    server = None
    for item in zone.game_server_cluster.server_list.values():
        if item.server_role == "world":
            server = item
            break
    tt_ret, tt_content = tt.render("test/test.py.j2",
                                   zone=zone,
                                   server=server)
    out_file = export_file.cal_test_file_path(out_root_dir, zone)
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    if tt_ret:
        file_utils.write_file(out_file, tt_content)

