from __future__ import annotations

import parsimonious
import logbook
import typing

from . import ob_english_maker
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
    lines:typing.List[ArticleAstVisitorSentence]

    def __init__(self, maker:ob_english_maker.ObEnglishMaker):
        super(ObEnglishArticle, self).__init__()
        self.maker = maker
        self.name = ""
        self.content = ""
        self.sentience_list = []

    def load(self):
        file_path = self.maker.work_path.joinpath(self.name)
        if file_path.is_file():
            self.content = file_utils.read_file(file_path.as_posix())
        else:
            self.content = ""
        self.parse_content()

    def parse_content(self):
        self.sentience_list = []
        grammar = parsimonious.grammar.Grammar(r"""
            all = sentence*
            sentence =  sentence_with_end / sentence_content
            sentence_with_end = sentence_content sentence_end_flag
            sentence_end_flag = ~r"[.!?]"
            not_sentence_end_flag = ~r"[^.!?]"
            sentence_content = sentence_content_elem* 
            sentence_content_elem = word / blank / not_sentence_end_flag
            blank = " "
            word = ~r"[a-zA-Z]+" 
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


    def visit_all(self, node, visited_children):
        # logbook.debug("ArticleAstVisitor.visit_all {} {}", node, visited_children)
        ret = []
        for elem in visited_children:
            words = elem[0]
            line_content = elem[1]
            # logbook.debug("ArticleAstVisitor.visit_all line {} {}", line_content, words)
            line_data = ArticleAstVisitorSentence()
            line_data.content = line_content
            line_data.words = words
            ret.append(line_data)
        return ret

    def visit_sentence(self, node, visited_children):
        # logbook.debug("ArticleAstVisitor.visit_sentence {} {}", node, visited_children)
        return visited_children[0], node.text

    def visit_sentence_with_end(self, node, visited_children):
        # logbook.debug("ArticleAstVisitor.visit_sentence_with_end {} {}", node, visited_children)
        return visited_children[0]

    def visit_sentence_end_flag(self, node, visited_children):
        # logbook.debug("ArticleAstVisitor.visit_sentence_end_flag {} {}", node, visited_children)
        return None

    def visit_sentence_content(self, node, visited_children):
        # logbook.debug("ArticleAstVisitor.visit_sentence_content {} {}", node, visited_children)
        words = []
        for elem in visited_children:
            if elem:
                words.append(elem)
        return words

    def visit_sentence_content_elem(self, node, visited_children):
        # 必然是最后一行了
        # logbook.debug("ArticleAstVisitor.visit_sentence_content_elem {} {}", node, visited_children)
        return visited_children[0]

    def visit_word(self, node, visited_children):
        # logbook.debug("ArticleAstVisitor.word {} {}", node, visited_children)
        return node.text

    def visit_not_sentence_end_flag(self, node, visited_children):
        # logbook.debug("ArticleAstVisitor.visit_not_sentence_end_flag {} {}", node, visited_children)
        return None

    def visit_blank(self, node, visited_children):
        # logbook.debug("ArticleAstVisitor.visit_blank {} {}", node, visited_children)
        return None
