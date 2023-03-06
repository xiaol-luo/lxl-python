import gevent
import logbook
from .app_setting import AppDDSetting
from libs.gevent_ext.gevent_cmd import GeventCmd
from libs.common.code_help import IndentFlag
from libs.gevent_ext.gevent_task import GeventTask
import typing

if typing.TYPE_CHECKING:
    from ..dd_robot_client.dd_robot_client import DDRobotClient

class AppDDTask_BuildAndroid(GeventTask):
    def __init__(self, app_setting: AppDDSetting, robot_client):
        super(AppDDTask_BuildAndroid, self).__init__()
        self.app_setting = app_setting
        self.robot_client: DDRobotClient = robot_client

    def _internal_logic(self):
        logbook.debug("setting {}", self.app_setting)
        self.robot_client.send_text("begin AppDDTask_BuildAndroid")
        with IndentFlag():
            # build asset bundle
            cmd_str = "\"{unity_exe_path}\" -projectPath {unity_project_dir} {unity_opt} {execute_cmd}".format(
                unity_exe_path=self.app_setting.unity_exe_path,
                unity_project_dir=self.app_setting.unity_project_dir,
                unity_opt=self.app_setting.unity_opt,
                execute_cmd=self.app_setting.cmd_build_ab
            )
            logbook.debug("cmd: {}", cmd_str)
            cmd = GeventCmd(cmd_str, capture_output=True)
            cmd.execute()
            logbook.debug("cmd result: {} {} {}", cmd.return_code, cmd.error_text, cmd.out_text)
            if 0 != cmd.return_code:
                error_msg = "cmd_build_ab fail ! return_code:{}, error_text:{}, out_text:{}".format(cmd.return_code, cmd.error_text, cmd.out_text)
                self.set_done(cmd.return_code, error_msg)
                logbook.error(error_msg)
                return
        with IndentFlag():
            # build app
            cmd_str = cmd_str = "\"{unity_exe_path}\" -projectPath {unity_project_dir} {unity_opt} {execute_cmd}".format(
                unity_exe_path=self.app_setting.unity_exe_path,
                unity_project_dir=self.app_setting.unity_project_dir,
                unity_opt=self.app_setting.unity_opt,
                execute_cmd=self.app_setting.cmd_build_app
            )
            logbook.debug("cmd: {}", cmd_str)
            cmd = GeventCmd(cmd_str, capture_output=True)
            cmd.execute()
            logbook.debug("cmd result: {} {} {}", cmd.return_code, cmd.error_text, cmd.out_text)
            if 0 != cmd.return_code:
                error_msg = "cmd_build_app fail ! return_code:{}, error_text:{}, out_text:{}".format(
                    cmd.return_code, cmd.error_text, cmd.out_text)
                self.set_done(cmd.return_code, error_msg)
                logbook.error(error_msg)
                return
        self.set_done()

