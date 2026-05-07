from selenium.webdriver.common.by import By

class OrderPageLocators:
    #Кнопки Заказать
    HEADER_ORDER_BUTTON=(By.XPATH, ".//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    FOOTER_ORDER_BUTTON=(By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")

    #Поля для заказа
    NAME=(By.CSS_SELECTOR, '[placeholder="* Имя"]')
    SURNAME=(By.CSS_SELECTOR, '[placeholder="* Фамилия"]')
    ADRESS=(By.CSS_SELECTOR, '[placeholder="* Адрес: куда привезти заказ"]')
    METRO=(By.CSS_SELECTOR, '[placeholder="* Станция метро"]')
    PHONE=(By.CSS_SELECTOR, '[placeholder="* Телефон: на него позвонит курьер"]')

    DATE=(By.CSS_SELECTOR, '[placeholder="* Когда привезти самокат"]')
    RENT_PERIOD=(By.XPATH, "//div[text()='* Срок аренды']/..//span[@class='Dropdown-arrow']")
    CHOOSE_RENTAL_PERIOD=(By.XPATH, ".//div[@class='Dropdown-menu']//div[text()='двое суток']")
    BLACK_COLOUR=(By.ID, "black")
    GREY_COLOUR=(By.ID, "grey")
    COMMENT=(By.CSS_SELECTOR, '[placeholder="Комментарий для курьера"]')

    #Кнопки подтверждения заказа
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")
    ORDER_BUTTON_IN_FORM = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")
    CONFIRM_YES = (By.XPATH, ".//button[text()='Да']")

    #Кнопки после успешного заказа
    SUCCESSFUL_ORDER = (By.XPATH, ".//div[contains(text(), 'Заказ оформлен')]")
    LOOK_STATUS_BUTTON = (By.XPATH, ".//div[@class='Order_Modal__YZ-d3']//button[text()='Посмотреть статус']")
