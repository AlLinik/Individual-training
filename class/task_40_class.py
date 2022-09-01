class Alphabet:

    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    # @staticmethod - метод может быть статическим (снимаем #, убираем self)
    def print(self):
        from string import ascii_uppercase
        return ascii_uppercase

    def letters_num(self):
        return len(self.print())


class EngAlphabet(Alphabet):
    __letters_num = Alphabet.letters_num

    def __init__(self, lang, letters):
        super(EngAlphabet, self).__init__(lang, letters)

    def is_en_letter(self, letter):
        if letter in self.print():
            print(f'Буква "{letter}" ОТНОСИТСЯ к английскому алфавиту.')
        else:
            print(f'Буква "{letter}" НЕ ОТНОСИТСЯ к английскому алфавиту.')

    def letters_num(self):
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        return 'Example text in English'


if __name__ == '__main__':
    obj_EA = EngAlphabet('EN', 'ABC')
    print(obj_EA.print())
    obj_A = Alphabet('EN', 'ABC')
    print(obj_A.letters_num())
    obj_EA.is_en_letter('F')
    obj_EA.is_en_letter('Щ')
    print(obj_EA.example())

