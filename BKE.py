from typing import List


def choose_square(name: str, filled_in_dict: dict) -> int:
    """
    Prompts the user to choose a square, and prompts again if an invalid
    square number is entered.
    :param name:  name of the player.
    :param filled_in_dict:  how the squares are filled in.
    :return:   integer of the chosen square.
    """
    chosen_square = input(name + " is aan zet. Toets een cijfer om een vakje "
                                 "in te vullen:")
    try:
        chosen_square = int(chosen_square)
        if chosen_square <= 0 or chosen_square >= 10:
            print(str(chosen_square) + " is geen valide vakje.")
            return choose_square(name, filled_in_dict)
        else:
            filled_in_set = set(filter(lambda k: filled_in_dict[k],
                                       filled_in_dict.keys()))
            if chosen_square in filled_in_set:
                print(str(chosen_square) + " is al ingevuld.")
                return choose_square(name, filled_in_dict)
        return chosen_square
    except ValueError:
        print(chosen_square + " is geen valide input.")
        return choose_square(name, filled_in_dict)


def check_if_3_the_same(v1: str, v2: str, v3: str) -> int:
    """
    Checks if 3 squares are the same and not None.
    :param v1, v2, v3: square values of which equality is checked.
    :return: int which is 0 if not the same and 1 if the same.
    """
    return (v1 == v2) and (v1 == v3) and v1


def check_win(filled_in_dict: dict) -> int:
    """
    Checks if a user has won.
    :param filled_in_dict: how the squares are filled in.
    :return: an int, 0 if the user hasn't won yet, 1 if he has.
    """
    row0 = check_if_3_the_same(filled_in_dict[1], filled_in_dict[2],
                               filled_in_dict[3])
    row1 = check_if_3_the_same(filled_in_dict[4], filled_in_dict[5],
                               filled_in_dict[6])
    row2 = check_if_3_the_same(filled_in_dict[7], filled_in_dict[8],
                               filled_in_dict[9])
    col0 = check_if_3_the_same(filled_in_dict[1], filled_in_dict[4],
                               filled_in_dict[7])
    col1 = check_if_3_the_same(filled_in_dict[2], filled_in_dict[5],
                               filled_in_dict[8])
    col2 = check_if_3_the_same(filled_in_dict[3], filled_in_dict[6],
                               filled_in_dict[9])
    dia1 = check_if_3_the_same(filled_in_dict[3], filled_in_dict[5],
                               filled_in_dict[7])
    dia2 = check_if_3_the_same(filled_in_dict[1], filled_in_dict[5],
                               filled_in_dict[9])
    return row0 or row1 or row2 or col0 or col1 or col2 or dia1 or dia2


def print_line(v1: str, v2: str, v3: str):
    """
    Prints a single line of the playing field
    :param v1, v2, v3: values to be filled in in the lines
    """
    print("   |   |   \n {0} | {1} | {2} \n   |   |   ".format(v1, v2, v3))


def print_field(filled_in_dict: dict):
    """
    Prints the playing field, with noughts and crosses at the correct places.
    :param filled_in_dict: how the squares are filled in.
    """
    els = []
    for k, v in filled_in_dict.items():
        if not v:
            els.append(str(k))
        else:
            els.append(v)
    print_line(els[6], els[7], els[8])
    print("-----------")
    print_line(els[3], els[4], els[5])
    print("-----------")
    print_line(els[0], els[1], els[2])


def play_turn(name: str, symbol: str, filled_in_dict: dict) -> bool:
    """
    Lets 1 player perform a turn.
    :param name: the player's name.
    :param symbol: the player's symbol (O/X).
    :param filled_in_dict: how the squares are filled in.
    :return: whether the player won or not.
    """
    position = choose_square(name + " ('" + symbol + "')", filled_in_dict)
    filled_in_dict[position] = symbol
    print_field(filled_in_dict)
    if check_win(filled_in_dict):
        input(name + " heeft gewonnen. Gefeliciteerd!\
              Toets Enter om te beeindigen.")
        return True
    return False


def main():
    """
    Main method, lets 2 players play a tic-tac-toe game
    """
    turns = 0

    filled_in_dict = {1: None, 2: None, 3: None, 4: None, 5: None, 6: None,
                      7: None, 8: None, 9: None}

    print("Welkom bij boter, kaas en eieren.")
    name_1 = input("Typ de naam van speler 1 ('O') in:")
    name_2 = input("Typ de naam van speler 2 ('X') in:")

    print_field(filled_in_dict)

    while True:
        if play_turn(name_1, "O", filled_in_dict):
            break
        turns += 1
        if turns == 5:
            input("Niemand heeft gewonnen. Gelijkspel! \
                  Toets Enter om te beeindigen.")
            break
        if play_turn(name_2, "X", filled_in_dict):
            break


if __name__ == "__main__":
    main()
