# Scrape_Odds_EuroBet_Ita
Scraper for Odds broker: Eurobet, built using Python and Selenium, setted for Firefox.
Scraper return the most important data of a match for betting
<br>
<br>
Selenium exploit DOM of web page, so if the website will change in the future, scaper cuold not will work properly.
<br>
<br>
Each function return a pandas dataframe

_**scrape_all_football_events()**_
return: 'Date', 'Bookmaker', 'League','Time', 'Team_1','Team_2','Odd_1','Odd_X','Odd_2' of the odds for major leagues.


_**scrape_football_today_tomorrow()**_
return: 'Date', 'Bookmaker', 'League','Time', 'Team_1','Team_2','Odd_1','Odd_X','Odd_2' of the odds for the today and tommorow football matches.


_**scrape_Tennis_today_tomorrow()**_
return: 'Date', 'Bookmaker', 'League','Time', 'Team_1','Team_2','Odd_1','Odd_X','Odd_2' of the odds for the today and tommorow tennis matches.
