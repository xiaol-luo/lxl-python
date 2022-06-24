import tt
import typing
import script_root.libs.utils.file_utils as file_utils
import os
import pathlib

from . import export_file


def export_test_file(out_root_dir:str, zone:typing.Dict[str, typing.Dict[str, str]], ext_params):
    locate_machine = None
    image = None
    for item in zone.etcd_cluster.server_list.values():
        locate_machine = item.locate_machine
        image = item.image
        break
    to_docker_file_list = zone.test_to_docker_file_list
    tt_ret, tt_content = tt.render("test/test.py.j2",
                                   zone=zone,
                                   locate_machine=locate_machine,
                                   to_docker_file_list=to_docker_file_list,
                                   image=image)
    out_file = export_file.cal_test_file_path(out_root_dir, zone)
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    if tt_ret:
        file_utils.write_file(out_file, tt_content)

