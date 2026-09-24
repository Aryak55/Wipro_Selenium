import pytest

from pages.login_page import LoginPage
from utilities.config_reader import ConfigReader
from utilities.csv_reader import CSVReader


login_data = CSVReader.read_csv("test_data/login_data.csv")


@pytest.mark.parametrize("data", login_data)
def test_invalid_login(driver, data):

    driver.get(ConfigReader.get_base_url())

    login_page = LoginPage(driver)

    login_page.open_login_page()

    login_page.login(
        data["email"],
        data["password"]
    )

    error_message = login_page.get_login_error()

    assert data["expected_result"] == "failure"

    assert error_message == "Your email or password is incorrect!"