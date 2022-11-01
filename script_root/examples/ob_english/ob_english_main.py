import argparse
import logbook
from script_root.libs.common.code_help import IndentFlag


from .ob_english_maker.ob_english_maker import ObEnglishMaker, ObEnglishUtils, ObEnglishLine, ObEnglishWord
from .ob_english_maker.ob_english_article import ObEnglishArticle

def main(arg_list):
    logbook.debug("arg_list {0}", arg_list)
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--notebook")
    arg_parser.add_argument("--action")
    parse_ret = arg_parser.parse_args(arg_list)
    logbook.debug("parse_ret {}", parse_ret)

    ObEnglishUtils.ensure_dirs(parse_ret.notebook)

    note_maker = ObEnglishMaker(parse_ret.notebook)
    note_maker.setup_workspace()

    note_maker.handle_article("hello.md")

    with IndentFlag():
        ob_article = ObEnglishArticle(note_maker)
        ob_article.name = ObEnglishUtils.cal_article_name("test.md")
        ob_article.content = "this is cat? hello world!\n I am fitz."
        ob_article.parse_content()


    with IndentFlag():
        name = "_article_/a1.md"
        out_article = ObEnglishUtils.cal_out_article_name(name)
        raw_worlds = ObEnglishUtils.cal_raw_words_name(name)
        name_1 = ObEnglishUtils.extract_article_name_from_out_article(out_article)
        name_2 = ObEnglishUtils.extract_article_name_from_raw_words(raw_worlds)
        # logbook.debug("xxxxxxxxxxx {} {} {} {} {}", name, out_article, raw_worlds, name_1, name_2)
    with IndentFlag():
        name = "_article_/d1/d2/d3/a1.md"
        out_article = ObEnglishUtils.cal_out_article_name(name)
        raw_worlds = ObEnglishUtils.cal_raw_words_name(name)
        name_1 = ObEnglishUtils.extract_article_name_from_out_article(out_article)
        name_2 = ObEnglishUtils.extract_article_name_from_raw_words(raw_worlds)
        # logbook.debug("xxxxxxxxxxx {} {} {} {} {}", name, out_article, raw_worlds, name_1, name_2)

    note_maker.save_workspace()


