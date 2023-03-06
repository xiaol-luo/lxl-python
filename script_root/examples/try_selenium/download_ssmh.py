import os.path
import sys

import logbook
import selenium.webdriver.support.wait
from seleniumwire import  webdriver
# import seleniumwire.undetected_chromedriver as uc
# import selenium.webdriver as webdriver
import seleniumwire
import seleniumwire.request
from selenium.webdriver.common.by import By as FindElemBy
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
import PIL
import io

def request_interceptor(request:seleniumwire.request.Request):
    pass

def response_interceptor(request:seleniumwire.request.Request , response:seleniumwire.request.Response, ext_data):
    if request.url.endswith(".jpg"):
        i = PIL.Image.open(io.BytesIO(response.body))
        save_path = os.path.join(ext_data["save_dir"], ext_data["file_prefix"] + os.path.basename(request.path))
        # save_path = "E:/tmp/images/" + ext_data["save_dir"] + str(ext_data["curr_page"]) + ".jpg"
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        i.save(save_path)

def try_next_page(driver, ext_data):
    div_page_num = driver.find_element(FindElemBy.CLASS_NAME, "newpagelabel")
    tmp_str_list = str.split(div_page_num.text, "/")
    curr_page = int(tmp_str_list[0])
    total_page = int(tmp_str_list[1])
    logbook.debug("xxxxxxxx {} {} {}", curr_page, total_page, curr_page == total_page)
    if curr_page == total_page:
        return False
    ext_data["curr_page"] = curr_page + 1
    btn_next_page = driver.find_element(FindElemBy.LINK_TEXT, "下一頁")
    btn_next_page.click()
    return True

def main(arg_list):
    import argparse
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("url")
    arg_parser.add_argument("save_dir")
    arg_parser.add_argument("file_prefix")
    parse_ret = arg_parser.parse_args(arg_list)
    opts = {
        'proxy' : {
            'http': "http://127.0.0.1:1081",
            'https': "http://127.0.0.1:1081",
            'no_proxy': "http://127.0.0.1,localhost",
        }
    }
    driver = webdriver.Chrome(seleniumwire_options=opts)
    ext_data = dict()
    # ext_data["begin_url"] = "https://www.wnacg.org/photos-view-id-9963883.html"
    ext_data["begin_url"] = parse_ret.url
    ext_data["save_dir"] = parse_ret.save_dir
    ext_data["file_prefix"] = parse_ret.file_prefix
    ext_data["curr_page"] = 1
    ext_data["driver"] = driver

    def response_cb(request:seleniumwire.request.Request , response:seleniumwire.request.Response):
        response_interceptor(request, response, ext_data)

    driver.response_interceptor = response_cb
    driver.request_interceptor = request_interceptor
    driver.get(ext_data["begin_url"])

    loop = 1
    while loop < 100000:
        if not try_next_page(ext_data["driver"], ext_data):
            break
        pass
    driver.close()

