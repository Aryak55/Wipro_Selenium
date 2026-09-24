import unittest

from utilities.csv_reader import CSVReader


class TestCSVReader(unittest.TestCase):

    def test_login_csv_has_data(self):

        data = CSVReader.read_csv(
            "test_data/login_data.csv"
        )

        self.assertGreater(
            len(data),
            0
        )

    def test_search_csv_has_data(self):

        data = CSVReader.read_csv(
            "test_data/search_data.csv"
        )

        self.assertGreater(
            len(data),
            0
        )


if __name__ == "__main__":
    unittest.main()