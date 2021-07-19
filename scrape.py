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
result.to_csv("FantasyResults.csv", index = False)


#Now, get all of the team rosters, and create seperate .csv files.

for i in range(len(result['team'])):
    url = "https://fantasy.espn.com/baseball/team?leagueId=132005&teamId=" + str(i+1)
    browser.get(url)
    time.sleep(7)
    page_source = browser.page_source
    soup = BeautifulSoup(page_source, "html.parser")
    elements = soup.find("span", class_="teamName truncate")
    team_name = elements.text.strip()
    team_name = team_name.replace(" ", "")
    file_name = team_name + ".csv"
    df_list = pd.read_html(page_source)

    rosters = [df_list[0], df_list[3]]
    result = pd.concat(rosters, axis = 0)
    result.to_csv(file_name, index=False)
    df = pd.read_csv(file_name)

    batter_names = df[['Batters', 'Batters.1']]
    pitcher_names = df[['Pitchers', 'Pitchers.1']]
    pitcher_names = pitcher_names.set_axis(['Batters', 'Batters.1'], axis=1)
    pitcher_names = pitcher_names.dropna()
    batter_names = batter_names.dropna()
    pitcher_names = pitcher_names.drop([0])
    batter_names = batter_names.drop([0])

    all_names = pd.concat([batter_names, pitcher_names])
    all_names = all_names.set_axis(['Name', 'Slot'], axis=1)
    all_names.to_csv(file_name, index=False)


browser.close()
