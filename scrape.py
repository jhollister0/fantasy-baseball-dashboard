from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time
opts = Options()
browser = Firefox(options=opts)
browser.get('https://fantasy.espn.com/baseball/league/standings?leagueId=132005')
time.sleep(5)
frms = browser.find_elements_by_xpath('(//iframe)')
#browser.switch_to_frame(frms[2])
browser.switch_to.frame(frms[2])
browser.find_element_by_xpath("(//input)[1]").send_keys("jhollister@outlook.com")
browser.find_element_by_xpath("(//input)[2]").send_keys("Osubbfan21!")
browser.find_element_by_xpath("(//button)").click()
browser.switch_to.default_content()
time.sleep(10)
page_source = browser.page_source
df_list = pd.read_html(page_source)
standings = [df_list[1], df_list[2]]
result = pd.concat(standings, axis=1)
result = result.set_axis(['rank', 'team', 'runs', 'tb', 'rbi', 'bb_hit', 'k_hit', 'sac', 'sb', 'ip', 'h', 'er', 'bb_pitch', 'k_pitch', 'nh', 'pg', 'w', 'l', 'sv', 'bs', 'hd'], axis=1)
result.to_csv("/Users/jameshollister/Documents/Python/FantasyResults.csv", index = False)
browser.close()


#frms = browser.find_elements_by_xpath('(//iframe)')
##browser.switch_to_frame(frms[2])
#browser.switch_to.frame(frms[2])
#browser.find_element_by_xpath("(//input)[1]").send_keys("jhollister@outlook.com")
#browser.find_element_by_xpath("(//input)[2]").send_keys("Osubbfan21!")
#browser.find_element_by_xpath("(//button").click()
