from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# логин-разлогин в админку с проверкой, что логин был выполнен
def test_login(browser):
    browser.get(f"{browser.base_url}/administration")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.ID, "form-login")))
    username_input = wait.until(EC.presence_of_element_located((By.ID, "input-username")))
    password_input = wait.until(EC.presence_of_element_located((By.ID, "input-password")))
    username_input.send_keys("user")
    password_input.send_keys("bitnami")
    wait.until(EC.visibility_of_element_located((By.ID, "form-login")))
    login_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "btn-primary")))
    login_button.click()
    logout_button = wait.until(EC.presence_of_element_located((By.ID, "nav-logout")))
    logout_button.click()
