from selenium import webdriver
import Data
import Method

driver = webdriver.Chrome()

selector = 'div.issue-page__details > section'

# Сравниваем ссылки на страницах для каждой пары новой и старой страницы
for pair in Data.data:
    old_url, new_url = pair.values()
    Method.compare_pages(driver, old_url, new_url, selector)

# Закрываем браузер после завершения работы
driver.quit()
