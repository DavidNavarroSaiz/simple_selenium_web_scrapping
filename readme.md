
# Exchange Rate Scraper

This project is a web scraper built using Python and Selenium. It extracts historical exchange rate data for various countries from the Federal Reserve website and saves the results into a CSV file.

## Features

- Scrapes country names, links, and monetary units from the Federal Reserve webpage.
- Navigates to each country's data page to extract exchange rates and dates.
- Saves the extracted data into a structured CSV file.
- Modular and reusable code design.

---

## Project Structure

```
.
├── scrape_exchange_rates.py  # Main script
```

---

## Requirements

To run this project, you need the following:

### Python Libraries:
- `selenium`
- `pandas`

Install the required libraries using pip:
```bash
pip install selenium pandas
```

### WebDriver:
- Ensure you have the **Chrome WebDriver** installed and added to your system's PATH. You can download it from [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads).

---

## How to Run

1. Clone this repository or download the `scrape_exchange_rates.py` file.
2. Ensure the required libraries and Chrome WebDriver are installed.
3. Run the script:
   ```bash
   python scrape_exchange_rates.py
   ```
4. The results will be saved in the `datos/test.csv` file.

---

## Script Workflow

1. **Set Up WebDriver**:
   - Configures Chrome WebDriver with options like `headless` mode and English language.

2. **Extract Country Data**:
   - Scrapes the main webpage to extract:
     - Country names.
     - Links to detailed exchange rate data pages.
     - Monetary units.

3. **Extract Exchange Rates**:
   - Navigates to each country-specific page.
   - Extracts date and exchange rate information from the first 10 rows of the data table.

4. **Save Data to CSV**:
   - Combines the extracted data into a structured DataFrame.
   - Saves the final data to a CSV file in the `datos/` directory.

5. **Clean Up**:
   - Closes the WebDriver instance to free resources.

---

## Key Functions

### `setup_driver()`
Sets up the Selenium WebDriver with Chrome options.
- **Returns:** Configured WebDriver instance.

### `extract_country_data(driver, url)`
Extracts country names, links, and monetary units from the main page.
- **Args:**
  - `driver` (webdriver.Chrome): Selenium WebDriver instance.
  - `url` (str): URL of the Federal Reserve webpage.
- **Returns:** List of dictionaries containing country data.

### `extract_exchange_rates(driver, country_data)`
Extracts exchange rates and dates from country-specific pages.
- **Args:**
  - `driver` (webdriver.Chrome): Selenium WebDriver instance.
  - `country_data` (list): List of dictionaries with country data.
- **Returns:** List of dictionaries containing exchange rate data.

### `save_to_csv(data, filepath)`
Saves the extracted data to a CSV file.
- **Args:**
  - `data` (list): List of dictionaries containing data to save.
  - `filepath` (str): Filepath to save the CSV.

### `main()`
Orchestrates the entire scraping process:
1. Sets up the WebDriver.
2. Extracts country data.
3. Extracts exchange rate data.
4. Saves data to a CSV file.
5. Cleans up the WebDriver.

---

## Example Output

### CSV File Structure:
| Country   | Monetary Unit   | Date       | Rate  |
|-----------|-----------------|------------|-------|
| USA       | Dollar          | 01/01/1999 | 1.000 |
| Canada    | Canadian Dollar | 01/01/1999 | 1.462 |
| Mexico    | Peso            | 01/01/1999 | 9.834 |

The CSV file will be saved as `datos/test.csv`.

---

## Potential Improvements

- **Error Handling**:
  Add more robust error handling for unexpected webpage structures or missing elements.
- **Dynamic Table Parsing**:
  Enhance flexibility to adapt to changes in table structure.
- **Headless Mode**:
  Enable headless mode for faster, non-visual execution.

---

## Troubleshooting

- **Selenium WebDriver Not Found**:
  Ensure ChromeDriver is installed and its version matches your Chrome browser.
- **Data Missing in Output**:
  Check for structural changes on the Federal Reserve website.
- **Slow Performance**:
  Reduce `sleep` durations and optimize element lookups.

---

## References

- [Federal Reserve Website](https://www.federalreserve.gov/)
- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [pandas Documentation](https://pandas.pydata.org/docs/)
- [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads)
