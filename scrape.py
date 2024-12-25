from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time

# Step 1: Set up Selenium and read URLs
driver = webdriver.Chrome()  # Initialize WebDriver (use the appropriate driver for your browser)
urls = open('urls.txt').readlines()  # Read URLs from a text file, one per line

all_vessel_data = []  # List to store extracted data for all vessels

# Track the start time of the entire process for performance measurement
start_time = time.time()

# Process each URL
for index, url in enumerate(urls):
    url = url.strip()  # Remove leading/trailing whitespace and newlines from the URL
    driver.get(url)  # Navigate to the URL using Selenium
    
    # Start the timer for this URL
    url_start_time = time.time()

    # Step 2: Click the button to reveal additional information (tables)
    try:
        # Wait for the button to be clickable and then click it
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-default w_vessel_insurance']"))
        )
        button.click()  # Simulate a click on the button

        # Wait until the "Searching..." message disappears
        WebDriverWait(driver, 60).until(
            EC.invisibility_of_element((By.XPATH, "//*[text()='Searching...']"))
        )
    except Exception as e:
        continue  # Skip this URL if an error occurs and move to the next

    # Step 3: Extract the HTML content of the page after interaction
    html_content = driver.page_source

    # Step 4: Parse the HTML content to extract tables using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")
    tables = soup.find_all("table", class_="table ship-info")  # Find all relevant tables

    # Filter tables to exclude those with "display: none" in their style attribute
    filtered_tables = [
        table for table in tables
        if 'display: none' not in (table.get('style') or '').lower()
    ]

    # Consolidate data for this vessel
    vessel_data = {}
    for table in filtered_tables:
        # Extract table headers
        headers = [th.get_text(strip=True) for th in table.find_all("th")]

        # Extract table rows
        cells = table.find_all("td")
        if cells:
            for header, cell in zip(headers, cells):
                # Check if a cell contains a hyperlink (<a>) and extract the link if present
                link = cell.find('a', href=True)
                if link:
                    if "vessel" in link['href']:
                        vessel_data[header] = f"https://www.balticshipping.com{link['href']}"
                    else:
                        vessel_data[header] = link['href']
                else:
                    vessel_data[header] = cell.get_text(strip=True)

    # Append the consolidated vessel data to the list
    all_vessel_data.append(vessel_data)

    # Calculate the time elapsed for processing this URL
    url_elapsed_time = time.time() - url_start_time

    # Estimate the remaining time for all URLs
    url_eta = (len(urls) - (index + 1)) * url_elapsed_time
    eta_minutes = int(url_eta // 60)
    eta_seconds = int(url_eta % 60)
    print(f"Processed {index + 1}/{len(urls)} URLs. ETA: {eta_minutes}m {eta_seconds}s")

# Quit the Selenium WebDriver after processing all URLs
driver.quit()

# Step 5: Create a DataFrame from the consolidated vessel data
if all_vessel_data:
    final_df = pd.DataFrame(all_vessel_data)  # Convert the list of dictionaries to a DataFrame

    # Step 6: Save the DataFrame to an Excel file
    final_df.to_excel("output.xlsx", index=False)  # Save the DataFrame without the index

    # Calculate and display the total time taken for the entire process
    total_time = time.time() - start_time
    total_minutes = int(total_time // 60)
    total_seconds = int(total_time % 60)
    print(f"All URLs processed. Total time: {total_minutes}m {total_seconds}s")
else:
    print("No data extracted.")
