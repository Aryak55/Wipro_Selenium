from selenium import webdriver


class DriverFactory:

    @staticmethod
    def create_driver():

        options = webdriver.ChromeOptions()

        options.page_load_strategy = "eager"

        driver = webdriver.Chrome(options=options)

        driver.maximize_window()

        return driver