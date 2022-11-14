from __future__ import annotations

import parsimonious
import logbook
import typing

from . import ob_english_maker
from . import ob_english_article_out
import script_root.libs.utils.file_utils as file_utils


class ArticleAstVisitorSentence(object):
    content:str
    words:typing.List[str]

    def __init__(self):
        super(ArticleAstVisitorSentence, self).__init__()
        self.content = ""
        self.words = []

    def __str__(self):
        return self.content or ""


class ObEnglishArticle(object):
    maker:ob_english_maker.ObEnglishMaker
    name:str
    content:str
    sentience_list:typing.List[ArticleAstVisitorSentence]

    def __init__(self, maker:ob_english_maker.ObEnglishMaker):
        super(ObEnglishArticle, self).__init__()
        self.maker = maker
        self.name = ""
        self.content = ""
        self.sentience_list = []

    def load(self):
        file_path = self.maker.work_path.joinpath(self.name)
        if file_path.is_file():
            self.content = file_utils.read_file(file_path.as_posix(), encoding="utf-8")
        else:
            self.content = ""
        self.parse_content()

    def parse_content(self):
        self.sentience_list = []
        grammar = parsimonious.grammar.Grammar(r"""
            all = sentence* 
            sentence = sentence_with_end / sentence_content
            sentence_with_end = sentence_content sentence_end_flag
            sentence_content = sentence_content_elem*
            sentence_end_flag = ~r"[.!?]+"
            not_sentence_end_flag = ~r"[^.!?]"
            sentence_content_elem = num_order / word / blank / not_sentence_end_flag
            blank = " "
            word = ~r"[a-zA-Z]+" 
            num_order = ~r"[0-9]+[\.)]"
        """)
        ast_tree = grammar.parse(self.content)
        visitor = ArticleAstVisitor(self)
        self.sentience_list = visitor.visit(ast_tree)
        for sentience in self.sentience_list:
            for word in sentience.words:
                self.maker.get_word(word)


class ArticleAstVisitor(parsimonious.nodes.NodeVisitor):
    def __init__(self, article:ObEnglishArticle):
        super(ArticleAstVisitor, self).__init__()
        self.article = article

    def generic_visit(self, node, visited_children):
        return node

    def visit_all(self, node, visited_children):
        # logbook.debug("ArticleAstVisitor.visit_all {} {}", node, visited_children)
        ret = []
        st_list: typing.List[ArticleAstVisitorSentence]
        for st_list in visited_children:
            ret.extend(st_list)
        for i in reversed(range(0, len(ret))):
            st = ret[i]
            st.content = st.content.replace("\r", "").replace("\n", "")
            st.content = st.content.strip(" ")
            if len(st.content) <= 0:
                ret.pop(i)
        return ret

    def visit_sentence(self, node, visited_children):
        return visited_children[0]

    def visit_sentence_content(self, node, visited_children):
        child:parsimonious.nodes.Node
        st_list = []
        st = ArticleAstVisitorSentence()
        for child in visited_children:
            if "num_order" == child.children[0].expr_name:
                if len(st.content.strip(" ")) > 0:
                    st_list.append(st)
                    st = ArticleAstVisitorSentence()
            st.content += child.text
            if "word" == child.children[0].expr_name:
                if not self.article.maker.get_word(child.text, False):
                    st.words.append(child.text)
                #else:
                #    st.words.append(child.text)
        st_list.append(st)
        return st_list

    def visit_sentence_with_end(self, node, visited_children):
        st_list: typing.List[ArticleAstVisitorSentence] = visited_children[0]
        st = st_list[len(st_list) - 1]
        st.content += visited_children[1].text
        return st_list




