from pages.main_page import MainPage
import time

#Для запуска теста используй команду "pytest -s -v --browser_name=chrome test_yandex.py"

def test_open_yandex(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    assert browser.current_url == 'https://yandex.ru/'
    page.should_be_site()
    page.go_to_button_translate()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    assert browser.current_url == 'https://translate.yandex.ru/?utm_source=main_stripe_big'
    page.go_to_change_lang()
    time.sleep(1)
    page.text_input()
    time.sleep(1)
    page.translate_examination()
