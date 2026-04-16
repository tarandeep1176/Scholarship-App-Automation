import pytest
import allure
from Libraries.Libraries import Import_libraries

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = Import_libraries.get_driver()

        if driver:
            screenshot = driver.get_screenshot_as_png()
            allure.attach(
                screenshot,
                name=f"{item.name}_failure",
                attachment_type=allure.attachment_type.PNG
            )
            print("Failure screenshot attached to Allure.")