from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from pages.base_page import BasePage


class SearchPage(BasePage):

    PRODUCTS_BUTTON = (
        By.CSS_SELECTOR,
        "a[href='/products']"
    )

    SEARCH_INPUT = (
        By.ID,
        "search_product"
    )

    SEARCH_BUTTON = (
        By.ID,
        "submit_search"
    )

    SEARCHED_PRODUCTS = (
        By.XPATH,
        "//div[@class='features_items']//div[contains(@class, 'productinfo')]"
    )

    def close_ad_if_present(self):

        try:
            close_button = self.driver.find_element(
                By.CSS_SELECTOR,
                "i[class='fa-times']"
            )

            self.click(close_button)

        except (NoSuchElementException, TimeoutException):
            pass

    def open_products_page(self):

        self.close_ad_if_present()

        self.click(
            self.wait_for_element(self.PRODUCTS_BUTTON)
        )

    def search_product(self, product_name):

        self.close_ad_if_present()

        self.enter_text(
            self.wait_for_element(self.SEARCH_INPUT),
            product_name
        )

        self.click(
            self.wait_for_element(self.SEARCH_BUTTON)
        )

    def get_searched_products(self):

        return self.wait.until(
            lambda driver: driver.find_elements(
                *self.SEARCHED_PRODUCTS
            )
        )