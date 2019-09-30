# import time


def test_button_add_to_basket_is_on_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    # time.sleep(30)
    assert browser.find_element_by_css_selector("button.btn-add-to-basket"), "Кнопка добавления в корзину не найдена"
