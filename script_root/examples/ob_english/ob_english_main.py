import argparse

import logbook

from script_root.libs.common.code_help import IndentFlag
from . import tt
from .ob_english_maker.ob_english_article_out import ObEnglishArticleOut
from .ob_english_maker.ob_english_maker import ObEnglishMaker, ObEnglishUtils


def main(arg_list):
    logbook.debug("arg_list {0}", arg_list)
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--notebook")
    arg_parser.add_argument("--action")
    parse_ret = arg_parser.parse_args(arg_list)
    logbook.debug("parse_ret {}", parse_ret)

    tt.set_filter("set_link", ObEnglishUtils.content_word_set_link)
    ObEnglishUtils.ensure_dirs(parse_ret.notebook)

    note_maker = ObEnglishMaker(parse_ret.notebook)
    note_maker.setup_workspace()

    note_maker.handle_article("hello.md")

    with IndentFlag():
        out_article = ObEnglishArticleOut.create_from_file(note_maker, "test.md")
        out_article.to_content()

    note_maker.save_workspace()



