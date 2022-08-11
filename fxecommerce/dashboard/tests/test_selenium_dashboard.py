import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



'''@pytest.mark.selenium
def test_new_admin_user(create_admin):
    assert create_admin.username == "admin"'''

@pytest.mark.selenium
def test_dashboard_admin_login(live_server, chrome_browser, django_database_fixture_setup):
    driver = chrome_browser
    driver.get(f'{live_server.url}/admin/login/')

    user_name = driver.find_element(By.XPATH, '//*[@id="id_username"]')
    user_password = driver.find_element(By.XPATH, '//*[@id="id_password"]')
    submit_button = driver.find_element(By.XPATH, '//input[@value="Log in"]')

    user_name.send_keys('admin')
    user_password.send_keys('password')
    submit_button.send_keys(Keys.RETURN)

    assert "Site administration" in driver.page_source
