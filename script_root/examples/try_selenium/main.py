import logbook
from seleniumwire import  webdriver
# import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By as FindElemBy
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui
import time

def response_interceptor(request, response):
    # logbook.debug("response_interceptor {}", request.url)
    pass

def main(arg_list):
    logbook.debug("1111111111111111")

    # driver = webdriver.Chrome()
    driver = webdriver.Chrome()

    driver.response_interceptor = response_interceptor
    logbook.debug("reach here 2")
    driver.get("https://www.baidu.com/")

    img_elem = driver.find_element(FindElemBy.ID, "s_lg_img")
    if False:
        action = ActionChains(driver)
        action.move_to_element(img_elem)
        action.context_click(img_elem).perform()
        action.perform()
        for i in range(8):
            pyautogui.press("down")
        pyautogui.press("enter")
        time.sleep(1)
        # pyautogui.press(["a", ".", "p", "n", "g"])
        pyautogui.write("tupian1")
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.press("left")
        pyautogui.press("enter")

    if False:
        kw_input = driver.find_element(FindElemBy.ID, "kw")
        kw_input.send_keys("hello world")
        submit_btn = driver.find_element(FindElemBy.ID, "su")
        submit_btn.submit()
    logbook.debug("reach here 3")

    for req in driver.requests:
        # logbook.debug("request {} \n resp {}", req.url, req.response.body)
        pass
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
