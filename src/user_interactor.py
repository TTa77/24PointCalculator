import time
from threading import Thread


class Interactor(Thread):
    def __init__(self):
        super().__init__()

        self.num_1: int = 0
        self.num_2: int = 0
        self.num_3: int = 0
        self.num_4: int = 0

        self.result: str = ""
        self.no_result = False

        self.receive_input()

    def set_result(self, res: str):
        self.result = res

    def set_no_result(self):
        self.no_result = True

    def receive_input(self):
        user_input = input("Input 4 numbers, separate by SPACE and submit by ENTER. Or type \"Q\" to exit: ")

        while not Interactor.check_input(user_input):
            if user_input.strip() in ("Q", "q"):
                exit()
            print("Invalid input, please check and re-type.\n")
            user_input = input("Input 4 numbers, separate by SPACE and submit by ENTER. Or type \"Q\" to exit: ")

        self.num_1, self.num_2, self.num_3, self.num_4 = \
            tuple(i for i in filter(lambda x: str.isdecimal(x), user_input.split(" ")))

    @staticmethod
    def check_input(received_input: str):
        elements = tuple(filter(lambda x: str.isdecimal(x), received_input.split(" ")))
        if len(elements) != 4:
            return False
        else:
            return True

    def generate_output(self):
        if self.result:
            print("{} {} {} {} can generate 24 as \"{}\"".format(
                self.num_1, self.num_2, self.num_3, self.num_4, self.result))
        else:
            print("{} {} {} {} cannot generate 24!".format(
                self.num_1, self.num_2, self.num_3, self.num_4))

    def run(self):
        while not (self.result or self.no_result):
            time.sleep(0.1)
        self.generate_output()
