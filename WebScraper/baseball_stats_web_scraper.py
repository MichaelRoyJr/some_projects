import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable

url = "http://freep.sportsdirectinc.com/baseball/mlb-teams.aspx?page=/data/mlb/teams/stats/2019/team2982.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

if response:
    player_list = []

    #get list of players and trim off category names
    players = soup.table.find_all('tr')
    del players[0]
    for player in players:
        stats = player.find_all('td')

        #store stats into dictionary
        player_dict = {}
        player_dict['Name'] = stats[0].get_text().strip()
        player_dict['G'] = stats[1].get_text().strip()
        player_dict['AB'] = stats[2].get_text().strip()
        player_dict['R'] = stats[3].get_text().strip()
        player_dict['H'] = stats[4].get_text().strip()
        player_dict['2B'] = stats[5].get_text().strip()
        player_dict['3B'] = stats[6].get_text().strip()
        player_dict['HR'] = stats[7].get_text().strip()
        player_dict['RBI'] = stats[8].get_text().strip()
        player_dict['BB'] = stats[10].get_text().strip()
        player_dict['K'] = stats[11].get_text().strip()
        player_dict['SB'] = stats[12].get_text().strip()
        player_dict['Avg'] = stats[14].get_text().strip()
        player_dict['SLG'] = stats[15].get_text().strip()
        player_dict['OBP'] = stats[16].get_text().strip()

        #add dictionary to list of dictionaries
        player_list.append(player_dict)

    #display in table form using PrettyTable
    table = PrettyTable(player_list[0].keys())
    table.align['Name'] = 'l'
    for player in player_list:
        table.add_row(player.values())
    print(table)

else:
    print("URL not found")