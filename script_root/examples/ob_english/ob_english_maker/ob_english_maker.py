from __future__ import annotations

import typing
import pathlib
import logbook
import os.path

from .ob_english_word import ObEnglishWord
from .ob_english_article import ObEnglishArticle
from .ob_english_utils import ObEnglishUtils

class ObEnglishOutArticle(object):
    def __init__(self):
        super(ObEnglishOutArticle, self).__init__()
        self.name = ""
        self.content = ""


class ObEnglishLine(object):
    def __init__(self):
        super(ObEnglishLine, self).__init__()
        self.content = ""
        self.words = []


class ObEnglishArticleRawWords(object):
    def __init__(self):
        super(ObEnglishArticleRawWords, self).__init__()
        self.name = ""
        self.content = ""
        self.words = []

        ObEnglishUtils.ensure_dirs()


class ObEnglishMaker(object):
    work_path: pathlib.Path
    word_map:typing.Dict[str, ObEnglishWord]

    def __init__(self, work_path):
        super(ObEnglishMaker, self).__init__()
        self.work_path = pathlib.Path(work_path)
        self.word_map = {}

    def setup_workspace(self):
        ObEnglishUtils.ensure_dirs(self.work_path.as_posix())
        root_files = os.listdir(self.work_path)
        for elem in root_files:
            logbook.debug("setup_workspace root_files {}", elem)
            if os.path.isfile(os.path.join(self.work_path, elem)):
                word = ObEnglishUtils.extract_word(elem)
                self.get_word(word, True)

    def save_workspace(self):
        for v in self.word_map.values():
            v.save()

    def handle_article(self, article_name: str):
        article_path = self.work_path.joinpath(article_name)
        logbook.debug("handle_article {0} {1}", self.work_path, article_path)


    def get_word(self, word:str, is_add_not_exist=True)->ObEnglishWord:
        assert word
        ret:ObEnglishWord = self.word_map.get(word, None)
        if ret is None:
            ret = ObEnglishWord(self)
            ret.word = word
            self.word_map[ret.word] = ret
            ret.load()
            ret.check_translate()
        return ret



    



