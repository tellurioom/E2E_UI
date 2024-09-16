import random

from selenium import webdriver
from selenium.webdriver.common.by import By

items = ["add-to-cart-sauce-labs-backpack",
         "add-to-cart-sauce-labs-bike-light",
         "add-to-cart-sauce-labs-bolt-t-shirt",
         "add-to-cart-sauce-labs-fleece-jacket",
         "add-to-cart-sauce-labs-onesie",
         "add-to-cart-test.allthethings()-t-shirt-(red)"]


def main():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")

    user_elem = driver.find_element(By.NAME, "user-name")
    user_elem.send_keys("standard_user")

    pass_elem = driver.find_element(By.NAME, value="password")
    pass_elem.send_keys("secret_sauce")

    log_button = driver.find_element(By.NAME, "login-button")
    log_button.click()

    buy_item = random.choice(items)
    buy_element = driver.find_element(By.NAME, buy_item)
    print(f"{buy_item}")
    buy_element.click()

    driver.get("https://www.saucedemo.com/cart.html")

    cart_list = driver.find_element(By.CLASS_NAME, "cart_list")
    el = list(cart_list.text.split("\n"))
    if len(el) == 1:
        raise Exception("Order failed")

    buy_button = driver.find_element(By.NAME, "checkout")
    buy_button.click()

    input_data = driver.find_element(By.NAME, "firstName")
    input_data.send_keys("John")
    input_data = driver.find_element(By.NAME, "lastName")
    input_data.send_keys("John")
    input_data = driver.find_element(By.NAME, "postalCode")
    input_data.send_keys("111111")

    continue_button = driver.find_element(By.NAME, "continue")
    continue_button.click()

    finish_button = driver.find_element(By.NAME, "finish")
    finish_button.click()

    elem = driver.find_element(By.CLASS_NAME, "complete-header")
    if elem.text == "Thank you for your order!":
        print("Order completed successfully", "\n")
    else:
        print(f"{elem.text}\n")
        raise Exception("Order failed")

    driver.quit()

main()

# while True:
#   main()
