import configparser
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from Actions.PageActions import UserActions
from Locators.page_locators import MomoLocators


class Selenium:
    @staticmethod
    def getMomoLogin(OptionType='--head'):
        # get config info
        config = configparser.ConfigParser()
        config.read(r"config.txt")
        URL = config.get('MOMO_LOGIN_PAGE', 'login_url')
        account = config.get('MOMO_LOGIN_PAGE', 'momo_account')
        password = config.get('MOMO_LOGIN_PAGE', 'momo_password')

        # config_checker
        if len(account) == 0:
            print("[警告請在 config.txt 輸入帳號")
            raise

        if len(password) == 0:
            print("[警告]請在 config.txt 輸入密碼")
            raise

        # initial
        global driver, wait, locators, actions
        chrome_options = Options()
        chrome_options.add_argument(OptionType)
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=chrome_options
        )
        wait = WebDriverWait(driver, 10)  # set max wait 10 sec
        actions = UserActions(driver=driver, wait=wait)
        locators = MomoLocators()

        # goto URL
        driver.get(URL)
        # driver.set_window_size(1920, 1080)
        driver.maximize_window()

        return account, password, driver, locators, actions


class LoginHelper:
    def loginFlow(self, OptionType):
        max_retries = 4
        retries = 0
        driver = None

        while retries < max_retries:
            try:
                account, password, driver, locators, actions = self._execute(
                    OptionType)
                if driver is not None:
                    return account, password, locators, actions, driver
            except Exception as e:
                print(f'Exception during login attempt {retries + 1} Msg: {e}')

            retries = retries + 1
            if retries < max_retries:
                time.sleep(2 ** retries)
                print(f'sleep: {2 ** retries} sec')

        raise Exception('Login failed after retries.')

    def _execute(self, OptionType):
        account, password, driver, locators, actions = Selenium.getMomoLogin(
            OptionType)
        return account, password, driver, locators, actions
