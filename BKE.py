from typing import List


def choose_square(name: str, filled_in_dict: dict) -> int:
    """
    Prompts the user to choose a square, and prompts again if an invalid square number is entered.
    :param name:  name of the player.
    :param filled_in_dict:  how the squares are filled in.
    :return:   integer of the chosen square.
    """
    p = input(name + " is aan zet. Toets een cijfer om een vakje in te vullen:")
    p = int(p)
    if p == 0 or p >= 10:
        print(str(p) + " is geen valide vakje.")
        p = choose_square(name, filled_in_dict)
    else:
        filled_in_set = set(filter(lambda k: filled_in_dict[k], filled_in_dict.keys()))
        if p in filled_in_set:
            print(str(p) + " is al ingevuld.")
            p = choose_square(name, filled_in_dict)
    return p


def check_if_3_the_same(filled_in_dict: dict, k1: int, k2: str, k3: int) -> int:
    """
    Checks if 3 squares are the same and not None.
    :param filled_in_dict: how the squares are filled in.
    :param k1, k2, k3: indexes art which equality is checked.
    :return: int which is 0 if not the same and 1 if the same.
    """
    return (filled_in_dict[k1] == filled_in_dict[k2]) and (filled_in_dict[k1] == filled_in_dict[k3]) and filled_in_dict[
        k1]


def check_win(filled_in_dict: dict) -> int:
    """
    Checks if a user has won.
    :param filled_in_dict: how the squares are filled in.
    :return: An int, 0 if the user hasn't won yet, 1 if he has.
    """
    row0 = check_if_3_the_same(filled_in_dict, 1, 2, 3)
    row1 = check_if_3_the_same(filled_in_dict, 4, 5, 6)
    row2 = check_if_3_the_same(filled_in_dict, 7, 8, 9)
    col0 = check_if_3_the_same(filled_in_dict, 1, 4, 7)
    col1 = check_if_3_the_same(filled_in_dict, 2, 5, 8)
    col2 = check_if_3_the_same(filled_in_dict, 3, 6, 9)
    dia1 = check_if_3_the_same(filled_in_dict, 3, 5, 7)
    dia2 = check_if_3_the_same(filled_in_dict, 1, 5, 9)
    return row0 or row1 or row2 or col0 or col1 or col2 or dia1 or dia2


def print_field(filled_in_dict: dict):
    """
    Prints the playing field, with noughts and crosses at the correct places.
    :param filled_in_dict: how the squares are filled in.
    :return: Nothing
    """
    els = []
    for k, v in filled_in_dict.items():
        if not v:
            els.append(str(k))
        else:
            els.append(v)
    print("   |   |   \n {6} | {7} | {8} \n   |   |   \n-----------\n   |   |   \n {3} | {4} | {5} \n   |   |   \n"
          "-----------\n   |   |   \n {0} | {1} | {2} \n   |   |   ".format(els[0],
                                                                            els[1],
                                                                            els[2],
                                                                            els[3],
                                                                            els[4],
                                                                            els[5],
                                                                            els[6],
                                                                            els[7],
                                                                            els[8]))


def main():
    """
    Main method, lets 2 players play a tic-tac-toe game
    :return: Nothing
    """
    finished = 0
    turns = 0
    filled_in_dict = {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None}

    print("Welkom bij boter, kaas en eieren.")
    name_1 = input("Typ de naam van speler 1 ('O') in:")
    name_2 = input("Typ de naam van speler 2 ('X') in:")

    print_field(filled_in_dict)

    while finished == 0:
        position = choose_square(name_1 + " ('O')", filled_in_dict)
        filled_in_dict[position] = "O"
        print_field(filled_in_dict)
        if check_win(filled_in_dict):
            input(name_1 + " heeft gewonnen. Gefeliciteerd! \
                  Toets Enter om te beeindigen.")
            break
        turns += 1
        if turns == 5:
            input("Niemand heeft gewonnen. Gelijkspel! \
                  Toets Enter om te beeindigen.")
            break

        position = choose_square(name_2 + " ('X')", filled_in_dict)
        filled_in_dict[position] = "X"
        print_field(filled_in_dict)
        if check_win(filled_in_dict):
            input(name_2 + " heeft gewonnen. Gefeliciteerd!\
                  Toets Enter om te beeindigen.")
            finished = 1


if __name__ == "__main__":
    main()
