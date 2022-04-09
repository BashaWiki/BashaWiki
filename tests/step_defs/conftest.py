"""
This module contains shared fixtures, steps, and hooks.
"""
import pytest
from selenium import webdriver
from webdrivermanager import ChromeDriverManager
import os
from utils.driver import Test_driver

driver_path = "./venv/Scripts/chromedriver.exe"


@pytest.fixture
def browser():
    #     driver_link, driver_path = ChromeDriverManager().download_and_install()
    browser = Test_driver().get_driver(os.getenv("BROWSER"))
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
