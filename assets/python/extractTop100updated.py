from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By  # Import Statement for By: Added to enable the use of By class for locating elements
from bs4 import BeautifulSoup
import random
import time
import pandas as pd
import os
from datetime import datetime  # Import Statement for datetime: Added for generating unique filenames with timestamps

# Setup Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # Headless mode for running without a GUI
chrome_options.add_argument("--no-sandbox")  # Required for some environments
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")  # Set user agent

# Start the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    url = "https://starngage.com/plus/ta/influencer/ranking/youtube/united-states/technology?page=2"  # URL to scrape
    driver.get(url)

    time.sleep(random.uniform(5, 10))  # Random sleep to mimic human behavior

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))  # Wait until the page is fully loaded
    )

    page_source = driver.page_source  # Get the page source
    soup = BeautifulSoup(page_source, 'html.parser')  # Parse the page source with BeautifulSoup

    # Find the table or section containing the influencer data
    table = soup.find('table')  # Modify this if necessary to target the correct table
    rows = table.find_all('tr') if table else []  # Get all rows in the table

    influencer_list = []  # Create a list to store all influencer data

    for row in rows[1:]:  # Skip the header row
        cols = row.find_all('td')  # Get all columns in the current row
        if len(cols) >= 4:  # Column Check: Ensure there are enough columns for the expected data
            influencer_data = {
                'header1': cols[0].get_text(strip=True),  # Extract data for header1
                'header2': cols[1].get_text(strip=True),  # Extract data for header2
                'header3': cols[2].get_text(strip=True),  # Extract data for header3
                'header4': cols[3].get_text(strip=True),  # Extract data for header4
            }
            influencer_list.append(influencer_data)  # Add the extracted data to the list

    # Create a DataFrame from the list of influencer data
    df = pd.DataFrame(influencer_list)

    # Generate a unique filename with a timestamp to avoid overwriting
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # Create a timestamp string
    filename = f'influencers_{timestamp}.csv'  # Generate a new filename

    # Save the DataFrame to a CSV file
    df.to_csv(filename, index=False)  # Save to CSV without the index

    print(f"CSV file saved successfully as {filename}.")  # Confirmation message

except Exception as e:
    print("An error occurred:", e)  # Print any error that occurs

finally:
    driver.quit()  # Ensure the WebDriver is closed
