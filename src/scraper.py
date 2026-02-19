import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

from src.image_utils import download_image


BASE_URL = "https://elpais.com"
OPINION_URL = "https://elpais.com/opinion/"


def setup_driver():

    options = webdriver.ChromeOptions()

    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    return driver


def handle_cookie_popup(driver):

    try:

        wait = WebDriverWait(driver, 8)

        buttons = wait.until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "button"))
        )

        for button in buttons:

            text = button.text.lower()

            if "accept" in text or "agree" in text or "aceptar" in text:
                button.click()
                print("✓ Cookie popup handled")
                time.sleep(2)
                return

    except:
        print("No cookie popup found")


def scrape_articles(driver):

    wait = WebDriverWait(driver, 15)

    articles_data = []

    print("Opening El Pais homepage...")
    driver.get(BASE_URL)

    handle_cookie_popup(driver)

    print("Opening Opinion section...")
    driver.get(OPINION_URL)

    wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article h2 a"))
    )

    article_elements = driver.find_elements(By.CSS_SELECTOR, "article h2 a")

    links = []

    for element in article_elements:

        link = element.get_attribute("href")

        if link and link not in links:
            links.append(link)

        if len(links) == 5:
            break

    print(f"✓ Found {len(links)} articles")

    for index, link in enumerate(links, start=1):

        print(f"\nScraping article {index}")

        driver.get(link)

        time.sleep(2)

        # TITLE
        try:
            title = driver.find_element(By.TAG_NAME, "h1").text.strip()
        except:
            title = ""

        # CONTENT
        content = ""

        try:

            paragraphs = driver.find_elements(
                By.CSS_SELECTOR,
                "div[data-dtm-region='articulo_cuerpo'] p"
            )

            if not paragraphs:

                paragraphs = driver.find_elements(
                    By.CSS_SELECTOR,
                    "article p"
                )

            content_list = []

            for p in paragraphs:

                text = p.text.strip()

                if text:
                    content_list.append(text)

            content = "\n\n".join(content_list)

        except:
            content = ""

        # IMAGE
        image_path = ""

        try:

            image = driver.find_element(By.CSS_SELECTOR, "figure img")

            image_url = image.get_attribute("src")

            image_path = download_image(image_url, index)

        except:

            print("No image found")

        article_data = {

            "title": title,
            "content": content,
            "image_path": image_path
        }

        articles_data.append(article_data)

        print("✓ Title:", title)

    return articles_data