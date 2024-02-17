from selenium import webdriver
import data
import method


selector = 'div.issue-page__details > section'
driver = webdriver.Chrome()

# Обрабатываем каждую пару старого и нового URL-адресов
for pair in data.data:
    old_url, new_url = pair.values()

    # Открываем старую страницу, собираем данные
    old_data = method.extract_data_from_page(driver, old_url, selector)
    new_data = method.extract_data_from_page(driver, new_url, selector)
    print(f"\nСравниваем {old_url} и {new_url}")
    method.compare_data(old_data, new_data)

driver.quit()
