from selenium.common.exceptions import NoSuchElementException # показывает ошибку при наличии исключения


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def __init__(self, browser, url, timeout=10):   #для неявного ожидания элемента
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what): #  наличие элементаа
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def get_current_url(self):
        return self.browser.current_url


    def change(self):
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
