from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


brand = []  #done
model_name = []  #done
scren_size = []  #done
RAM = []  #done
storage = []  #done
CPU = []  #done
operating_system = []  #done
price = []  #done
rating = []  #done
review_count = []  #done
graphic_card_description = []  #done


url = "https://www.amazon.in/s?k=laptops"
num_pages=4

for i in range(num_pages):
    driver.get(url)
    try:
        next_btn = driver.find_element(By.XPATH,"//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-button-accessibility s-pagination-separator']")
        next_url = next_btn.get_attribute("href")
    except:
        next_url = "No next page"
        break

    laptop_links = driver.find_elements(By.XPATH,"//a[@class='a-link-normal s-no-outline']")
    laptop_urls = []
    for link in laptop_links:
        laptop_urls.append(link.get_attribute("href"))


    for url in laptop_urls:
        driver.get(url)
        try:
            brand.append(driver.find_element(By.XPATH,"//tr[@class='a-spacing-small po-brand']"
                                                    "//td[@class='a-span9']"
                                                    "//span[@class='a-size-base po-break-word']").text)
        except:
            brand.append("No brand")
        try:
            model_name.append(driver.find_element(By.XPATH,"//tr[@class='a-spacing-small po-model_name']"
                                                        "//td[@class='a-span9']"
                                                        "//span[@class='a-size-base po-break-word']").text)
        except:
            model_name.append("No model name")

        try:
            scren_size.append(driver.find_element(By.XPATH,"//tr[@class='a-spacing-small po-display.size']"
                                                        "//td[@class='a-span9']"
                                                        "//span[@class='a-size-base po-break-word']").text)
        except:
            scren_size.append("No screen size")

        try:
            RAM.append(driver.find_element(By.XPATH,"//tr[@class='a-spacing-small po-ram_memory.installed_size']"
                                                        "//td[@class='a-span9']"
                                                        "//span[@class='a-size-base po-break-word']").text)
        except:
            RAM.append("No RAM")

        try:
            storage.append(driver.find_element(By.XPATH,"//tr[@class='a-spacing-small po-hard_disk.size']"
                                                        "//td[@class='a-span9']"
                                                        "//span[@class='a-size-base po-break-word']").text)
        except:
            storage.append("No storage")

        try:
            CPU.append(driver.find_element(By.XPATH,"//tr[@class='a-spacing-small po-cpu_model.family']"
                                                        "//td[@class='a-span9']"
                                                        "//span[@class='a-size-base po-break-word']").text)
        except:
            CPU.append("No CPU")

        try:
            operating_system.append(driver.find_element(By.XPATH,
                                        "//th[@class='a-color-secondary a-size-base prodDetSectionEntry'][contains(text(),'Operating System')]/../td").text)
        except Exception:
            operating_system.append("No operating system")

        try:
            price.append(driver.find_element(By.XPATH,"//span[@class='a-price aok-align-center reinventPricePriceToPayMargin priceToPay']"
                                                    "//span[@aria-hidden='true']"
                                                    "//span[@class='a-price-whole']").text)
        except:
            price.append("No price")

        try:
            graphic_card_description.append(driver.find_element(By.XPATH,"//th[@class='a-color-secondary a-size-base prodDetSectionEntry'][contains(text(),'Graphics Card Description')]/../td").text)

        except Exception:
            graphic_card_description.append("No graphic card description")

        try:
            rating.append(driver.find_element(By.XPATH,"//span[@id='acrPopover']"
                                                "//span[@class='a-declarative']"
                                                "//a[@class='a-popover-trigger a-declarative']"
                                                "//span[@class='a-size-base a-color-base']").text)
        except:
            rating.append("No rating")

        try:
            review_count.append(driver.find_element(By.XPATH,"//span[@id='acrCustomerReviewText' and contains(text(), 'ratings')]").text)
        except:
            review_count.append("No review count")

    url = next_url


df = pd.DataFrame(
    {
        'Brand': brand,
        'Model Name': model_name,
        'Screen Size': scren_size,
        'RAM': RAM,
        'Storage': storage,
        'CPU': CPU,
        'Operating System': operating_system,
        'Price': price,
        'Rating': rating,
        'Review Count': review_count,
        'Graphic Card Description': graphic_card_description
    }
)

df.to_csv("laptops_amazon1.csv")