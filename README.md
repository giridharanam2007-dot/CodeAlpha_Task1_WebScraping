# Task 1 – Web Scraping

**Internship:** CodeAlpha – Data Analytics Internship

## Project Overview
This project performs web scraping using Python to extract book information from [Books to Scrape](https://books.toscrape.com/).

The collected information is processed and stored in CSV format for further analysis.

## Features
- Extracts book titles and prices.
- Collects product ratings.
- Retrieves product URLs.
- Uses BeautifulSoup for HTML parsing.
- Stores scraped data in a CSV file.

## Technologies Used
- Python
- Requests
- BeautifulSoup
- Pandas

## Dataset
**Source:** [Books to Scrape](https://books.toscrape.com/)

**Output File:** `dataset/books_data.csv`

## Project Structure
```text
Task-1-Web-Scraping/
│
├── dataset/
│   └── books_data.csv
├── scraper.py
├── requirements.txt
└── README.md
```

## How to Run

1. Clone the repository.
2. Install the required libraries:

```bash
pip install -r requirements.txt
```

3. Execute the scraper:

```bash
python scraper.py
```

4. Find the generated CSV file inside the `dataset` folder.

## Output
The scraped book information is saved in CSV format for further use and analysis.

## Internship
CodeAlpha – Data Analytics Internship

**Task 1: Web Scraping**