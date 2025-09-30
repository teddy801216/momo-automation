from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.page_locators import MomoLocators
from selenium.common.exceptions import NoSuchElementException


class UserActions:
    def __init__(self, driver: WebDriver, wait: WebDriverWait):
        self.driver = driver
        self.wait = wait
        self.momoLocators = MomoLocators()

    def Login(self, account, password, locators: MomoLocators):
        # switch to iframe
        if not self._switch_to_login_iframe(locators, timeout=10):
            self._dump_inputs_in_current_frame()
            raise NoSuchElementException("Login iframe not found can't switch")

        # input account, password  on iframe
        input_account = self.wait.until(
            EC.element_to_be_clickable(locators.account_locator)
        )
        input_account.send_keys(account)

        input_password = self.wait.until(EC.element_to_be_clickable(
            locators.password_locator)
        )
        input_password.send_keys(password)

        # click remember_me on iframe
        remember_me = self.wait.until(EC.element_to_be_clickable(
            locators.remember_me_locator)
        )
        remember_me.click()  # default is clicked, click again for not remember

        # click login button on iframe
        button_login_locator = self.wait.until(EC.element_to_be_clickable(
            locators.button_login_locator)
        )
        button_login_locator.click()

        # assert self.wait.until(EC.element_to_be_clickable(locators.main_header_locator)) is True

    def _switch_to_login_iframe(self, locators: MomoLocators, timeout=10):
        self.driver.switch_to.default_content()  # switch to init page
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.frame_to_be_available_and_switch_to_it(
                    locators.login_iframe_locator  # start switch to iframe
                )
            )
            return True
        except Exception:
            print("Login iframe not found")
            return False

    def click_footer_car(self, locators: MomoLocators):
        footer_car = self.wait.until(EC.element_to_be_clickable(locators.footer_car))
        footer_car.click()

    def _dump_inputs_in_current_frame(self):
        inputs = self.driver.find_elements(By.CSS_SELECTOR, "input")
        print(f"[IFRAME] inputs = {len(inputs)}")
        for i, el in enumerate(inputs):
            print(i, {
                "id": el.get_attribute("id"),
                "name": el.get_attribute("name"),
                "class": el.get_attribute("class"),
                "type": el.get_attribute("type"),
                "placeholder": el.get_attribute("placeholder"),
            })

    def _dump_all_elements(self, tag="*"):
        """列印頁面上所有符合 tag 的元素資訊"""
        elems = self.driver.find_elements(By.CSS_SELECTOR, tag)
        print(f"[DUMP] 共找到 {len(elems)} 個元素")
        for i, el in enumerate(elems):
            attrs = {
                "tag": el.tag_name,
                "id": el.get_attribute("id"),
                "name": el.get_attribute("name"),
                "class": el.get_attribute("class"),
                "placeholder": el.get_attribute("placeholder"),
                "type": el.get_attribute("type"),
                "text": el.text.strip(),
            }
            print(f"[{i}] {attrs}")
