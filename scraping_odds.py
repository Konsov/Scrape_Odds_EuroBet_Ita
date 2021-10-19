from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
from random import randint
import pprint

import pandas as pd

class scrape_eurobet:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        profile = webdriver.FirefoxProfile()
        
        self.driver = webdriver.Firefox(profile)


    def closeBrowser(self):
        self.driver.close()

    def openBrowser(self):
        driver = self.driver
        driver.get("https://www.eurobet.it/") #andare sulla homepage

    def scrape_all_football_events(self):
        driver = self.driver
        
        columns = ['Date', 'Bookmaker', 'League','Time', 'Team_1','Team_2','Odd_1','Odd_X','Odd_2']

        df = pd.DataFrame()

        bookmaker = "Eurbet"
        
        leagues_lits = ["https://www.eurobet.it/it/scommesse/#!/calcio/it-serie-a",
        "https://www.eurobet.it/it/scommesse/#!/calcio/it-serie-b1",
        "https://www.eurobet.it/it/scommesse/#!/calcio/serie-c",
        "https://www.eurobet.it/it/scommesse/#!/calcio/it-serie-d",
        "https://www.eurobet.it/it/scommesse/#!/calcio/wd-coppa-america",
        "https://www.eurobet.it/it/scommesse/#!/calcio/wd-qual-mondiali",
        "https://www.eurobet.it/it/scommesse/#!/calcio/wd-amichevoli-nazionali",
        "https://www.eurobet.it/it/scommesse/#!/calcio/wd-mondiali-calcio",
        "https://www.eurobet.it/it/scommesse/#!/calcio/wd-copa-libertadores",
        "https://www.eurobet.it/it/scommesse/#!/calcio/wd-copa-sudamericana",
        "https://www.eurobet.it/it/scommesse/#!/calcio/wd-afc-cup",
        "https://www.eurobet.it/it/scommesse/#!/calcio/eu-champions-league",
        "https://www.eurobet.it/it/scommesse/#!/calcio/eu-europa-league",
        "https://www.eurobet.it/it/scommesse/#!/calcio/uefa-nations-league",
        "https://www.eurobet.it/it/scommesse/#!/calcio/eu-u21-europei",
        "https://www.eurobet.it/it/scommesse/#!/calcio/ing-championship1",
        "https://www.eurobet.it/it/scommesse/#!/calcio/ing-league-one2",
        "https://www.eurobet.it/it/scommesse/#!/calcio/ing-league-two1",
        "https://www.eurobet.it/it/scommesse/#!/calcio/es-liga-adelante",
        "https://www.eurobet.it/it/scommesse/#!/calcio/es-tercera-division",
        "https://www.eurobet.it/it/scommesse/#!/calcio/es-coppa-spagna-f",
        "https://www.eurobet.it/it/scommesse/#!/calcio/de-bundesliga",
        "https://www.eurobet.it/it/scommesse/#!/calcio/de-2-bundesliga1",
        "https://www.eurobet.it/it/scommesse/#!/calcio/de-regionalliga",
        "https://www.eurobet.it/it/scommesse/#!/calcio/de-ii-bundesliga-f",
        "https://www.eurobet.it/it/scommesse/#!/calcio/fr-ligue-2",
        "https://www.eurobet.it/it/scommesse/#!/calcio/dz-ligue-1",
        "https://www.eurobet.it/it/scommesse/#!/calcio/dz-ligue-2",
        "https://www.eurobet.it/it/scommesse/#!/calcio/sa-saudi-professional-league",
        "https://www.eurobet.it/it/scommesse/#!/calcio/sa-saudi-first-division",
        "https://www.eurobet.it/it/scommesse/#!/calcio/au-a-league-60",
        "https://www.eurobet.it/it/scommesse/#!/calcio/at-bundesliga",
        "https://www.eurobet.it/it/scommesse/#!/calcio/bh-premier-league",
        "https://www.eurobet.it/it/scommesse/#!/calcio/by-vysshaya-liga-369",
        "https://www.eurobet.it/it/scommesse/#!/calcio/ba-coppa-bosnia-herzegovina",
        "https://www.eurobet.it/it/scommesse/#!/calcio/br-brasileiro-a",
        "https://www.eurobet.it/it/scommesse/#!/calcio/br-brasileiro-b",
        "https://www.eurobet.it/it/scommesse/#!/calcio/br-brasilero-d",
        "https://www.eurobet.it/it/scommesse/#!/calcio/br-alagoano",
        "https://www.eurobet.it/it/scommesse/#!/calcio/br-catarinense",
        "https://www.eurobet.it/it/scommesse/#!/calcio/br-brasilero-f",
        "https://www.eurobet.it/it/scommesse/#!/calcio/bg-a-pfg",
        "https://www.eurobet.it/it/scommesse/#!/calcio/cn-league-one",]

        for league in leagues_lits:
            driver.get(league)
           
            strUrl = driver.current_url

            if(strUrl == "https://www.eurobet.it/it/scommesse/#!/"):
                print("No " + league + " games currently available")
                return
                

            days = driver.find_elements_by_class_name('discipline-football')
            
            for day in days:

                event_day = day.find_element_by_tag_name('h2')

                event_row = day.find_elements_by_css_selector('div[style=""]')
        
                for row in event_row:

                    try:
                        league_row = row.find_element_by_class_name("breadcrumb-meeting")
                        league_span = league_row.find_elements_by_tag_name('span')
                        league_nation = league_span[0].text
                        league_name= league_span[1].text
                    except:
                        league_nation = league_nation
                        league_name= league_name

                    event_date = event_day.text

                    event_bookmaker = bookmaker

                    time_match = row.find_element_by_class_name("time-box ")
                    event_time = time_match.text
                    
                    if('\n' in event_time):
                        event_time = event_time.split('\n')[1] 

                    event_players = row.find_element_by_class_name("event-players")
                    players = event_players.find_elements_by_tag_name('span')
                    player_one = players[1].text
                    player_two = players[3].text
                    event_player_one = player_one
                    event_player_two = player_two

                    odds = row.find_elements_by_class_name("container-quota-new")
                    event_odd_1 = odds[0].text
                    event_odd_X = odds[1].text
                    event_odd_2 = odds[2].text

                    df_row = {'Date':event_date, 'Bookmaker':event_bookmaker, 'League': league_name, 'Time':event_time , 'Team_1':event_player_one, 'Team_2':event_player_two, 'Odd_1':event_odd_1,'Odd_X':event_odd_X,'Odd_2':event_odd_2}
                    df = df.append(df_row, ignore_index=True)
    
        pprint.pprint(df)
        return(df)

    def scrape_football_today_tomorrow(self):
        driver = self.driver
        
        columns = ['Date', 'Bookmaker', 'Nation','League','Time','Team_1','Team_2','Odd_1','Odd_X','Odd_2','Last_Update']

        df = pd.DataFrame()

        bookmaker = "Eurobet"
        
        driver.get("https://www.eurobet.it/it/scommesse/#!/calcio/?temporalFilter=TEMPORAL_FILTER_OGGI_DOMANI")
        
        
        time.sleep(0.2)
                                                                                
        height = driver.execute_script("return document.body.scrollHeight")
        
        scrol = 400
        while(scrol < height):
            height = driver.execute_script("return document.body.scrollHeight")
            driver.execute_script(f"window.scrollTo(0,{scrol})")
            time.sleep(0.1)
            scrol = scrol + 400
        
        strUrl = driver.current_url


        if(strUrl == "https://www.eurobet.it/it/scommesse/#!/"):
            print("No games currently available")
            return
        
        days = driver.find_elements_by_class_name('discipline-football')

        for day in days:

            event_day = day.find_element_by_tag_name('h2')

            event_row = day.find_elements_by_css_selector('div[style=""]')

            for row in event_row:

                try:
                    league_row = row.find_element_by_class_name("breadcrumb-meeting")
                    league_span = league_row.find_elements_by_tag_name('span')
                    league_nation = league_span[0].text
                    league_name= league_span[1].text
                except:
                    league_nation = league_nation
                    league_name= league_name

                event_date = event_day.text

                event_bookmaker = bookmaker

                time_match = row.find_element_by_class_name("time-box ")
                event_time = time_match.text
                
                if('\n' in event_time):
                    event_time = event_time.split('\n')[1] 

                event_players = row.find_element_by_class_name("event-players")
                players = event_players.find_elements_by_tag_name('span')
                player_one = players[1].text
                player_two = players[3].text
                event_player_one = player_one
                event_player_two = player_two

                odds = row.find_elements_by_class_name("container-quota-new")
                event_odd_1 = odds[0].text
                event_odd_X = odds[1].text
                event_odd_2 = odds[2].text

                t = time.localtime()
                current_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

                df_row = {'Date':event_date, 'Bookmaker':event_bookmaker, 'Nation': league_nation, 'League': league_name, 'Time':event_time , 'Team_1':event_player_one, 'Team_2':event_player_two, 'Odd_1':event_odd_1,'Odd_X':event_odd_X,'Odd_2':event_odd_2,'Last_Update': current_time }
                df = df.append(df_row, ignore_index=True)

        pprint.pprint(df)
        return(df)    

    def scrape_tennis_today_tomorrow(self):
        driver = self.driver
        
        columns = ['Date', 'Bookmaker', 'Category','League','Time','Team_1','Team_2','Odd_1','Odd_2','Last_Update']

        df = pd.DataFrame()

        bookmaker = "Eurobet"
        
        driver.get("https://www.eurobet.it/it/scommesse/#!/tennis/?temporalFilter=TEMPORAL_FILTER_OGGI_DOMANI")
        
        
        time.sleep(0.2)
                                                                                
        height = driver.execute_script("return document.body.scrollHeight")
        
        scrol = 400
        while(scrol < height):
            height = driver.execute_script("return document.body.scrollHeight")
            driver.execute_script(f"window.scrollTo(0,{scrol})")
            time.sleep(0.1)
            scrol = scrol + 400
        
        strUrl = driver.current_url


        if(strUrl == "https://www.eurobet.it/it/scommesse/#!/"):
            print("No games currently available")
            return
        
        days = driver.find_elements_by_class_name('discipline-tennis')

        for day in days:

            event_day = day.find_element_by_tag_name('h2')
            
            # event_row = day.find_elements_by_class_name('event-row')

            event_row = day.find_elements_by_css_selector('div[style=""]')

            for row in event_row:

                try:
                    league_row = row.find_element_by_class_name("breadcrumb-meeting")
                    league_span = league_row.find_elements_by_tag_name('span')
                    league_nation = league_span[0].text
                    league_name= league_span[1].text
                except:
                    league_nation = league_nation
                    league_name= league_name

                event_date = event_day.text

                event_bookmaker = bookmaker

                time_match = row.find_element_by_class_name("time-box ")
                event_time = time_match.text
                
                if('\n' in event_time):
                    event_time = event_time.split('\n')[1] 

                event_players = row.find_element_by_class_name("event-players")
                players = event_players.find_elements_by_tag_name('span')
                player_one = players[1].text
                player_two = players[3].text
                event_player_one = player_one
                event_player_two = player_two

                odds = row.find_elements_by_class_name("container-quota-new")
                event_odd_1 = odds[0].text
                event_odd_2 = odds[1].text

                t = time.localtime()
                current_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

                df_row = {'Date':event_date, 'Bookmaker':event_bookmaker, 'Category': league_nation, 'League': league_name, 'Time':event_time , 'Team_1':event_player_one, 'Team_2':event_player_two, 'Odd_1':event_odd_1,'Odd_2':event_odd_2,'Last_Update': current_time }
                df = df.append(df_row, ignore_index=True)

        pprint.pprint(df)
        return(df) 