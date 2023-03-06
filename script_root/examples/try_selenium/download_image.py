import logbook
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
    # logbook.debug("request_interceptor {} {}", request.url, type(request))
    pass

def response_interceptor(request:seleniumwire.request.Request , response:seleniumwire.request.Response, ext_data):
    # logbook.debug("response_interceptor {} {} {}", request.path, type(request), type(response))
    if request.url.endswith(".jpg"):
        i = PIL.Image.open(io.BytesIO(response.body))
        # i.save("E:/tmp/images/" + str(request.path.replace("/", "_")) + ".jpg")
        i.save("E:/tmp/images/" + ext_data["save_dir"] + str(ext_data["curr_page"]) + ".jpg")
        pass
    '''
    if request.url.endswith(".mp3"):
        logbook.warn("find mp3 {}", request.url)
    '''

def main(arg_list):
    logbook.debug("1111111111111111")

    # chrome_opt = selenium.webdriver.ChromeOptions()
    # chrome_opt.add_argument("--proxy-server=http://127.0.0.1:1081")
    # chrome_opt.add_argument("proxy-server=socks5://127.0.0.1:1081")
    # driver = webdriver.Chrome()

    opts = {
        'proxy' : {
            'http': "http://127.0.0.1:1081",
            'https': "http://127.0.0.1:1081",
            'no_proxy': "http://127.0.0.1,localhost",
        }
    }
    driver = webdriver.Chrome(seleniumwire_options=opts)
    # driver = webdriver.Chrome()
    # driver:uc.Chrome = uc.Chrome(seleniumwire_options=opts)


    ext_data = dict()
    ext_data["save_dir"] = "a/"
    ext_data["curr_page"] = 1

    def response_cb(request:seleniumwire.request.Request , response:seleniumwire.request.Response):
        response_interceptor(request, response, ext_data)

    driver.response_interceptor = response_cb
    driver.request_interceptor = request_interceptor
    driver.get("https://www.wnacg.org/photos-view-id-9880562.html")



    #for req in driver.requests:
        # logbook.debug("request {} \n resp {}", req.url, req.response and req.response.body or "")
    #    pass

    loop = 1
    while loop < 100000:
        loop = loop + 1
        # driver.forward()
        # next_btn = driver.find_element(FindElemBy.CLASS_NAME, "nextpostslink")
        # next_btn.click()
        # logbook.debug("next_btn {}", type(next_btn))
        div_page_num = driver.find_element(FindElemBy.CLASS_NAME, "newpagelabel")
        b_curr_page = div_page_num.find_element(FindElemBy.XPATH, "b")
        str_curr_page = b_curr_page.text
        str_total_page = div_page_num.text
        logbook.debug("xxxx {} {}", str_curr_page, str_total_page)
        btn_next_page = driver.find_element(FindElemBy.LINK_TEXT, "下一頁")
        btn_next_page.click()
        ext_data["curr_page"] = int(str_curr_page) + 1
        if "/" + str_curr_page == str_total_page:
            break
    time.sleep(10)
    clear_chrome_cache_new(driver)
    time.sleep(10)
    logbook.debug("test, {}", driver.title)


def clear_chrome_cache(driver: webdriver.Chrome):
    driver = webdriver.Chrome()
    # 设置隐式等待
    driver.implicitly_wait(10)
    # 清除缓存提示框
    driver.get('chrome://settings/clearBrowserData')
    # 2S 等待时间
    time.sleep(2)
    clearButton = driver.execute_script(
        "return document.querySelector('settings-ui').shadowRoot.querySelector('settings-main').shadowRoot.querySelector('settings-basic-page').shadowRoot.querySelector('settings-section > settings-privacy-page').shadowRoot.querySelector('settings-clear-browsing-data-dialog').shadowRoot.querySelector('#clearBrowsingDataDialog').querySelector('#clearBrowsingDataConfirm')")
    clearButton.click()

def clear_chrome_cache_new(driver: webdriver.Chrome):
    driver.get('chrome://version')
    path_elem = driver.find_element(FindElemBy.ID, "profile_path")
    logbook.debug("path_elem.text {}", path_elem.text)
    import os
    cache_path = os.path.join(path_elem.text, "Cache/Cache_Data")
    logbook.debug("cache_path {}", cache_path)
    import shutil
    shutil.rmtree(cache_path) # 权限不够删除文件， 这个函数不可用
