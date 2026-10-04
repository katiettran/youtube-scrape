from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import csv

options = Options()
driver = webdriver.Chrome(options=options)

url = "https://www.youtube.com/results?search_query=python+tutorial"
driver.get(url)

time.sleep(5)

videos = driver.find_elements(By.XPATH, "//a[@id='video-title']")

results = []
# helper function to extract video details (title and link)
# loop through each video element and extract the title and link
for v in videos:
    title = v.text.strip()
    link = v.get_attribute("href")

    if title and link:
        results.append((title, link))

print("\nTop results:\n")

for title, link in results[:10]:
    print(title)
    print(link)
    print("---")

with open("youtube_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Link"])
    writer.writerows(results[:10])

driver.quit()