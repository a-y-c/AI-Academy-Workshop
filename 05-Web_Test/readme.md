# Sample Selenium Test

This guide will help you set up a simple Selenium test that checks if a webpage loads correctly and verifies the title. This example uses Chrome WebDriver.

## Prerequisites

Ensure you have Python installed on your machine. If not, download and install it from [here](https://www.python.org/downloads/).

## Step 1: Install Selenium and WebDriver Manager

Open your terminal or command prompt and run the following command to install Selenium and WebDriver Manager:

```bash
pip install selenium webdriver-manager
```
# Step 2: Create the Selenium Test

Create a file named `test_selenium.py` with the following content:

```python
# test_selenium.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def test_page_load():
    # Set up the Chrome WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

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
```

# Step 3: Run the Selenium Test

Navigate to the directory where you saved `test_selenium.py` and run the test with the following command:

```bash
python test_selenium.py
```
This script will open http://www.example.com, check the title of the page, verify the text of the heading, and then close the browser.

# Summary

1. **Install Selenium and WebDriver Manager**: Ensure you have the necessary packages installed.
2. **Create the Test Script**: Write your Selenium test script in Python.
3. **Run the Test**: Execute your test script to verify the webpage functionality.

Enjoy your testing adventure! What's next on your list?
