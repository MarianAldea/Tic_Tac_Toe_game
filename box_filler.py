class BoxFiller():
    def __init__(self):
        self.invalid_move = False
        
    def fill_boxes(self, list_of_boxes, move, letter):
        row = move.lower()[0]
        column = move.lower()[1]
        boxes_to_fill = list_of_boxes
        self.invalid_move = False
        if row == "a":
            if column == "1":
                if boxes_to_fill[0] == " ":
                    boxes_to_fill.pop(0)
                    boxes_to_fill.insert(0, letter)
                else:
                    self.invalid_move = True
                    print("Invalid move, please try again.")
            elif column == "2":
                if boxes_to_fill[1] == " ":
                    boxes_to_fill.pop(1)
                    boxes_to_fill.insert(1, letter)
                else:
                    self.invalid_move = True
                    print("Invalid move, please try again.")
            elif column == "3":
                if boxes_to_fill[2] == " ":
                    boxes_to_fill.pop(2)
                    boxes_to_fill.insert(2, letter)
                else:
                    self.invalid_move = True
                    print("Invalid move, please try again.")
            else:
                self.invalid_move = True
                print("Invalid move, please try again.")

        elif row == "b":
            if column == "1":
                if boxes_to_fill[3] == " ":
                    boxes_to_fill.pop(3)
                    boxes_to_fill.insert(3, letter)
                else:
                    self.invalid_move = True
                    print("Invalid move, please try again.")
            elif column == "2":
                if boxes_to_fill[4] == " ":
                    boxes_to_fill.pop(4)
                    boxes_to_fill.insert(4, letter)

                else:
                    self.invalid_move = True
                    print("Invalid move, please try again.")
            elif column == "3":
                if boxes_to_fill[5] == " ":
                    boxes_to_fill.pop(5)
                    boxes_to_fill.insert(5, letter)

                else:
                    self.invalid_move = True
                    print("Invalid move, please try again.")
            else:
                self.invalid_move = True
                print("Invalid move, please try again.")

        elif row == "c":
            if column == "1":
                if boxes_to_fill[6] == " ":
                    boxes_to_fill.pop(6)
                    boxes_to_fill.insert(6, letter)
                else:
                    self.invalid_move = True
                    print("Invalid move, please try again.")
            elif column == "2":
                if boxes_to_fill[7] == " ":
                    boxes_to_fill.pop(7)
                    boxes_to_fill.insert(7, letter)
                else:
                    self.invalid_move = True
                    print("Invalid move, please try again.")
            elif column == "3":
                if boxes_to_fill[8] == " ":
                    boxes_to_fill.pop(8)
                    boxes_to_fill.insert(8, letter)
                else:
                    self.invalid_move = True
                    print("Invalid move, please try again.")
            else:
                self.invalid_move = True
                print("Invalid move, please try again.")
        else:
            self.invalid_move = True
            print("Invalid move, please try again.")
        return boxes_to_fill
