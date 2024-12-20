import time
import json
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Setup WebDriver
def setup_driver():
    driver = webdriver.Chrome(executable_path="path/to/chromedriver")
    driver.maximize_window()
    return driver

# Amazon Login Function
def login_to_amazon(driver, username, password):
    driver.get("https://www.amazon.in/")
    
    try:
        sign_in_btn = driver.find_element(By.ID, "nav-link-accountList")
        sign_in_btn.click()
        time.sleep(2)

        email_input = driver.find_element(By.ID, "ap_email")
        email_input.send_keys(username)
        driver.find_element(By.ID, "continue").click()
        time.sleep(2)

        password_input = driver.find_element(By.ID, "ap_password")
        password_input.send_keys(password)
        driver.find_element(By.ID, "signInSubmit").click()
        time.sleep(3)

    except Exception as e:
        print(f"Login failed: {e}")
        driver.quit()

# Scraping Functionality
def scrape_category(driver, category_url, category_name):
    driver.get(category_url)
    time.sleep(2)

    products = []
    
    while len(products) < 1500:
        product_elements = driver.find_elements(By.CSS_SELECTOR, "div.zg-grid-general-faceout")

        for product in product_elements:
            try:
                name = product.find_element(By.CSS_SELECTOR, "span.a-text-normal").text
                price = product.find_element(By.CSS_SELECTOR, "span.a-price-whole").text
                discount = product.find_element(By.CSS_SELECTOR, "span.discount").text
                
                if "%" in discount and int(discount.replace("%", "")) > 50:
                    products.append({
                        "Name": name,
                        "Price": price,
                        "Discount": discount,
                        "Category": category_name
                    })
            except NoSuchElementException:
                continue

        try:
            next_button = driver.find_element(By.CSS_SELECTOR, "ul.a-pagination li.a-last a")
            next_button.click()
            time.sleep(3)
        except NoSuchElementException:
            break

    return products

# Save Data to File
def save_to_csv(data, filename="output.csv"):
    keys = data[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

# Main Function
def main():
    username = input("Enter Amazon username: ")
    password = input("Enter Amazon password: ")

    categories = [
        {"url": "https://www.amazon.in/gp/bestsellers/kitchen/ref=zg_bs_nav_kitchen_0", "name": "Kitchen"},
        {"url": "https://www.amazon.in/gp/bestsellers/shoes/ref=zg_bs_nav_shoes_0", "name": "Shoes"},
        {"url": "https://www.amazon.in/gp/bestsellers/computers/ref=zg_bs_nav_computers_0", "name": "Computers"},
        {"url": "https://www.amazon.in/gp/bestsellers/electronics/ref=zg_bs_nav_electronics_0", "name": "Electronics"}
        # Add more categories as needed
    ]

    driver = setup_driver()
    login_to_amazon(driver, username, password)

    all_products = []

    for category in categories:
        print(f"Scraping category: {category['name']}")
        category_products = scrape_category(driver, category["url"], category["name"])
        all_products.extend(category_products)

    driver.quit()
    save_to_csv(all_products)
    print(f"Scraping complete. Data saved to output.csv")

if __name__ == "__main__":
    main()
