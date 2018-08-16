import random


class Main:
    # define variable
    sum_o = 0
    sum_x = 0
    opponent = 0
    welcome_text_show = ""
    random_score = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    array_table = []
    score_board = []
    round = 0

    # Start the program
    def run(self):
        random.shuffle(self.random_score)

        self.array_table = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        self.opponent = 0
        self.welcome_text_show = 0
        print("Welcome to XO game !!!")
        self.show_table()
        print("O, will move first. ")
        self.position_input()

    # Show table of game
    def show_table(self):
        print("-------------------")
        print("====== Board ====== ")
        print("-------------------")
        print("   B1  B2  B3")
        print("A1 " + self.array_table[0][0] + " | " + self.array_table[0][1] + " | " + self.array_table[0][2])
        print("  ---+---+---")
        print("A2 " + self.array_table[1][0] + " | " + self.array_table[1][1] + " | " + self.array_table[1][2])
        print("  ---+---+---")
        print("A3 " + self.array_table[2][0] + " | " + self.array_table[2][1] + " | " + self.array_table[2][2])
        print("-------------------")

    # Check input is in 1, 2, or 3
    def check_matching_input(self, result):
        challenge_array = [1, 2, 3]

        if result[0] in challenge_array and result[1] in challenge_array:
            return True
        else:
            return False

    # switching between X or O
    def toggle_opponent(self):
        self.opponent = not self.opponent

    # Change position weather when valid input
    def position_input(self):
        symbol = "O" if self.opponent == 0 else "X"
        print("Now, " + symbol + " turn : ")
        input_a = input(symbol + "(A) :")
        if not input_a:
            print("Wrong turn, try again !")
            self.position_input()
            return False
        input_b = input(symbol + "(B) :")
        if not input_b:
            print("Wrong turn, try again !")
            self.position_input()
            return False

        a = int(input_a)
        b = int(input_b)

        result = [a, b]
        if self.check_matching_input(result):
            if (self.array_table[a - 1][b - 1] == " "):
                self.array_table[a - 1][b - 1] = symbol
                if self.opponent == 0:
                    self.sum_o += self.random_score[((a * b) - 1)]
                else:
                    self.sum_x += self.random_score[((a * b) - 1)]

            else:
                print("Target can not be blank, try again !")
                self.position_input()
                return False
        else:
            print("Wrong turn, try again !")
            self.position_input()
            return False

        # Check Draw by round
        self.round += 1
        if self.round == 9:
            print("Draw! No one win.")
            self.show_table()
            self.play_again()
        elif not self.check_win():
            self.show_table()
            self.toggle_opponent()
            self.position_input()
        else:
            self.show_table()
            if self.opponent == 0:
                print("Hooley ! " + symbol + " is winner with point : " + str(self.sum_o) + " point!")
                self.save_point(self.sum_o)
            else:
                print("Hooley ! " + symbol + " is winner with point : " + str(self.sum_x) + " point!")
                self.save_point(self.sum_x)

    # check win game
    def check_win(self):
        if (self.check_same_value(self.array_table[0]) and self.array_table[0][0] != " ") or (
                self.check_same_value(self.array_table[1]) and self.array_table[1][0] != " ") or (
                self.check_same_value(self.array_table[2]) and self.array_table[2][0] != " "):
            return True
        elif (self.check_same_value([self.array_table[0][0], self.array_table[1][0], self.array_table[2][0]]) and
              self.array_table[2][
                  0] != " ") or (
                self.check_same_value([self.array_table[0][1], self.array_table[1][1], self.array_table[2][1]]) and
                self.array_table[0][
                    1] != " ") or (
                self.check_same_value([self.array_table[0][2], self.array_table[1][2], self.array_table[2][2]]) and
                self.array_table[0][2] != " "):
            return True
        elif (self.check_same_value([self.array_table[0][0], self.array_table[1][1], self.array_table[2][2]]) and
              self.array_table[0][
                  0] != " " or self.check_same_value(
                    [self.array_table[0][2], self.array_table[1][1], self.array_table[2][0]]) and self.array_table[0][
                  2] != " "):
            return True
        else:
            return False

    # check weather array are matched
    def check_same_value(self, array_parameter):
        i = 1
        while i < len(array_parameter):
            if array_parameter[i] != array_parameter[0]:
                return False
            i += 1
        return True

    # save point to score board on win
    def save_point(self, point):
        name = input("Please enter your name : ")
        _id = len(self.score_board) + 1
        self.score_board.append([_id, name, point])
        self.show_score_board()
        self.play_again()

    # show score board
    def show_score_board(self):
        print("-----------------------------------------")
        print("Table of best score             ")
        print("-----------------------------------------")
        sorted_score = sorted(self.score_board, key=self.get_key, reverse=True)
        loop = 0
        while loop < len(sorted_score) and loop < 5:
            print("%r. %r, score: %r" % ((loop + 1), sorted_score[loop][1], sorted_score[loop][2]))
            loop += 1
        print("-----------------------------------------")

    # only key helper for sorted
    def get_key(self, item):
        return item[2]

    # Play again and will not lose any score
    def play_again(self):
        # clear default
        self.sum_o = 0
        self.sum_x = 0
        self.round = 0
        
        answer = input("Do you need to try again? (Y/N)")
        if answer == 'y' or answer == 'Y':
            self.run()
        elif answer == 'n' or answer == 'n':
            self.goodbye()
        else:
            print("Incorrect answered please check !")
            self.play_again()

    # end or quite program score will lost here
    def goodbye(self):
        print("Thank you for playing, good bye ! :-)")


# Start the program
Main().run()
