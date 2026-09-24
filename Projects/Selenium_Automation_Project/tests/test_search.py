import pytest

from pages.search_page import SearchPage
from utilities.config_reader import ConfigReader
from utilities.csv_reader import CSVReader


search_data = CSVReader.read_csv("test_data/search_data.csv")


@pytest.mark.parametrize("data", search_data)
def test_search_product(driver, data):

    driver.get(ConfigReader.get_base_url())

    search_page = SearchPage(driver)

    # Open the Products page
    search_page.open_products_page()

    # Search for the product from CSV
    search_page.search_product(
        data["product_name"]
    )

    # Get the search results
    products = search_page.get_searched_products()

    # Validate the result
    assert data["expected_result"] == "found"
    assert len(products) > 0