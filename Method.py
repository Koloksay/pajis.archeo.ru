from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def extract_data_from_page(driver, selector):
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

def compare_data(old_data, new_data):
    assert len(old_data) == len(new_data), "Количество записей на старой и новой страницах различается."

    for i, (old_item, new_item) in enumerate(zip(old_data, new_data), start=1):
        if old_item == new_item:
            print(f"Строка {i}: Старая и новая записи совпадают: {old_item}")
        else:
            print(f"Строка {i}: Старая и новая записи не совпадают: Старая - {old_item}, Новая - {new_item}")

def compare_pages(driver, old_url, new_url, selector):
    try:
        driver.get(old_url)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        old_data = extract_data_from_page(driver, selector)
    except Exception as e:
        print(f"Ошибка при извлечении данных со старой страницы: {e}")

    try:
        driver.get(new_url)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        new_data = extract_data_from_page(driver, selector)
    except Exception as e:
        print(f"Ошибка при извлечении данных с новой страницы: {e}")

    compare_data(old_data, new_data)