players_stats = [] 
players_stats.append({"name": "Aaron Judge", "Games": 123, "Home Runs": 44})
players_stats.append({"name": "Juan Soto", "Games": 121, "Home Runs": 34})
players_stats.append({"name": "Bobby Witt", "Games": 124, "Home Runs": 25})
players_stats.append({"name": "Shohei Ohtani", "Games":122, "Home Runs": 39})
players_stats.append({"name": "Marcell Ozuna", "Games": 124, "Home Runs": 36})
players_stats.append({"name": "Rafael Devers", "Games": 110, "Home Runs": 27})
players_stats.append({"name": "Yordan Alvarez", "Games": 117, "Home Runs": 25})
players_stats.append({"name": "Brent Rooker", "Games": 107, "Home Runs": 29})
players_stats.append({"name": "Gunnar Henderson", "Games": 123, "Home Runs": 33})
players_stats.append({"name": "Vladimir Guerrero", "Games": 123, "Home Runs": 25})

for i in range(10):
    # print(players_stats[i]["name"]["Home Runs"]/["Games"])
    player_games = players_stats[i]["Games"]
    player_name = players_stats[i]["name"]
    player_hr = players_stats[i]["Home Runs"]

    if player_hr/player_games > .250:
        print(player_hr/player_games)
        print(player_name)


    # print(player_hr/player_games)


# name:(Aaron Judge, Juan Soto, Bobby Witt, Shohei Ohtani, Marcell Ozuna, Rafael Devers, Yordan Alvarez, Brent Rooker, Gunnar Henderson, Vladimir Guerrero)
# average=({44/123, 34/121, 25/124, 39/122, 36/124, 27/110, 25/117, 29/107, 33/123, 25/123})
# percantage=({35.77, 28.10, 20.16, 31.97, 29.03, 24.55, 21.37, 27.10, 26.83, 20.33})
# print.name_percantage