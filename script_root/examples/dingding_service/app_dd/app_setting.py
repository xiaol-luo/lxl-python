
import platform


class AppDDSetting(object):
    def __init__(self):
        super(AppDDSetting, self).__init__()
        self.platform_system = platform.system()
        self.unity_exe_path = r"C:/Program Files/Unity/Hub/Editor/2021.3.18f1c1/Editor/Unity.exe"
        self.unity_project_dir = r"F:/work/tanchiyu/client/game_card"
        self.unity_log_file = r"F:/work/ws/unity_log.txt"
        self.unity_opt = "-quit -batchmode  -buildTarget android -logFile {0}".format(self.unity_log_file)
        self.cmd_build_ab = "-executeMethod UtopiaEditor.BuildAndroid.BuildAssetBundle"
        self.cmd_build_app = "-executeMethod UtopiaEditor.BuildAndroid.BuildApp"


def get_setting():
    if platform.system() == "Windows":
        return AppDDSetting()
    else:
        return 2