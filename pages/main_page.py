from pages.base_page import BasePage
from pages.locators import MainPageLocators



class MainPage(BasePage):
    def go_to_button_translate(self): #переход по кнопке "Переводчик"
        button_translate = self.browser.find_element(*MainPageLocators.Translate)
        button_translate.click()


    def should_be_site(self): #Проверка лого (зашел на страницу)
        assert self.is_element_present(*MainPageLocators.LOGO), "Сайт не открылся"

    def should_be_URL(self, browser): #проба вернуть ссылку и проверить ее
        url = browser.current_url
        assert url == 'https://translate.yandex.ru/?utm_source=main_stripe_big'


    def go_to_change_lang(self): #нажатие кнопки для смены языка
        button_lang_change = self.browser.find_element(*MainPageLocators.button_change)
        button_lang_change.click()

    def text_input(self): #ввод текста
        ru = self.browser.find_element(*MainPageLocators.rus)
        ru.send_keys('текст')

    def translate_examination(self):   # проверка перевода
        en_text = self.browser.find_element(*MainPageLocators.en).text
        assert en_text == ('text'), 'ошибка в переводе'


