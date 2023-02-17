
import platform


class AppDDSetting(object):
    def __init__(self):
        super(AppDDSetting, self).__init__()
        self.platform_system = platform.system()
        self.unity_exe_path = r"C:/Program Files/Unity/Hub/Editor/2021.3.18f1c1/Editor/Unity.exe"
        self.unity_project_dir = r"F:/work/tanchiyu/client/game_card"
        self.build_asset_bundle_cmd = "-quit -batchmode  -buildTarget android -executeMethod UtopiaEditor.BuildAb.BatchMode_CopyResources"
        self.unity_log_file = r"F:/work/ws/unity_log.txt"


def get_setting():
    if platform.system() == "Windows":
        return AppDDSetting()
    else:
        return 2