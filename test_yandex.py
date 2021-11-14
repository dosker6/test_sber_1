from pages.main_page import MainPage
import time


#Для запуска теста используйте команду "pytest -s -v --browser_name=chrome test_yandex.py"

def test_open_yandex(browser):
    url = "https://yandex.ru/"
    page = MainPage(browser, url)
    page.open()                                  #открытие ссылки
    page.should_be_site()                        #проверка адреса сайта и отображение логотипа
    page.go_to_button_translate()                #переход на страницу переводчик
    page.change_window()                         #смена окна
    page.should_be_URL()                         #проверка адреса переводчик
    page.go_to_change_lang()                     #нажатие кнопки для смены языка ввода
    page.text_input()                            #ввод текста
    time.sleep(1)
    page.translate_examination()                 #проверка правильности перевода
