from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def extract_data_from_page(url, selector):
    driver = webdriver.Chrome()
    try:
        driver.get(url)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        sections = driver.find_elements(By.CSS_SELECTOR, selector)
        articles_data = []

        for section in sections:
            section_title = section.find_element(By.CSS_SELECTOR, 'h2.detail-section__title').text
            articles = section.find_elements(By.CSS_SELECTOR, 'ul.detail-section__list > li.detail-section__file')

            for article in articles:
                article_title_element = article.find_element(By.CSS_SELECTOR, 'a.file__article-link')
                article_pdf_element = article.find_element(By.CSS_SELECTOR, 'a.file__pdf-link')

                article_title = article_title_element.text
                article_pdf_link = article_pdf_element.get_attribute('href')
                article_link = article_title_element.get_attribute('href')

                articles_data.append({
                    "section_title": section_title,
                    "article_title": article_title,
                    "article_pdf_link": article_pdf_link,
                    "article_link": article_link
                })

        return articles_data
    finally:
        driver.quit()


def compare_data(old_data, new_data):
    if len(old_data) != len(new_data):
        return False

    for old_item, new_item in zip(old_data, new_data):
        if old_item == new_item:
            return True

    return False
