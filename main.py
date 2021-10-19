from scraping_odds import scrape_eurobet
import time

username = "USERNAME"
password = "PASSWORD"
pageManager = scrape_eurobet(username,password)

start = time.time()

t = time.localtime()

pageManager.scrape_tennis_today_tomorrow()

end = time.time()
print(end - start)