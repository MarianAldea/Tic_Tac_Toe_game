import box_filler
import win_condition

list_of_boxes = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
i = 1
verify = win_condition.CheckWinner()
check_boxes = box_filler.BoxFiller()
def print_board(list):
    row_1 = f"|   | 1 | 2 | 3 |\n"
    row_2 = f"| a | {list[0]} | {list[1]} | {list[2]} |\n"
    row_3 = f"| b | {list[3]} | {list[4]} | {list[5]} |\n"
    row_4 = f"| c | {list[6]} | {list[7]} | {list[8]} |\n"

    row_list = [row_1, row_2, row_3, row_4]
    for i in row_list:
        print (i)
print_board(list_of_boxes)

while verify.game_on:
    if i % 2 == 1:
        move_x = input("You are X, type your move: ")
        letter = "X"
    else:
        move_x = input("You are 0, type your move: ")
        letter = "0"
    list_of_boxes = check_boxes.fill_boxes(move=move_x, letter=letter, list_of_boxes=list_of_boxes)
    if check_boxes.invalid_move:
        i -= 1
    print_board(list_of_boxes)
    if i >= 3:
        verify.verify_winner(checked_boxes=list_of_boxes, letter=letter, turn_number=i)
    i += 1
    if not verify.game_on:
        answer = input("Play again? Y/N")
        print(answer)
        if answer == "Y":
            verify.restart_game()
            i = 1

