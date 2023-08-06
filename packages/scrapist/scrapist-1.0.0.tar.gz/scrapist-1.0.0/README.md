# Scrapist: The Next Level of Efficient Web Scraping
Scrapist is a web scraper designed for Python. This web scraper uses requests and BeautifulSoup and also provides support for Scrapy style CSS selectors. Its features are:
* Faster than requests and BeautifulSoup.
* Is effective in fetching multiple pages compared to Scrapy.
* Provides support for both BeautifulSoup-style selection and Scrapy-style CSS selection.

# Installation
To install Scrapist, run this command in the terminal:
```
    pip install scrapist
```

# Initialization
To start web scraping with Scrapist, use this code:
```python
    from scrapist import Scraper

    scraper = Scraper()
    data = scraper.scrape("<your url here>")
    print(data.soup)
```

# Getting Specified Parts/Tags of a web page
To get specified parts/tags of a web page, you can choose either of the two ways:

## The Scrapy-style
To get specified data Scrapy-style, use this code after the initialization:
```python
    first = data.css("<your css selector here>").get()
    print(first)
    # Or
    all_data = data.css("<your css selector here>").getall()
    print(all_data)
```

## The BeautifulSoup-style
To get specified data BeautifulSoup-style, use this code after the initialization:
```python
    first = data.find("<your tag here>", "[your attributes here]")
    print(first)
    # Or
    all_data = data.find_all("<your tag here>", "[your attributes here]")
    print(all_data)
```

# Creating a Soup Strainer
To create a soup strainer, use this code just after the line of creating a scraper (The `scraper = Scraper()` intialization line):
```python
    strainer = scraper.strainer("<your tag here>", "[your attribute here]")
```
And use the strainer in the `strainer` parameter in `scraper.scrape()` function.