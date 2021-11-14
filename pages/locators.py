from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGO = (By.CSS_SELECTOR, ".home-logo__default")
    Translate = (By.CSS_SELECTOR, 'body > div.body__wrapper > div.container.rows > div.row.rows__row.rows__row_main > div > div.container.container__services.container__line > nav > div > ul > li:nth-child(8) > a > div.services-new__icon')
    button_change = (By.CSS_SELECTOR, '#translator > div.translator-container > div.langs-panel > button.langs-swapButton > svg')
    rus = (By.CSS_SELECTOR,'#fakeArea')
    en = (By.CSS_SELECTOR,'#translation')