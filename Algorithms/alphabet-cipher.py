class AlphabetCipher(object):
    ALPHABET_STRING = 'abcdefghijklmnopqrstuvwxyz'

    alphabet = []

    def __init__(self):
        self.alphabet = self.get_alphabet_list()

    def get_alphabet_list(self):
        result = []
        for char in self.ALPHABET_STRING:
            result.append(char)

        return result

    def get_full_keyword(self, keyword, message):
        repeat = len(message) // len(keyword)
        rest = len(message) % len(keyword)

        return repeat * keyword + keyword[:rest]

    def get_index_for_letter(self, letter):
        return self.alphabet.index(letter)

    def get_letter_for_index(self, index):
        return self.alphabet[index]

    def encode(self, keyword, message):
        result = ""

        full_keyword = self.get_full_keyword(keyword, message)
        for index, char in enumerate(full_keyword):
            message_index = self.get_index_for_letter(message[index])
            keyword_index = self.get_index_for_letter(char)

            encoded_letter_index = message_index + keyword_index

            # Wrap around from index 25 to index 0,
            # since there are 26 letters in the alphabet
            if encoded_letter_index > (len(self.alphabet) - 1):
                encoded_letter_index = encoded_letter_index - len(self.alphabet)

            result += self.get_letter_for_index(encoded_letter_index)

        print(result)


alphabet_cipher = AlphabetCipher()
alphabet_cipher.encode("bond", "theredfoxtrotsquietlyatmidnight")
alphabet_cipher.encode("train", "murderontheorientexpress")
alphabet_cipher.encode("garden", "themolessnuckintothegardenlastnight")