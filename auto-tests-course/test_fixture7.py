import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

# @pytest.mark.parametrize('language', ["ru", "en-gb"])
# #class TestLogin:
# def test_guest_should_see_login_link(browser, language):
#     link = "http://selenium1py.pythonanywhere.com/{%s}" %(language)
#     browser.get(link)
#     browser.find_element_by_css_selector("#login_link")

@pytest.mark.parametrize('links_id',["236895","236896","236897","236898","236899","236903","236904","236905"])
#@pytest.mark.parametrize('answer',["math.log(int(time.time()))"])
def test_gather_info_for_answer(browser,links_id):
    answer = math.log(int(time.time()))
    timeForAnswer = str(answer)

    link = "https://stepik.org/lesson/%s/step/1" %(links_id)
    browser.get(link)

    time.sleep(5)

    input1 = browser.find_element_by_tag_name('textarea').send_keys(timeForAnswer)
    time.sleep(2)


    submit = browser.find_element_by_css_selector("div.attempt__actions > button").click()
    time.sleep(2)

    result = browser.find_element_by_css_selector('[class*="smart-hints__hint"]')
    finalResult = result.text
    assert "Correct!" == finalResult
    print(finalResult)
