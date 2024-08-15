from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
# Not wrong just non specific
article_count = driver.find_element(By.ID, value="articlecount")
print(article_count.text)
# specific honed in on anchor tag using CSS selectors
# article_count_honed = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# article_count_honed.click()

# Find element by Link text
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# Click the search button to open the bar
search_button = driver.find_element(By.CSS_SELECTOR, value="#p-search a")
search_button.click()
# Find the "Search" <input> by Name
search = driver.find_element(By.NAME, value="search")

# Send key input
search.send_keys("Python", Keys.ENTER)

# driver.quit()













