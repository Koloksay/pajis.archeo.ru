from selenium import webdriver
import Data
import Method


selector = 'div.issue-page__details > section'
driver = webdriver.Chrome()

# Обрабатываем каждую пару старого и нового URL-адресов
for pair in Data.data:
    old_url, new_url = pair.values()

    # Открываем старую страницу, собираем данные
    old_data = Method.extract_data_from_page(driver, old_url, selector)
    new_data = Method.extract_data_from_page(driver, new_url, selector)
    print(f"\nСравниваем {old_url} и {new_url}")
    Method.compare_data(old_data, new_data)

driver.quit()
