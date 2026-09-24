import csv


class CSVReader:

    @staticmethod
    def read_csv(file_path):
        with open(file_path, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)

    @staticmethod
    def validate_csv(file_path, required_columns):
        with open(file_path, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            # Check required columns
            for column in required_columns:
                if column not in reader.fieldnames:
                    return False

            # Check that required fields are not empty
            for row in reader:
                for column in required_columns:
                    if not row[column].strip():
                        return False

        return True