from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time

def test_01():
    driver = Chrome()
    driver.implicitly_wait(10)
    driver.get('https://ecoflowukraine.com')

    product_locator = "//a[@class='products-menu__title-link'][contains(text(),'Продукти')]"
    hover_element_1 = driver.find_element(by='xpath', value=product_locator)
    ActionChains(driver).move_to_element(hover_element_1).perform()

    delta2_locator = "//a[contains(text(), 'Лінійка DELTA 2')]"
    element2 = driver.find_element(by='xpath', value=delta2_locator)
    element2.click()
    result_page_delta_2_locator = "//h1[@id='j-catalog-header']"
    result_page_delta_2_locator = driver.find_element(by='xpath', value=result_page_delta_2_locator)
    assert (result_page_delta_2_locator.text == "Лінійка DELTA 2")

def test_02():
    driver = Chrome()
    driver.implicitly_wait(10)  # Implicit wait
    driver.get('https://ecoflowukraine.com')
    product_locator = "//a[@class='products-menu__title-link'][contains(text(),'Продукти')]"
    element = driver.find_element(by='xpath', value=product_locator)
    element.click()
    time.sleep(5)
    pagination_locator = "//span[normalize-space()='2']"
    pagination_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pagination_locator)))
    pagination_element.click()
    time.sleep(5)
    expected_url = "https://ecoflowukraine.com/products/filter/page=2/"
    assert driver.current_url == expected_url

def test_03():
    driver = Chrome()
    driver.implicitly_wait(10)  # Implicit wait
    driver.get('https://ecoflowukraine.com')
    product_locator = "//a[@class='products-menu__title-link'][contains(text(),'Продукти')]"
    element = driver.find_element(by='xpath', value=product_locator)
    element.click()
    time.sleep(5)
    lower_price_first_locator ="// span[contains(text(), 'спочатку дешевше')]"
    element = driver.find_element(by='xpath', value=lower_price_first_locator)
    element.click()
    time.sleep(5)
    expected_url = "https://ecoflowukraine.com/products/filter/sort_price=ASC/"
    assert driver.current_url == expected_url

def test_04():
    driver = Chrome()
    driver.implicitly_wait(10)  # Implicit wait
    driver.get('https://ecoflowukraine.com')
    product_locator = "//a[@class='products-menu__title-link'][contains(text(),'Продукти')]"
    element = driver.find_element(by='xpath', value=product_locator)
    element.click()
    time.sleep(5)
    search_input_field_locator = "//input[@placeholder='пошук товарів']"
    search_input_field = driver.find_element(by='xpath', value=search_input_field_locator)
    search_input_field.send_keys("DELTA 2")
    search_button_locator = "//button[@class='search__button j-search-button']//*[name()='svg']"
    search_button = driver.find_element(by='xpath', value=search_button_locator)
    search_button.click()


'''def test_05():
    driver = Chrome()
    driver.implicitly_wait(10)  # Implicit wait
    driver.get('https://ecoflowukraine.com')
    product_locator = "//a[@class='products-menu__title-link'][contains(text(),'Продукти')]"
    driver.find_element(by='xpath', value=product_locator).click()
    time.sleep(5)
    max_price_input_locator = "//input[@name='filter[price][max]']"
    max_price_input = driver.find_element(by='xpath', value=max_price_input_locator )
    max_price_input.clear()
    max_price_input.send_keys("0")
    max_price_input.send_keys(Keys.RETURN)
    time.sleep(5)
    ok_button_locator = "//span[contains(text(),'ОК')]"
    ok_button = driver.find_element(by='xpath', value=ok_button_locator)
    ok_button.click()
    time.sleep(5)
    result_locator = "//a[@title='Зарядна станція EcoFlow DELTA Pro Ultra']"
    result_locator_Pro_Ultra = driver.find_element(by='xpath', value=result_locator)
    assert (result_locator_Pro_Ultra.text == "Зарядна станція EcoFlow DELTA Pro Ultra")'''


def test_06():
    driver = Chrome()
    driver.implicitly_wait(10)  # Implicit wait
    driver.get('https://ecoflowukraine.com')
    product_locator = "//a[@class='products-menu__title-link'][contains(text(),'Продукти')]"
    driver.find_element(by='xpath', value=product_locator).click()
    time.sleep(5)
    pagination_locator = "//span[normalize-space()='3']"
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pagination_locator))).click()
    time.sleep(5)
    expected_url = "https://ecoflowukraine.com/products/filter/page=3/"
    assert driver.current_url == expected_url