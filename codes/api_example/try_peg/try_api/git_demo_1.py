from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor

log_debug = print


class ParseResultVisitor(NodeVisitor):
    def visit_root(self, node, visited_children):
        log_debug("visit_text::{}_{}".format(node, visited_children))
        ret = []
        for child in visited_children:
            ret.append(child)
        return ret

    def visit_blod_texts(self, node, visisted_children):
        return node.text

    def visit_blod_text(self, node, visited_children):
        log_debug("visit_blod_text::{}_{}".format(node, visited_children))
        _, text, _ = visited_children
        return text

    def visit_text(self, node, visited_children):
        log_debug("visit_text::{}_{}".format(node, visited_children))
        return node.text

    def visit_blod_open(self, node, visited_children):
        log_debug("visit_bold_open::{}_{}".format(node, visited_children))
        return node.text

    def visit_blod_close(self, node, visited_children):
        log_debug("visit_bold_close::{}_{}".format(node, visited_children))
        return node.text

    def visit_blank(self, node, visited_children):
        log_debug("visit_blank::{}_{}".format(node, visited_children))
        return ""

    def visit_blanks(self, node, visited_children):
        log_debug("visit_blanks::{}_{}".format(node, visited_children))
        return ""


def _main():
    grammar = Grammar(
        r"""
            root = blod_texts*
            blod_texts = blod_text / blanks  
            blanks = ~"\s*"
            blod_text = blod_open text blod_close 
            blod_open = "(("
            blod_close = "))"
            text = ~"[A-Z 0-9]*"i   
        """)
    ast_tree = grammar.parse(" ((hello 1))  ((hello 1))  ((hello 1))  ((hello 1)) ")
    # log_debug("parse retsule is {}".format(ast_tree))

    visitor = ParseResultVisitor()
    ret = visitor.visit(ast_tree)
    # log_debug("visit ret \n {}".format(ret))


if __name__ == "__main__":
    _main()


