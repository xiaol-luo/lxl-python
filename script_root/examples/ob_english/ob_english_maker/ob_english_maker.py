import typing
import pathlib
import logbook
import os.path


class ObEnglishUtils(object):
    Out_Article_Prefix = "oat_"
    Raw_Words_Prefix = "rws_"

    In_Article_Dir = "_article_"
    Out_Article_Dir = "_out_article_"
    Raw_Words_Dir = "_raw_words_"
    Review_Dir = "_review_"

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


class ObEnglishArticle(object):
    def __init__(self):
        super(ObEnglishArticle, self).__init__()
        self.name = ""
        self.content = ""
        self.out_article = None
        self.raw_words = None


class ObEnglishOutArticle(object):
    def __init__(self):
        super(ObEnglishOutArticle, self).__init__()
        self.name = ""
        self.content = ""


class ObEnglishArticleRawWords(object):
    def __init__(self):
        super(ObEnglishArticleRawWords, self).__init__()
        self.name = ""
        self.content = ""


class ObEnglishWord(object):
    def __init__(self):
        super(ObEnglishWord, self).__init__()


class ObEnglishMaker(object):
    notebook_path: pathlib.Path

    def __init__(self, notebook_path):
        super(ObEnglishMaker, self).__init__()
        self.notebook_path = pathlib.Path(notebook_path)

    def parse_notebook(self):
        pass

    def handle_article(self, article_name: str):
        article_path = self.notebook_path.joinpath(article_name)
        logbook.debug("handle_article {0} {1}", self.notebook_path, article_path)



