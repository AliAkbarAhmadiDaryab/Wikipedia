import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt
import numpy as np
import re
import dict_correspondent as dc


url = 'https://en.wikipedia.org/wiki/List_of_terrorist_incidents_in_January%E2%80%93June_2014'
html = urllib.request.urlopen(url)
soup = bs(html, 'html.parser')
soup = soup('table')
# Retrieving the First Table
months = ['January', 'February', 'March', 'April','May']
# for i,table in enumerate(soup):

for i, table in enumerate(soup):
    if i > 0 and i <= 4:
        find_table = table
        # Extract tr (rows) from table
        find_table = find_table('tr')
        all_war_part = []  # Storing the Identity of Attacks
        all_war_location = []  # Place of the Attack
        # Since Part and Location has links in table we can extract the wanted data base on tag <a>
        for tr in find_table:
            alinks = tr.find_all('a')
            alinks = list(alinks)
            if len(alinks) >= 1:
                all_war_location.append(alinks[0].get_text().lower())
            alinks.reverse()
            if len(alinks) >= 1:
                all_war_part.append(alinks[0].get_text().lower())

        all_war_unique_part = set(all_war_part)
        print(all_war_unique_part)
        all_war_dict_frequency = {}
        for war in all_war_part:
            all_war_dict_frequency[war] = all_war_dict_frequency.get(war, 0) + 1
        all_war_frequency_great_4 = {}
        for key, value in all_war_dict_frequency.items():
            if value > 3:
                all_war_frequency_great_4[key] = value
            elif value == 1:
                all_war_frequency_great_4['ONE'] = all_war_frequency_great_4.get('ONE', 0) + 1
            elif value == 2:
                all_war_frequency_great_4['TWO'] = all_war_frequency_great_4.get('TWO', 0) + 1
            else:
                all_war_frequency_great_4['THE'] = all_war_frequency_great_4.get('THE', 0) + 1

        xvalues, yvalues = dc.replace_not_exist(all_war_frequency_great_4)
        percents = dc.get_percentage(all_war_frequency_great_4)
        xposition = np.arange(len(xvalues)) * 3
        plt.xlabel('Country Name')
        plt.ylabel('Number of Terrorist Incidents')
        plt.title(months[i-1] + " 2014 Terrorist Incidents Around the worlds")
        plt.xticks(xposition, xvalues)
        plt.bar(xposition, percents, align='center', width=1.2, label="Percentage")
        plt.bar(xposition, yvalues, align='center', width=1.2, label="Frequency")
        plt.legend()
        plt.show()


