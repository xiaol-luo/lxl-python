import logbook

from . import caiyun
import time
from script_root.libs.third_part.ECDICT.stardict import DictCsv

do_translate_words = caiyun.translate_words
do_translate_sentences = caiyun.translate_sentences


def translate_words(word_list, cb_fn=None):
    out_list = do_translate_words(word_list)
    if cb_fn:
        cb_fn(word_list, out_list)
    time.sleep(10)
    return out_list


def translate_sentences(sentence_list, cb_fn=None):
    out_list = do_translate_words(sentence_list)
    if cb_fn:
        cb_fn(sentence_list, out_list)
    time.sleep(10)
    return out_list


def test():
    dt:DictCsv = DictCsv("D:/work_space/code/lxl-python/script_root/libs/third_part/ECDICT/ecdict.csv")
    ret = dt.query("got")
    logbook.debug("query reasult {0}", ret)
