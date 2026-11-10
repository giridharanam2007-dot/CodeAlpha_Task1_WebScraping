
import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pathlib import Path

BASE_URL = "https://books.toscrape.com/"
OUTPUT_FILE = Path("dataset/books_data.csv")

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

# Convert rating words into numbers
RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}


def scrape_books():
    books = []
    next_page = BASE_URL
    page_number = 1

    print("Starting Web Scraping...")
    print("-" * 45)

    while next_page:
        response = requests.get(
            next_page,
            headers=HEADERS,
            timeout=20
        )
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        articles = soup.select("article.product_pod")

        for book in articles:
            title = book.h3.a["title"]

            price = book.select_one(".price_color").get_text(
                strip=True
            )

            availability = book.select_one(
                ".availability"
            ).get_text(strip=True)

            rating_class = book.p.get("class", [])
            rating = next(
                (word for word in rating_class
                 if word in RATING_MAP),
                "Not Rated"
            )

            product_link = urljoin(
                next_page,
                book.h3.a["href"]
            )

            books.append({
                "Title": title,
                "Price": price,
                "Availability": availability,
                "Rating": RATING_MAP.get(rating, "Not Rated"),
                "Product_URL": product_link
            })

        print(
            f"Page {page_number}: "
            f"{len(articles)} books collected"
        )

        next_button = soup.select_one("li.next a")

        if next_button:
            next_page = urljoin(
                next_page,
                next_button["href"]
            )
        else:
            next_page = None

        page_number += 1

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df = pd.DataFrame(books)
    df.to_csv(OUTPUT_FILE, index=False)

    print("-" * 45)
    print("WEB SCRAPING COMPLETED!")
    print(f"Total books collected: {len(books)}")
    print(f"Dataset saved to: {OUTPUT_FILE}")

    print("\nSample Records:")
    print(df.head())


if __name__ == "__main__":
    scrape_books()
