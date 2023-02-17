import gevent
import logbook
from .app_setting import AppDDSetting
from libs.gevent_ext.gevent_cmd import GeventCmd


class AppDDTask(gevent.Greenlet):
    def __init__(self):
        super(AppDDTask, self).__init__(self._internal_logic)
        self.is_done = False
        self.error_num = 0
        self.error_msg = ""

    def _internal_logic(self):
        # 重写这里
        pass


class AppDDTask_BuildAndroid(AppDDTask):
    def __init__(self, app_setting: AppDDSetting):
        super(AppDDTask_BuildAndroid, self).__init__()
        self.app_setting = app_setting

    def _internal_logic(self):
        logbook.debug("setting {}", self.app_setting)
        cmd_str = "\"{unity_exe_path}\" -projectPath {unity_project_dir} -logFile {unity_log_file} {build_asset_bundle_cmd}".format(
            unity_exe_path=self.app_setting.unity_exe_path,
            unity_project_dir=self.app_setting.unity_project_dir,
            unity_log_file=self.app_setting.unity_log_file,
            build_asset_bundle_cmd=self.app_setting.build_asset_bundle_cmd
        )
        logbook.debug("cmd {}", cmd_str)
        cmd = GeventCmd(cmd_str, capture_output=True)
        cmd.execute()
        logbook.debug("cmd execute {} {} {}", cmd.return_code, cmd.error_text, cmd.out_text)
