from player import Player, Forward, MiddleField, DefenseField
from factory import register, unregister, create_player
import json


def load_players():
    with open("data.json", 'r') as f:
        return json.load(f)


def common_way(data):
    players = []
    for player in data['players']:
        role = player['role']
        if role == 'FW':
            players.append(Forward(**player))
        elif role == 'MF':
            players.append(Forward(**player))
        elif role == 'DF':
            players.append(DefenseField(**player))

    for player in players:
        print(player, player.info())


def register_player():
    register('FW', Forward)
    register('MF', MiddleField)
    register('DF', DefenseField)


def factory_way(data):
    players = data.copy()
    register_player()

    for args in players['players']:
        player = create_player(args)
        print(player, player.info())


if __name__ == '__main__':
    data = load_players()
    common_way(data)
    print('----------')
    factory_way(data)