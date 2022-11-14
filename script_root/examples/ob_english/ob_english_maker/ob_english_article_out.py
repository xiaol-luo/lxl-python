from __future__ import annotations

import parsimonious
import logbook
import typing

from . import ob_english_maker
from . import ob_english_utils
from . import ob_english_article
from .. import tt
import script_root.libs.utils.file_utils as file_utils
import os
import datetime


class ArticleSentence(object):
    content: str
    translation: str

    def __init__(self):
        super(ArticleSentence, self).__init__()
        self.content = ""
        self.translation = ""

    def __str__(self):
        return self.content or ""


class ObEnglishArticleOut(object):
    maker: ob_english_maker.ObEnglishMaker
    name: str
    date: str
    raw_word_set: typing.Set[str]
    sentence_list: typing.List[ArticleSentence]

    def __init__(self, maker: ob_english_maker.ObEnglishMaker):
        super(ObEnglishArticleOut, self).__init__()
        self.maker = maker
        self.name = ""
        self.date = ""
        self.raw_word_set = set()
        self.sentence_list = []

    @property
    def create_date(self) -> datetime.datetime:
        ret = None
        if len(self.date) > 0:
            ret = datetime.datetime.fromisoformat(self.date)
        return ret

    def update_from_other(self, other: ObEnglishArticleOut):
        if other.date:
            self.date = other.date
        self.raw_word_set.update(other.raw_word_set)
        old_sentence_list = self.sentence_list
        self.sentence_list = []
        for i in other.sentence_list:
            st = ArticleSentence()
            self.sentence_list.append(st)
            st.content = i.content
            for j in old_sentence_list:
                if i.content == j.content:
                    st.translation = j.translation

    @staticmethod
    def create_from_article(maker: ob_english_maker.ObEnglishMaker, article: ob_english_article.ObEnglishArticle):
        ret = ObEnglishArticleOut(maker)
        ret.name = ob_english_maker.ObEnglishUtils.cal_out_article_name(article.name)
        ret.date = ""
        sentence: ob_english_article.ArticleAstVisitorSentence
        for sentence in article.sentience_list:
            st = ArticleSentence()
            st.content = sentence.content
            st.translation = ""
            ret.sentence_list.append(st)
            for word in sentence.words:
                maker.get_word(word, True)
                ret.raw_word_set.add(word)
        return ret

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

        grammar = parsimonious.grammar.Grammar(r"""
            all = block*
            block = date_block / raw_word_block / sentence_block / line
            
            date_block = date_block_begin date_block_content date_block_end            
            date_block_begin = ~r"[\s]*<!--__date__[\s]*"
            date_block_content = ~r"[\S]*"
            date_block_end = ~r"[\s]*__date__-->[\s]*"
            
            raw_word_block = raw_word_block_begin raw_word_block_content raw_word_block_end
            raw_word_block_begin = ~r"<!--__raw_word__[\s]*"
            raw_word_block_content = raw_word_block_word*
            raw_word_block_word = ~r"[a-zA-Z]+[\s]*"
            raw_word_block_end = ~r"[\s]*__raw_word__-->[\s]*"
            
            sentence_block = sentence_block_begin sentence_block_content sentence_block_end
            sentence_block_begin =  ~r"[\s]*<!--__sentence__[\s]*"
            sentence_block_content = sentence_block_content_unit*
            sentence_block_content_unit = sentence_block_content_original sentence_block_content_gap sentence_block_content_translate sentence_block_content_end_gap
            sentence_block_content_gap = ~r"[/s]*========== Content And Translate  ==========\n[/s]*"
            sentence_block_content_end_gap = ~r"[/s]*========== GGGGGGGG  ==========\n[/s]*"
            sentence_block_content_original = ~r"[^\n]*\n"
            sentence_block_content_translate = ~r"[^\n]*\n"
            sentence_block_word = ~r"[^\n]*\n"
            sentence_block_end = ~r"[\s]*__sentence__-->[\s]*"
            
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
        # ast = grammar.parse("<!--__sentence__ hello\n world\n========== GGGGGGGG  ==========\n __sentence__-->")
        visitor = ArticleOutAstVisitor()
        ret = visitor.visit(ast)
        self.sentence_list = ret['sentence_list']
        self.raw_word_set = set(ret['raw_word_list'])
        self.date = ret['date']
        for elem in self.raw_word_set:
            if elem:
                self.maker.get_word(elem, True)

    def to_content(self):
        raw_word_list = []
        sorted_word_list = list(self.raw_word_set)
        sorted_word_list.sort()
        for e in sorted_word_list:
            raw_word_list.append(self.maker.get_word(e, True))
        is_ok, out_content = tt.render("out_article.j2",
                                       date=self.date,
                                       sentence_list=self.sentence_list,
                                       raw_word_list=raw_word_list)
        return is_ok and out_content or None

    def save(self):
        self.check_translate()
        if not self.date:
            self.date = datetime.datetime.now().isoformat()
        out_content = self.to_content()
        if out_content:
            out_file = self.maker.work_path.joinpath(self.name)
            file_utils.write_file(out_file.as_posix(), out_content, encoding="utf-8")

    def check_translate(self):
        wait_translate_sentence_list = []
        for sentence in self.sentence_list:
            if sentence.content and not sentence.translation:
                wait_translate_sentence_list.append(sentence.content)
        if len(wait_translate_sentence_list) <= 0:
            return
        from ..translate import translator
        ret_list = translator.translate_sentences(wait_translate_sentence_list)
        translate_map = {}
        for i in range(0, len(wait_translate_sentence_list)):
            translate_map[wait_translate_sentence_list[i]] = ret_list[i]

        for sentence in self.sentence_list:
            if sentence.content and not sentence.translation:
                sentence.translation = translate_map[sentence.content]

    def reuse_translate(self, old_article):
        for sentence in self.sentence_list:
            if sentence.content and not sentence.translation:
                for elem in old_article.sentence_list:
                    if elem.translation and elem.content == sentence.content:
                        sentence.translation = elem.translation


class ArticleOutAstVisitor(parsimonious.nodes.NodeVisitor):
    def __init__(self):
        super(ArticleOutAstVisitor, self).__init__()

    def visit_all(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_all {} {}", node, visited_children)
        ret = {}
        ret['date'] = ""
        ret["sentence_list"] = []
        ret["raw_word_list"] = []
        block: parsimonious.nodes.Node = None
        for block in visited_children:
            if block.expr_name == "line":
                continue
            if block.expr_name == "date_block":
                content_node: parsimonious.nodes.Node = block.children[1]
                assert content_node.expr_name == "date_block_content"
                ret["date"] = content_node.text
            if block.expr_name == "sentence_block":
                content_node: parsimonious.nodes.Node = block.children[1]
                assert content_node.expr_name == "sentence_block_content"
                unit: parsimonious.nodes.Node
                for unit in content_node.children:
                    assert unit.expr_name == "sentence_block_content_unit"
                    original_st: parsimonious.nodes.Node = unit.children[0]
                    translate_st: parsimonious.nodes.Node = unit.children[2]
                    st = ArticleSentence()
                    st.content = original_st.text.strip("\n")
                    st.translation = translate_st.text.strip("\n")
                    ret["sentence_list"].append(st)
            if block.expr_name == "raw_word_block":
                content_node: parsimonious.nodes.Node = block.children[1]
                assert content_node.expr_name == "raw_word_block_content"
                for elem in content_node.children:
                    ret["raw_word_list"].append(elem.text.strip("\n"))
                continue
        return ret

    def visit_chinese_word(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_chinese_word {}", node.text)
        return node

    def visit_word(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_word {}", node.text)
        return node

    def visit_block(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_block {}", node.text)
        return visited_children[0]

    def visit_line(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_line {}", node.text)
        return node

    def visit_line_with_end(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_line_with_end {}", node.text)
        return node

    def visit_line_elems(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_line_elems {}", node.text)
        return node

    def visit_line_elem(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_line_elem {}", node.text)
        return node

    def visit_line_end(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_line_end {}", node.text)
        return node

    def visit_line_any(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_line_any {}", node.text)
        return node

    def visit_date_block(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_date_block {}", node.text)
        return node

    def visit_date_block_begin(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_date_block_begin {}", node.text)
        return node

    def visit_date_block_end(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_date_block_end {}", node.text)
        return node

    def visit_date_block_content(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_date_block_content {}", node.text)
        return node

    def visit_raw_word_block(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_raw_word_block {}", node.text)
        return node

    def visit_raw_word_block_begin(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_raw_word_block_begin {}", node.text)
        return node

    def visit_raw_word_block_end(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_raw_word_block_end {}", node.text)
        return node

    def visit_raw_word_block_content(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_raw_word_block_words {}", node.text)
        return node

    def visit_raw_word_block_word(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_raw_word_block_word {}", node.text)
        return node

    def visit_sentence_block(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_sentence_block {}", node.text)
        return node

    def visit_sentence_block_begin(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_sentence_block_begin {}", node.text)
        return node

    def visit_sentence_block_content(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_sentence_block_content {}", node.text)
        return node

    def visit_sentence_block_end(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_sentence_block_end {}", node.text)
        return node

    def visit_sentence_block_content_unit(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_sentence_block_content_unit {}", node.text)
        return node

    def visit_sentence_block_content_original(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_sentence_block_content_original {}", node.text)
        return node

    def visit_sentence_block_content_translate(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_sentence_block_content_translate {}", node.text)
        return node

    def visit_sentence_block_content_gap(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_sentence_block_content_gap {}", node.text)
        return node

    def visit_sentence_block_content_end_gap(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_sentence_block_content_gap {}", node.text)
        return node
