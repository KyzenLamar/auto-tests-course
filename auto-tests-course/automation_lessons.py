'''def test_substring(full_string, substring):
    assert substring in full_string,\
    f"expected '{substring}' to be substring of '{full_string}'"'''




'''def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result ,f"expected {expected_result}, got {actual_result}"'''


'''def test_substring(full_string, substring):
    assert substring in full_string, f"expected {'substring'} to be substring of {'full_string'}"'''


'''def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"

if __name__ == "__main__":
    test_abs1()
    print("All tests passed!")'''

#class TestWeb():
from selenium import webdriver
import time

def test_registrationCheck_1():
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Kод, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
    input3.send_keys("Smolensk@mail")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    # проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

def test_registrationCheck_2():
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Kод, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath('//input[@placeholder="Введите имя"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('//input[@placeholder="Введите фамилию"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath('//input[@placeholder="Введите Email"]')
    input3.send_keys("Smolensk@mail")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    # проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text

if __name__=='__main__':
    test_registrationCheck_1()
    test_registrationCheck_2()