import time


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_book_to_basket(browser):
    browser.get(link)
    time.sleep(5)
    basket = browser.find_element_by_xpath('//*[@id="add_to_basket_form"]/button')
    #if basket:
    assert basket, "Button is not exist!"
