# test_selenium.py
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_page_load():
    # Set up the Chrome WebDriver
    driver = webdriver.Chrome()

    try:
        # Open the webpage
        driver.get("http://www.example.com")

        # Verify the title of the page
        assert "Example Domain" in driver.title

        # Find an element on the page (e.g., the <h1> tag)
        heading = driver.find_element(By.TAG_NAME, "h1")
        assert heading.text == "Example Domain"

        print("Test Passed")
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    test_page_load()
