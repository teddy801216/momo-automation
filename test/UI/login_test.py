from Actions.Selenium import LoginHelper
from OpenAI.OpenAPI import OpenAIHelper

loginHelper = LoginHelper()
openAiHelper = OpenAIHelper()


def test_login_2FA():
    account, password, locators, actions, driver = loginHelper.loginFlow(OptionType='--head')
    actions.Login(account=account, password=password, locators=locators)
    # check if login show 2FA
    result = openAiHelper.compare_screen_with_image(r'./test/image/2FA_NOTIFY.png')
    assert result is True
    driver.quit()
