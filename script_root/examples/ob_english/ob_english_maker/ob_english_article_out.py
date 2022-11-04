from __future__ import annotations

import parsimonious
import logbook
import typing

from . import ob_english_maker
from . import ob_english_utils
from .. import tt
import script_root.libs.utils.file_utils as file_utils
import os


class ArticleSentence(object):
    content:str
    translation:str

    def __init__(self):
        super(ArticleSentence, self).__init__()
        self.content = ""
        self.translation = ""

    def __str__(self):
        return self.content or ""


class ArticleSentence(object):
    def __init__(self):
        super(ArticleSentence, self).__init__()
        self.content = ""
        self.translation = ""


class ObEnglishArticleOut(object):
    maker:ob_english_maker.ObEnglishMaker
    name:str
    raw_word_set:typing.Set[str]
    sentence_list:typing.List[ArticleSentence]

    def __init__(self, maker:ob_english_maker.ObEnglishMaker):
        super(ObEnglishArticleOut, self).__init__()
        self.maker = maker
        self.name = ""
        self.raw_word_set = set()
        self.sentence_list = []

    @staticmethod
    def create_from_file(maker, name):
        real_name = ob_english_maker.ObEnglishUtils.cal_out_article_name(name)
        file_path = maker.work_path.joinpath(real_name)
        file_content = ""
        if file_path.is_file():
            file_content = file_utils.read_file(file_path.as_posix(), encoding="utf-8")
        ret = ObEnglishArticleOut(maker)
        ret.name = real_name
        ret.from_content(file_content)
        return ret

    def from_content(self, content):
        self.sentence_list.clear()
        self.raw_word_set.clear()
        
        s = ArticleSentence()
        s.content ="hello world!"
        s.translation = "你好 世界！"
        self.sentence_list.append(s)

        self.raw_word_set.add("hello")
        self.raw_word_set.add("word")

        grammar = parsimonious.grammar.Grammar(r"""
            all = block*
            block = date_block / raw_word_block / line
            
            date_block = date_block_begin date_block_content date_block_end            
            date_block_begin = ~r"[\s]*<!--__date__[\s]*"
            date_block_content = ~r"[\S]*"
            date_block_end = ~r"[\s]*__date__-->[\s]*"
            
            raw_word_block = raw_word_block_begin raw_word_block_content raw_word_block_end
            raw_word_block_begin = ~r"[\s]*<!--__raw_word__[\s]*"
            raw_word_block_content = raw_word_block_word*
            raw_word_block_word = ~r"[^\n]*\n"
            raw_word_block_end = ~r"[\s]*__raw_word__-->[\s]*"
            
            line = line_with_end / line_elems 
            line_with_end = line_elems line_end 
            line_elems = line_elem*
            line_elem = word / chinese_word / line_any
            line_any = ~r"[^\n]"
            line_end = "\n"
            word = ~r"[a-zA-Z]+"
            chinese_word = ~r"[\u4e00-\u9fa5]" 
        """)
        ast = grammar.parse(content)
        # ast = grammar.parse("<!--__raw_word__ hello\n world\n __raw_word__-->")
        visitor = ArticleOutAstVisitor()
        visitor.visit(ast)

    def to_content(self):
        is_ok, out_content = tt.render("out_article.j2",
                  date="1234",
                  sentence_list=self.sentence_list,
                  raw_word_list=list(self.raw_word_set))
        out_file = self.maker.work_path.joinpath(self.name)
        # logbook.debug("out article content is {}", out_content)
        file_utils.write_file(out_file.as_posix(), out_content, encoding="utf-8")



class ArticleOutAstVisitor(parsimonious.nodes.NodeVisitor):
    def __init__(self):
        super(ArticleOutAstVisitor, self).__init__()

    def visit_all(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_all {} {}", node, visited_children)
        ret = []
        return ret

    def visit_chinese_word(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_chinese_word {}", node.text)

    def visit_word(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_word {}", node.text)

    def visit_block(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_block {}", node.text)

    def visit_line(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_line {}", node.text)

    def visit_line_with_end(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_line_with_end {}", node.text)

    def visit_line_elems(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_line_elems {}", node.text)

    def visit_line_elem(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_line_elem {}", node.text)

    def visit_line_end(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_line_end {}", node.text)

    def visit_line_any(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_line_any {}", node.text)

    def visit_date_block(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_date_block {}", node.text)

    def visit_date_block_begin(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_date_block_begin {}", node.text)

    def visit_date_block_end(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_date_block_end {}", node.text)

    def visit_date_block_content(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_date_block_content {}", node.text)

    def visit_raw_word_block(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_raw_word_block {}", node.text)

    def visit_raw_word_block_begin(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_raw_word_block_begin {}", node.text)

    def visit_raw_word_block_end(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_raw_word_block_end {}", node.text)

    def visit_raw_word_block_content(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_raw_word_block_words {}", node.text)

    def visit_raw_word_block_word(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_raw_word_block_word {}", node.text)