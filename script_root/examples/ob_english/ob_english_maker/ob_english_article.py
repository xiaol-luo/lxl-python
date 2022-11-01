from __future__ import annotations

import parsimonious
import logbook
import typing

from . import ob_english_maker


class ArticleAstVisitorLine(object):
    content:str
    words:typing.List[str]

    def __init__(self):
        super(ArticleAstVisitorLine, self).__init__()
        self.content = ""
        self.words = []

    def __str__(self):
        return self.content or ""


class ObEnglishArticle(object):
    maker:ob_english_maker.ObEnglishMaker
    name:str
    content:str
    lines:typing.List[ArticleAstVisitorLine]

    def __init__(self, maker:ob_english_maker.ObEnglishMaker):
        super(ObEnglishArticle, self).__init__()
        self.maker = maker
        self.name = ""
        self.content = ""
        self.lines = []

    def parse_content(self):
        self.lines = []
        grammar = parsimonious.grammar.Grammar(r"""
            all = line*
            line =  line_with_end / line_without_end
            line_with_end = line_text line_end
            line_without_end = line_text_elem*
            line_end = "\n"
            line_text = line_text_elem*
            line_text_elem = blank / word / punctuation
            blank = " "
            word = ~r"[a-zA-Z0-9]+" 
            punctuation = ~r"[^a-zA-z0-9\n ]+"
        """)
        # ast_tree = grammar.parse(self.content)
        # content = "hello, world\nthis is cat"
        ast_tree = grammar.parse(self.content)
        visitor = ArticleAstVisitor(self)
        self.lines = visitor.visit(ast_tree)
        # logbook.debug("visit ret \n {}", lines)
        for line in self.lines:
            for word in line.words:
                self.maker.get_word(word)


class ArticleAstVisitor(parsimonious.nodes.NodeVisitor):
    def __init__(self, article:ObEnglishArticle):
        super(ArticleAstVisitor, self).__init__()
        self.article = article


    def visit_all(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_all {} {}", node, visited_children)
        ret = []
        for elem in visited_children:
            words = elem[0]
            line_content = elem[1]
            logbook.debug("ArticleAstVisitor.visit_all line {} {}", line_content, words)
            line_data = ArticleAstVisitorLine()
            line_data.content = line_content
            line_data.words = words
            ret.append(line_data)
        return ret

    def visit_line(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_line {} {}", node, visited_children)
        return visited_children[0]

    def visit_line_end(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.line_end {} {}", node, visited_children)
        return None

    def visit_line_with_end(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.line_with_end {} {}", node, visited_children)
        ret = []
        for elem in visited_children[0]:
            if elem:
                ret.append(elem)
        return ret, node.text

    def visit_line_without_end(self, node, visited_children):
        # 必然是最后一行了
        logbook.debug("ArticleAstVisitor.visit_line_without_end {} {}", node, visited_children)
        ret = []
        for elem in visited_children:
            if elem:
                ret.append(elem)
        return ret, node.text

    def visit_line_text(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_line_text {} {}", node, visited_children)
        ret = []
        for elem in visited_children:
            if elem:
                ret.append(elem)
        return ret

    def visit_line_text_elem(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_visit_line_text_elem {} {}", node, visited_children)
        if visited_children[0]:
            return visited_children[0]
        return None

    def visit_punctuation(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_punctuation {} {}", node, visited_children)
        return None

    def visit_word(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.word {} {}", node, visited_children)
        return node.text

    def visit_blank(self, node, visited_children):
        logbook.debug("ArticleAstVisitor.visit_blank {} {}", node, visited_children)
        return None
