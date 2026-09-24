import os


class Screenshot:

    @staticmethod
    def take_screenshot(driver, test_name):

        screenshot_folder = "reports/screenshots"

        os.makedirs(
            screenshot_folder,
            exist_ok=True
        )

        file_path = os.path.join(
            screenshot_folder,
            f"{test_name}.png"
        )

        driver.save_screenshot(file_path)