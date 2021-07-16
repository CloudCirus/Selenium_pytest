import pytest
from selenium import webdriver


def test_add_to_cart_button(browser: webdriver.Chrome):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    browser.implicitly_wait(5)
    button = browser.find_element_by_css_selector('.btn-add-to-basket')
    button.click()
    alert = browser.find_element_by_tag_name('strong').text
    assert alert, 'alert is not "Deferred benefit offer"'
