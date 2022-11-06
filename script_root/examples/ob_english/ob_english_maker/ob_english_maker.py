from __future__ import annotations

import typing
import pathlib
import logbook
import os.path

from .ob_english_word import ObEnglishWord
from .ob_english_article import ObEnglishArticle
from .ob_english_utils import ObEnglishUtils
from . import ob_english_article_out


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
        self.check_translate_words()
        for v in self.word_map.values():
            v.save()

    def handle_article(self, _article_name: str):
        article_name = ObEnglishUtils.cal_article_name(_article_name)
        article = ObEnglishArticle(self)
        article.name = article_name
        article.load()
        return article


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

    def check_translate_words(self):
        wait_translate_list = []
        for elem in self.word_map.values():
            if elem.word and not elem.translation:
                wait_translate_list.append(elem.word)
        if len(wait_translate_list) <= 0:
            return
        from ..translate import translator
        ret_list = translator.translate_words(wait_translate_list)
        translate_map = {}
        for i in range(0, len(wait_translate_list)):
            translate_map[wait_translate_list[i]] = ret_list[i]
        for word in wait_translate_list:
            w = self.get_word(word, False)
            w.translation = translate_map[word]




    



