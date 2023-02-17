import argparse

import logbook

from script_root.libs.common.code_help import IndentFlag
from . import tt
from .ob_english_maker.ob_english_article_out import ObEnglishArticleOut
from .ob_english_maker.ob_english_maker import ObEnglishMaker, ObEnglishUtils
from .ob_english_maker import ob_english_article_out
from .translate import translator


def main(arg_list):
    logbook.debug("arg_list {0}", arg_list)
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--notebook")
    arg_parser.add_argument("--action")
    parse_ret = arg_parser.parse_args(arg_list)
    logbook.debug("parse_ret {}", parse_ret)

    if True:
        translator.test()
        return

    tt.set_filter("set_link", ObEnglishUtils.content_word_set_link)
    ObEnglishUtils.ensure_dirs(parse_ret.notebook)

    note_maker = ObEnglishMaker(parse_ret.notebook)
    note_maker.setup_workspace()

    with IndentFlag():
        article = note_maker.handle_article("test.md")

        out_article_name = ObEnglishUtils.cal_out_article_name("test.md")

        out_article_1: ob_english_article_out.ObEnglishArticleOut = ob_english_article_out.ObEnglishArticleOut.create_from_article(
            note_maker, article)
        # out_article_1.save()

        out_article_2:ob_english_article_out.ObEnglishArticleOut = ob_english_article_out.ObEnglishArticleOut.create_from_file(
            note_maker, out_article_name)
        out_article_2.update_from_other(out_article_1)
        out_article_2.save()

        # out_article_1.reuse_translate(out_article_2)
        # out_article_1.save()
    note_maker.save_workspace()



