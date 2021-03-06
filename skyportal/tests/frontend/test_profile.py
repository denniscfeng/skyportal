import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import uuid
import time


def test_add_token(driver, user):
    driver.get(f'/become_user/{user.id}')
    driver.get('/profile')
    driver.wait_for_xpath('//input[@name="acls_Comment"]')
    driver.wait_for_xpath('//input[@name="acls_Upload data"]')
    try:
        driver.wait_for_xpath('//input[@name="acls_Manage sources"]')
    except:
        pass
    else:
        raise Exception('ACLs list rendering error.')


def test_add_token(driver, super_admin_user):
    driver.get(f'/become_user/{super_admin_user.id}')
    driver.get('/profile')
    driver.wait_for_xpath('//input[@name="acls_Comment"]')
    driver.wait_for_xpath('//input[@name="acls_Upload data"]')
    driver.wait_for_xpath('//input[@name="acls_Manage sources"]')
    driver.wait_for_xpath('//input[@name="acls_Manage groups"]')
    driver.wait_for_xpath('//input[@name="acls_Become user"]')
    driver.wait_for_xpath('//input[@name="acls_System admin"]')
