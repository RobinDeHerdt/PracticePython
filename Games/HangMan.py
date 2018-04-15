from random import randint


class HangManGame(object):
    WORD_LIST = ['Priest', 'Metallica']
    MAX_TRIES = 10

    tries = 0
    keyword = ""
    correct_indexes = []

    def __init__(self):
        self.keyword = self.get_random_keyword()
        self.play_round()

    def get_user_input(self):
        return input("Guess a letter: \n")

    def get_random_keyword(self):
        random_index = randint(0, len(self.WORD_LIST) - 1)
        return self.WORD_LIST[random_index].lower()

    def print_game_status(self):
        letters = list(self.keyword)
        for i in range(len(self.keyword)):
            if i not in self.correct_indexes:
                letters[i] = "_"

        print("".join(letters)  + "\n")

    def is_valid_input(self, user_input):
        if not user_input:
            return False

        if len(user_input) > 1:
            return False

        return True

    def play_round(self):
        if self.tries >= self.MAX_TRIES:
            print("Game over")
            return

        user_input = self.get_user_input().lower()

        if not self.is_valid_input(user_input):
            print("That doesn't seem quite right. Try again.")
            self.play_round()

        correct_guess = False
        for i in range(len(self.keyword)):
            if self.keyword[i] == user_input:
                correct_guess = True
                self.correct_indexes.append(i)

        if correct_guess:
            print("Correct! \n")
        else:
            self.tries += 1
            tries_left = self.MAX_TRIES - self.tries
            print("Incorrect! " + str(tries_left) + " tries left. \n")

        self.print_game_status()
        self.play_round()


HangManGame()
