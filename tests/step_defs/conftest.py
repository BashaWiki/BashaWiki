"""
This module contains shared fixtures, steps, and hooks.
"""
import pytest
from selenium import webdriver
from webdrivermanager import ChromeDriverManager
import os

driver_path = "./venv/Scripts/chromedriver.exe"


@pytest.fixture
def browser():
    # if os.path.isfile('./Scripts/chromedriver.exe'):
    # global driver_path
    # if driver_path == "":
    #     driver_link, driver_path = ChromeDriverManager().download_and_install()
    # # print(os.path.isfile(driver_path))
    driver = webdriver.Chrome(
        executable_path=driver_path)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def pytest_bdd_before_scenario(request, feature, scenario):
    print("called before scenario")


def pytest_bdd_after_scenario(request, feature, scenario):
    print("called after scenario")


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')
