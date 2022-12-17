from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_URL = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
    LOGIN_EMAIL = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD1 = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD2 = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")

class ProductPageLocators:
    ADD_TO_CART_BTN = (By.XPATH, "//button[contains(text(),'Добавить в корзину')]")

    PRODUCT_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    CART_PRODUCT_NAME = (By.XPATH, "//div[@class='alertinner ']/strong")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    CART_PRICE = (By.XPATH, "//div[@class='alertinner ']/p/strong")

    SUCCESS_BAR = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-success  fade in']")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    CART_LINK = (By.XPATH, "//a[@class='btn btn-default']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class CartPageLocators():
    CART_CONTENTS = (By.XPATH, "//form[@id='basket_formset']")
    EMPTY_CART_CONTENTS = (By.XPATH, "//div[@id='content_inner']/p")
