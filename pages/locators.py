from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
    LOGIN_EMAIL = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD1 = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD2 = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")