from selenium.webdriver.common.by import By


class MomoLocators:
    # Login process
    login_iframe_locator = (By.CSS_SELECTOR, "iframe.loginIframe")
    account_locator = (By.XPATH, "//input[@type='text' and contains(@placeholder,'手機')]")
    password_locator = (By.XPATH, "//input[@type='password' and contains(@placeholder,'英數字')]")
    remember_me_locator = (By.XPATH, "//input[@class='checkbox']")
    button_login_locator = (By.CSS_SELECTOR, "a.login, button.login, input[type='submit']")

    # main page
    main_header_locator = (By.ID, "mainMomoHeader")
    footer_car = (By.XPATH, "//li[@class='cart']/a")
