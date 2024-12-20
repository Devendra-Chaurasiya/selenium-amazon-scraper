# Amazon Best Sellers Scraper

This project is a Python-based web scraper that automates the process of extracting product details from Amazon's Best Sellers section using Selenium. The script can scrape data from multiple categories, filter products with discounts greater than 50%, and save the results in a structured CSV file.

---

## Features

- **Authentication**: Logs in to Amazon using user-provided credentials.
- **Data Extraction**:
  - Scrapes details for products in 10 categories.
  - Filters products with discounts greater than 50%.
  - Handles pagination to extract up to 1500 best-selling products per category.
- **Output**:
  - Saves scraped data in a CSV file for easy access and analysis.
- **Error Handling**:
  - Manages missing elements, timeouts, and empty datasets gracefully.

---

## Technologies Used

- **Python**: Programming language.
- **Selenium**: For web automation and scraping.
- **CSV**: For storing the extracted data.

---

## Prerequisites

1. **Python 3.8+** installed on your system.
2. **Google Chrome** browser.
3. **ChromeDriver**: Ensure the version matches your Chrome browser.
   - Download ChromeDriver: [https://sites.google.com/chromium.org/driver/](https://sites.google.com/chromium.org/driver/).
4. Install required Python libraries:
   ```bash
   pip install selenium
   ```

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/amazon-best-sellers-scraper.git
   cd amazon-best-sellers-scraper
   ```

2. **Set Up ChromeDriver**:
   - Download and extract ChromeDriver.
   - Update the path to `chromedriver.exe` in the script:
     ```python
     driver = webdriver.Chrome(service=Service("C:\\path\\to\\chromedriver.exe"))
     ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. **Run the Script**:
   ```bash
   python amazon_scraper.py
   ```

2. **Enter Amazon Credentials**:
   - You will be prompted to enter your Amazon username and password.

3. **Scraper Execution**:
   - The script will log in to Amazon and scrape product data from the specified categories.
   - Data is saved in `output.csv` in the same directory as the script.

---

## Folder Structure

```plaintext
amazon-best-sellers-scraper/
├── README.md          # Project documentation
├── requirements.txt   # List of dependencies
├── amazon_scraper.py  # Main Python script
├── output/            # Folder for storing scraped data
│   └── output.csv     # Example output file
```

---

## Output

- **File**: `output.csv`
- **Columns**:
  - Product Name
  - Product Price
  - Sale Discount
  - Category Name
  - Additional product details as per scraping requirements.

---

## Example Output

| Name                      | Price   | Discount | Category   |
|---------------------------|---------|----------|------------|
| Product 1                 | ₹499 | 55%      | Electronics|
| Product 2                 | ₹999 | 60%      | Kitchen    |

---

## Known Issues

1. **Empty Output**:
   - If no products match the filter criteria (e.g., discounts > 50%), the script may produce an empty output.
   - Ensure the specified categories have sufficient products meeting the criteria.

2. **Two-Factor Authentication (2FA)**:
   - The script does not handle 2FA. If enabled on your Amazon account, you must manually complete the login process.

3. **CAPTCHA Challenges**:
   - If Amazon presents a CAPTCHA, the script cannot bypass it and will require manual intervention.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributions

Contributions are welcome! Please fork the repository and create a pull request for review.

---

## Contact

For questions or support, please contact:
- **Name**: Devendra Mahesh Chaurasiya
- **Email**: devendrachaurasiya2004@gmail.com
- **GitHub**: [Devendra-Chaurasiya](https://github.com/Devendra-Chaurasiya)

