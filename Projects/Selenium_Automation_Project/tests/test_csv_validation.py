from utilities.csv_reader import CSVReader


def test_login_csv_validation():

    is_valid = CSVReader.validate_csv(
        "test_data/login_data.csv",
        ["email", "password", "expected_result"]
    )

    assert is_valid is True


def test_search_csv_validation():

    is_valid = CSVReader.validate_csv(
        "test_data/search_data.csv",
        ["product_name", "expected_result"]
    )

    assert is_valid is True