from __future__ import annotations

import parsimonious
import logbook
import typing

from . import ob_english_maker
from .ob_english_utils import ObEnglishUtils

import script_root.libs.utils.file_utils as file_utils


class ObEnglishWord(object):
    maker:ob_english_maker.ObEnglishMaker
    content:str
    translation:str
    error_num:int

    def __init__(self, maker:ob_english_maker.ObEnglishMaker):
        super(ObEnglishWord, self).__init__()
        self.maker = maker
        self.content = ""
        self.word = ""
        self.translation = ""
        self.error_num = 0

    @property
    def name(self):
        return ObEnglishUtils.cal_word_name(self.word)

    def set_word(self, word):
        self.word = word
        self.load()

    def load(self):
        file_path = self.maker.work_path.joinpath(self.name)
        all_lines = None
        if file_path.is_file():
            all_lines = file_utils.read_all_lines(file_path.as_posix(), encoding='utf-8')
        else:
            all_lines = []
        self.content = "".join(all_lines)
        if len(all_lines) > 1:
            self.translation = "".join(all_lines[1:])
        else:
            self.translation = ""

    def save(self):
        file_path = self.maker.work_path.joinpath(self.name)
        file_utils.write_file(file_path.as_posix(), "\n".join([self.word, self.translation]), encoding="utf-8")

    def do_translate(self):
        if not self.translation:
            self.translation = ""
            pass

    def check_translate(self):
        if not self.translation:
            self.do_translate()


