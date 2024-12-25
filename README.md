### README

# Vessel Data Scraping Tool

This project provides a complete workflow for extracting and scraping detailed information about vessels from Baltic Shipping's website. It consists of two Python scripts:

1. **`extract.py`**: Extracts all vessel URLs from the site's XML sitemaps and consolidates them into a text file.
2. **`scraper.py`**: Scrapes the detailed data from the extracted URLs and exports the results to an Excel file.

---

## Features

- **Automated Sitemap Parsing**: `extract.py` processes multiple XML sitemaps to fetch vessel URLs.
- **Web Interaction**: `scraper.py` uses Selenium to interact with webpages and load hidden content dynamically.
- **Data Consolidation**: Extracted data is saved in a structured Excel file for easy analysis.
- **Error Handling**: Skips invalid URLs and handles timeouts or missing elements gracefully.

---

## Requirements

### Prerequisites

- **Python 3.7+**
- **Google Chrome** (or another supported browser)
- **ChromeDriver** (or the corresponding WebDriver for your browser)

### Installation

1. Clone this repository or download the scripts.

2. Install the required Python libraries using pip:
   
   ```bash
   pip install -r requirements.txt  
   ```

---

## Workflow

### Step 1: Extract URLs

Run the `extract.py` script to fetch vessel URLs from the Baltic Shipping sitemaps.

1. Ensure `extract.py` is in the working directory.

2. Run the script:
   
   ```bash
   python extract.py  
   ```

3. Output:
   
   - A file named `urls.txt` containing all the extracted vessel URLs, one per line.

### Step 2: Scrape Vessel Data

Run the `scraper.py` script to scrape detailed information for each vessel URL in `urls.txt`.

1. Ensure `scraper.py` and `urls.txt` are in the same directory.

2. Run the script:
   
   ```bash
   python scraper.py  
   ```

3. Output:
   
   - An Excel file named `output.xlsx` containing the scraped vessel data.

---

## Outputs

### `urls.txt`

- A plain text file containing one vessel URL per line.

### `output.xlsx`

- An Excel spreadsheet with detailed vessel information. Each row corresponds to a vessel, and columns represent attributes or details.

---

## Notes

- **Timeouts and Failures**:
  
  - The scripts handle missing elements and timeouts, skipping problematic entries while continuing the process.

- **Performance**:
  
  - For large datasets, processing times may vary based on the number of URLs and the website's response speed.

- **Customizability**:
  
  - Adjust `scraper.py` for specific webpage structures or additional data points.

---

## Troubleshooting

- **Driver Errors**:
  
  - Ensure the ChromeDriver version matches your installed version of Google Chrome. Update or replace the driver if necessary.

- **Missing Data**:
  
  - Check that the webpage's structure (e.g., button classes, table classes) has not changed.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for details.
