from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")

    SIGNUP_LOGIN = (
        By.XPATH,
        "//a[contains(text(), 'Signup / Login')]"
    )

    LOGIN_ERROR = (
        By.XPATH,
        "//*[contains(text(), 'Your email or password is incorrect!')]"
    )

    def open_login_page(self):
        self.click(
            self.wait_for_element(self.SIGNUP_LOGIN)
        )

    def login(self, email, password):
        self.enter_text(
            self.wait_for_element(self.EMAIL_INPUT),
            email
        )

        self.enter_text(
            self.wait_for_element(self.PASSWORD_INPUT),
            password
        )

        self.click(
            self.wait_for_element(self.LOGIN_BUTTON)
        )

    def get_login_error(self):
        return self.wait_for_element(self.LOGIN_ERROR).text