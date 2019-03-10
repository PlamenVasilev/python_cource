games_db = []

while True:
    data = input()

    if data == 'report':
        break

    player = data.split(' -> ')[0]
    player_games = list(map(int, data.split(' -> ')[1].split(', ')))

    games_db.append({
        'name': player,
        'games': player_games,
        'score': sum(player_games),
    })

while True:
    command = input()

    if command == 'end':
        break
    elif command == 'score descending':
        for player in sorted(games_db, key=lambda p: (-p['score'], p['name'])):
            print(f'{player["name"]}: {player["score"]}')
    elif command == 'score ascending':
        for player in sorted(games_db, key=lambda p: (p['score'], p['name'])):
            print(f'{player["name"]}: {player["score"]}')
    elif command == 'numberOfGames descending':
        for player in sorted(games_db, key=lambda p: (-len(p['games']), p['name'])):
            print(f'{player["name"]}: {len(player["games"])}')
    elif command == 'numberOfGames ascending':
        for player in sorted(games_db, key=lambda p: (len(p['games']), p['name'])):
            print(f'{player["name"]}: {len(player["games"])}')


