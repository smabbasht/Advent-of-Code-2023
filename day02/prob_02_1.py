CONSTRAINT_BAG = {"red": 12, "green": 13, "blue": 14}
print(CONSTRAINT_BAG)


def parse_game(game_string):
    game = game_string.split(": ")[1]
    game = game.split(";")
    game = [i.split(",") for i in game]
    game = [[(int(i.split()[0]), i.split()[1]) for i in j] for j in game]
    return game


def is_possible(sum_bag, constraint_bag):
    for i in sum_bag:
        if i[0] > constraint_bag[i[1]]:
            return False
    return True


def compute_sum(game):
    truths_inverted = []
    for i in game:
        truths_inverted.append(not is_possible(i, CONSTRAINT_BAG))
    return not sum(truths_inverted)


def read_file():
    with open("input02") as f:
        return f.readlines()


def main():
    sum = 0
    games_file = read_file()
    for ind, game_string in enumerate(games_file):
        game = parse_game(game_string)
        sum += (compute_sum(game))*(ind+1)
    return sum


print(main())
