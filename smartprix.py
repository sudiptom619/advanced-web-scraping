import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# for explicit waits
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://smartprix.com/")

element = driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div/a[4]")

element.click()
time.sleep(1)

driver.find_element(By.XPATH, "/html/body/div/main/aside/div/div[5]/div[2]/label[1]/input").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div/main/aside/div/div[5]/div[2]/label[2]/input").click()

# explicit await
try:
    target = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME,"sm-product"))
    )
except:
    print("No more products waiting ")
    driver.quit()

#run js in selenium with execute script
old_height = driver.execute_script('return document.body.scrollHeight')
while True:

    driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
    time.sleep(5)

    new_height = driver.execute_script('return document.body.scrollHeight')

    print(old_height)
    print(new_height)

    if new_height == old_height:
        break

    old_height = new_height

html = driver.page_source

with open("smartprix.html", "w", encoding='utf-8') as f:
    f.write(html)



