import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


def setup_driver():
    """
    Sets up the Selenium WebDriver with Chrome options.
    Returns:
        driver (webdriver.Chrome): Configured Selenium WebDriver instance.
    """
    chrome_options = Options()
    # Uncomment the following line to run in headless mode
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument('--lang=en')
    driver = webdriver.Chrome(options=chrome_options)
    return driver


def extract_country_data(driver, url):
    """
    Extracts country data (name, link, monetary unit) from the main page.

    Args:
        driver (webdriver.Chrome): Selenium WebDriver instance.
        url (str): URL of the webpage to scrape.

    Returns:
        list: List of dictionaries containing country data.
    """
    driver.get(url)
    sleep(1)  # Wait for the page to load

    # Locate the table containing the country data
    table = driver.find_element(By.CLASS_NAME, "statistics")
    rows = table.find_elements(By.TAG_NAME, "tr")[:10]

    country_data = []
    for row in rows:
        try:
            link_element = row.find_element(By.TAG_NAME, "a")
            country_name = link_element.text.strip()
            country_link = link_element.get_attribute("href")

            monetary_unit = row.find_element(By.TAG_NAME, "td").text.strip()

            country_data.append({
                "Country": country_name,
                "Link": country_link,
                "Monetary Unit": monetary_unit
            })
        except Exception as e:
            print(f"Error processing row: {e}")
    
    return country_data


def extract_exchange_rates(driver, country_data):
    """
    Extracts exchange rates for each country from their respective pages.

    Args:
        driver (webdriver.Chrome): Selenium WebDriver instance.
        country_data (list): List of dictionaries with country data.

    Returns:
        list: List of dictionaries containing exchange rate data.
    """
    all_data = []
    for data in country_data:
        try:
            driver.get(data['Link'])
            sleep(2)  # Wait for the page to load

            table_xpath = '/html/body/table'  # XPath of the table on the linked page
            table = driver.find_element(By.XPATH, table_xpath)

            rows = table.find_elements(By.TAG_NAME, "tr")[:10]
            for row in rows:
                try:
                    date_cell = row.find_element(By.TAG_NAME, "th")
                    date = date_cell.text.strip()

                    rate_cell = row.find_element(By.TAG_NAME, "td")
                    rate = rate_cell.text.strip()

                    all_data.append({
                        "Country": data['Country'],
                        "Monetary Unit": data['Monetary Unit'],
                        "Date": date,
                        "Rate": rate
                    })
                except Exception as e:
                    print(f"Error extracting row data: {e}")

        except Exception as e:
            print(f"Error navigating to {data['Country']}: {e}")
    
    return all_data


def save_to_csv(data, filepath):
    """
    Saves the extracted data to a CSV file.

    Args:
        data (list): List of dictionaries containing the data to save.
        filepath (str): Path to save the CSV file.
    """
    df = pd.DataFrame(data)
    df.to_csv(filepath, index=False)
    print(f"\nData saved to {filepath}")


def main():
    """
    Main function to run the scraping process.
    """
    url = "https://www.federalreserve.gov/releases/h10/hist/default1999.htm"
    output_file = './datos/test.csv'

    # Step 1: Set up the Selenium WebDriver
    driver = setup_driver()

    try:
        # Step 2: Extract country data
        print("Extracting country data...")
        country_data = extract_country_data(driver, url)
        print(f"Extracted {len(country_data)} countries.")

        # Step 3: Extract exchange rates
        print("Extracting exchange rates...")
        all_data = extract_exchange_rates(driver, country_data)
        print(f"Extracted exchange rates for {len(all_data)} entries.")

        # Step 4: Save data to CSV
        save_to_csv(all_data, output_file)
    finally:
        # Step 5: Clean up and close the browser
        driver.quit()
        print("WebDriver closed.")


if __name__ == "__main__":
    main()
