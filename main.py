# Import required modules
import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Send a GET request to the Zillow Clone website
response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
print(response.status_code)  # Print the HTTP status code
data = response.text  # Get the HTML content

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find all property links
links = soup.select(".property-card-link")
link_list = [link.get("href") for link in links]

# Find all property addresses
addresses = soup.find_all("address")
add_list = [address.get_text().strip() for address in addresses]

# Find all property prices
prices = soup.select("span.PropertyCardWrapper__StyledPriceLine")
price_list = [price.get_text().replace("/mo", "").replace("+", "").strip() for price in prices]

# Wait for 10 seconds before starting form filling
time.sleep(10)

# Google Form link
FORM_LINK = Replace With Your Google Form link

# Set Chrome options to keep the browser open after script ends
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Start the Chrome browser
driver = webdriver.Chrome(options=chrome_options)
driver.get(FORM_LINK)  # Open the Google Form
wait = WebDriverWait(driver, 2)  # Set up explicit wait

# Loop through all properties and fill the form for each
for i in range(len(price_list)):
    # Fill address field
    fill_add = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")))
    fill_add.send_keys(add_list[i])

    # Fill price field
    fill_price = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    fill_price.send_keys(price_list[i])

    # Fill link field
    fill_link = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    fill_link.send_keys(link_list[i])

    # Click the submit button
    sub_form = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')))
    sub_form.click()
    time.sleep(1)  # Wait for the form to submit

    # Click the "Submit another response" link
    submit_another_response = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')))
    submit_another_response.click()
