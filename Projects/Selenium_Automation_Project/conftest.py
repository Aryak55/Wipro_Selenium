import pytest

from utilities.driver_factory import DriverFactory
from utilities.screenshot import Screenshot


@pytest.fixture
def driver():
    driver = DriverFactory.create_driver()

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:
            Screenshot.take_screenshot(
                driver,
                item.name
            )