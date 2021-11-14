from pages.base_page import BasePage
from pages.locators import MainPageLocators



class MainPage(BasePage):
    def go_to_button_translate(self): #переход по кнопке "Переводчик"
        button_translate = self.browser.find_element(*MainPageLocators.Translate)
        button_translate.click()


    def should_be_site(self): #Проверка лого (зашел на страницу)  и ссылки.
        assert self.is_element_present(*MainPageLocators.LOGO), "Сайт не открылся"
        assert self.get_current_url() == 'https://yandex.ru/'

    def should_be_URL(self): #вернуть ссылку и проверить ее
        assert self.get_current_url() == 'https://translate.yandex.ru/?utm_source=main_stripe_big'


    def go_to_change_lang(self): #нажатие кнопки для смены языка
        button_lang_change = self.browser.find_element(*MainPageLocators.button_change)
        button_lang_change.click()

    def text_input(self): #ввод текста
        ru = self.browser.find_element(*MainPageLocators.rus)
        ru.send_keys('текст')

    def translate_examination(self):   # проверка перевода
        en_text = self.browser.find_element(*MainPageLocators.en).text
        assert en_text == ('text'), 'ошибка в переводе'

    def change_window(self): # смена окна
        self.change()


