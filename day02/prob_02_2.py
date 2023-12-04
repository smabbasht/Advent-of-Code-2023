# CONSTRAINT_BAG = {"red": 12, "green": 13, "blue": 14}
# print(CONSTRAINT_BAG)


def parse_game(game_string):
    game = game_string.split(": ")[1]
    game = game.split(";")
    game = [i.split(",") for i in game]
    game = [[(int(i.split()[0]), i.split()[1]) for i in j] for j in game]
    return game


def compute_minimum_bag(game):
    min_bag = {'red': 0, 'green': 0, 'blue': 0}
    new_game = []
    for i in game:
        new_game += i
    for i in new_game:
        min_bag[i[1]] = i[0] if i[0] > min_bag[i[1]] else min_bag[i[1]]
    return min_bag["red"] * min_bag["green"] * min_bag["blue"]


def read_file():
    with open("input02") as f:
        return f.readlines()


def main():
    sum = 0
    games_file = read_file()
    for ind, game_string in enumerate(games_file):
        game = parse_game(game_string)
        sum += compute_minimum_bag(game)
    return sum


print(main())
