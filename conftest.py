import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from helper import OrderDataHelper
from URL import MAIN_URL

@pytest.fixture
def driver():
    driver=webdriver.Firefox()
    driver.maximize_window()
    driver.get(MAIN_URL)
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 20)

@pytest.fixture
def data_for_order():
    return OrderDataHelper.generate_order_data()