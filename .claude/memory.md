# Laptop Scraping - Amazon laptop ma'lumotlari

## Maqsad
Selenium yordamida Amazon.in dan laptop ma'lumotlarini scraping qilish va tahlil qilish.

## Tech Stack
- **Language:** Python
- **Scraping:** Selenium WebDriver, ChromeDriver (webdriver_manager)
- **Data:** pandas, numpy
- **Visualization:** matplotlib, seaborn
- **Environment:** Jupyter Notebook

## Arxitektura
```
laptop_amazon.py      — Scraping skripti
laptop_amazon.ipynb   — Jupyter tahlil notebook
laptops_amazon.csv    — Scraped data
README.md             — O'rnatish qo'llanmasi
```

## Muhim logika
- Amazon.in laptop qidirish (4 sahifa)
- 11 ta parametr: brand, model, RAM, storage, CPU, OS, price, rating, reviews, GPU, screen size
- Dynamic XPath selectors
- Exception handling: missing data = "No [parameter]"
- CSV export + Jupyter vizualizatsiya
