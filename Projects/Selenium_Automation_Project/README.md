# Selenium Python Automation Framework

## Project Overview

This project is a Selenium Python automation framework developed using
Page Object Model (POM), PyTest, Unittest, CSV-based test data,
configuration management, explicit waits, failure screenshots, and HTML
test reporting.

The project automates selected login and product-search scenarios on
AutomationExercise.

---

## Technologies Used

- Python
- Selenium WebDriver
- PyTest
- Unittest
- HTML Test Reporting
- CSV
- Page Object Model
- Git/GitHub

---

## Project Structure

```text
Project/
│
├── config/
│   └── config.ini
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   └── search_page.py
│
├── reports/
│   ├── screenshots/
│   └── report.html
│
├── test_data/
│   ├── login_data.csv
│   └── search_data.csv
│
├── tests/
│   ├── test_csv_unittest.py
│   ├── test_csv_validation.py
│   ├── test_login.py
│   └── test_search.py
│
├── utilities/
│   ├── config_reader.py
│   ├── csv_reader.py
│   ├── driver_factory.py
│   └── screenshot.py
│
├── conftest.py
├── requirements.txt
├── .gitignore
└── README.md
Framework Features
Page Object Model

Page-specific locators and actions are maintained inside page classes.

LoginPage
SearchPage
BasePage

Common Selenium operations such as clicking, entering text, retrieving
text, and explicit waits are maintained in BasePage.

Data-Driven Testing

Test data is stored in CSV files and read using the CSVReader utility.

PyTest parametrization executes the same test with multiple sets of
CSV data.

CSV Validation

The framework validates:

Required CSV columns
Required field values
Configuration Management

The application URL is maintained in:

config/config.ini

and accessed through ConfigReader.

WebDriver Factory

Browser creation and browser configuration are centralized in:

utilities/driver_factory.py
Failure Screenshots

A PyTest hook captures a screenshot when a Selenium test fails.

Screenshots are stored in:

reports/screenshots/
HTML Reporting

PyTest HTML reporting is used to generate:

reports/report.html
Unittest

A small Unittest component is included to validate CSV data availability.

Test Scenarios
Login

The login test uses invalid credentials from:

test_data/login_data.csv

Each CSV row is executed as a separate parametrized test.

Product Search

The search test uses product names from:

test_data/search_data.csv

Each product search is executed as a separate parametrized test.

CSV Validation

The framework validates the structure and required fields of the login
and search CSV files.

Installation

Create and activate a Python virtual environment:

python3 -m venv venv
source venv/bin/activate

Install project dependencies:

pip install -r requirements.txt
Running the Tests

Run the complete test suite:

pytest -v
Generate HTML Report

Run:

pytest -v --html=reports/report.html --self-contained-html

The generated report will be available at:

reports/report.html
Test Result

The complete test suite currently contains:

2 login tests
3 search tests
2 CSV validation tests
2 Unittest tests

Total: 9 tests

All current tests are passing.