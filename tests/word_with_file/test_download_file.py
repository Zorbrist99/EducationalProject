from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from tests.word_with_file.script_os import TMP_DIR

"""
Все команды с webDriver это настройка браузера под себя. 
Это как будто ты говоришь:
"Открой браузер, настрой его вот так, и отдай мне управление."
"""
"""
options = webdriver.ChromeOptions()
Создаёшь объект настроек браузера. Это как список параметров, который ты дашь браузеру при запуске.
"""
options = webdriver.ChromeOptions()

"""
Набор пользовательских настроек, которые мы можем выставить в браузере по-умолчанию
"""
prefs = {
    "download.default_directory": TMP_DIR,
    "download.prompt_for_download": False
}

options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
browser.config.driver = driver
