from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGO_YANDEX = (By.XPATH, ".//img[@alt='Yandex']")
    LOGO_SCOOTER = (By.XPATH, ".//img[@alt='Scooter']")
    HEADER_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']")
    FOOTER_ORDER_BUTTON=(By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")
    COOKIE_BUTTON = (By.XPATH, "//button[contains(@class, 'App_CookieButton')]")
    