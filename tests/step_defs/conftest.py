"""
This module contains shared fixtures, steps, and hooks.
"""
import pytest
from selenium import webdriver
from webdrivermanager import ChromeDriverManager
import os
from utils import driver

driver_path = "./venv/Scripts/chromedriver.exe"


@pytest.fixture
def browser():
    # if os.path.isfile('./Scripts/chromedriver.exe'):
    # global driver_path
    # if driver_path == "":
    #     driver_link, driver_path = ChromeDriverManager().download_and_install()
    # # print(os.path.isfile(driver_path))
    print('browser started')
    b = driver.Test_driver()
    browser = b.get_driver("edge")
    # browser = webdriver.Chrome(
    #     executable_path=driver_path)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
    print('browser closed')


def pytest_bdd_before_scenario(request, feature, scenario):
    print("called before scenario")


def pytest_bdd_after_scenario(request, feature, scenario):
    print("called after scenario")


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')


