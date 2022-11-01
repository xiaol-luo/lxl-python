import os

class ObEnglishUtils(object):
    Out_Article_Prefix = "oat_"
    Raw_Words_Prefix = "rws_"

    In_Article_Dir = "_article_"
    Out_Article_Dir = "_out_article_"
    Raw_Words_Dir = "_raw_words_"
    Review_Dir = "_review_"

    @staticmethod
    def ensure_dirs(root_dir):
        os.makedirs(os.path.join(root_dir, ObEnglishUtils.In_Article_Dir), exist_ok=True)
        os.makedirs(os.path.join(root_dir, ObEnglishUtils.Out_Article_Dir), exist_ok=True)
        os.makedirs(os.path.join(root_dir, ObEnglishUtils.Raw_Words_Dir), exist_ok=True)
        os.makedirs(os.path.join(root_dir, ObEnglishUtils.Review_Dir), exist_ok=True)

    @staticmethod
    def cal_word_name(in_str:str):
        while in_str.endswith(".md"):
            in_str = in_str[:len(".md")]
        ret = in_str + ".md"
        return ret

    @staticmethod
    def extract_word(in_str):
        ret = os.path.basename(in_str)
        while ret.endswith(".md"):
            ret = ret[:len(".md")]
        return ret

    @staticmethod
    def cal_article_name(in_name):
        ret = in_name
        hit_pos = in_name.find(ObEnglishUtils.In_Article_Dir)
        if hit_pos < 0:
            in_name = ObEnglishUtils.In_Article_Dir + "/" + in_name
        return in_name

    @staticmethod
    def cal_out_article_name(_in_name):
        in_name = ObEnglishUtils.extract_article_name(_in_name)
        hit_pos = in_name.find(ObEnglishUtils.In_Article_Dir)
        if hit_pos < 0:
            return None
        sub_name = in_name[hit_pos + len(ObEnglishUtils.In_Article_Dir):]
        sub_dir, sub_file = os.path.split(sub_name)
        if not sub_dir.endswith(("/", "\\")):
            sub_dir = sub_dir + "/"
        real_name = in_name[0:hit_pos] + ObEnglishUtils.Out_Article_Dir + sub_dir + ObEnglishUtils.Out_Article_Prefix + sub_file
        return real_name

    @staticmethod
    def extract_article_name_from_out_article(in_name: str):
        hit_pos = in_name.find(ObEnglishUtils.Out_Article_Dir)
        if hit_pos < 0:
            return None
        sub_name = in_name[hit_pos + len(ObEnglishUtils.Out_Article_Dir):]
        sub_dir, sub_file = os.path.split(sub_name)
        if not sub_dir.endswith(("/", "\\")):
            sub_dir = sub_dir + "/"
        assert (sub_file.startswith(ObEnglishUtils.Out_Article_Prefix))
        real_sub_file = sub_file[len(ObEnglishUtils.Out_Article_Prefix):]
        real_name = in_name[0:hit_pos] + ObEnglishUtils.In_Article_Dir + sub_dir + real_sub_file
        return real_name

    @staticmethod
    def cal_raw_words_name(_in_name):
        in_name = ObEnglishUtils.extract_article_name(_in_name)
        hit_pos = in_name.find(ObEnglishUtils.In_Article_Dir)
        if hit_pos < 0:
            return None
        sub_name = in_name[hit_pos + len(ObEnglishUtils.In_Article_Dir):]
        sub_dir, sub_file = os.path.split(sub_name)
        if not sub_dir.endswith(("/", "\\")):
            sub_dir = sub_dir + "/"
        real_name = in_name[0:hit_pos] + ObEnglishUtils.Raw_Words_Dir + sub_dir + ObEnglishUtils.Raw_Words_Prefix + sub_file
        return real_name

    @staticmethod
    def extract_article_name_from_raw_words(in_name:str):
        hit_pos = in_name.find(ObEnglishUtils.Raw_Words_Dir)
        if hit_pos < 0:
            return None
        sub_name = in_name[hit_pos+len(ObEnglishUtils.Raw_Words_Dir):]
        sub_dir, sub_file = os.path.split(sub_name)
        if not sub_dir.endswith(("/", "\\")):
            sub_dir = sub_dir + "/"
        assert(sub_file.startswith(ObEnglishUtils.Raw_Words_Prefix))
        real_sub_file = sub_file[len(ObEnglishUtils.Raw_Words_Prefix):]
        real_name = in_name[0:hit_pos] + ObEnglishUtils.In_Article_Dir + sub_dir + real_sub_file
        return real_name

    @staticmethod
    def extract_article_name(in_name:str):
        if in_name.find(ObEnglishUtils.In_Article_Dir) >= 0:
            return in_name
        ret = ObEnglishUtils.extract_article_name_from_out_article(in_name)
        if ret:
            return ret
        ret = ObEnglishUtils.extract_article_name_from_raw_words(in_name)
        if ret:
            return ret
        assert(False)