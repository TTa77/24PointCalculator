from threading import Thread


class Calculator(Thread):
    def __init__(self, four_numbers: tuple):
        super().__init__()

        self.sequence = list(four_numbers)
        self.possible_arranges = []

        self.generate_all_candidates()

    def generate_all_candidates(self):
        operators = ['+', '-', '*', '/']

        for first_operator in operators:
            for second_operator in operators:
                for third_operator in operators:

                    sequence_with_operators = Calculator.insert_operators(
                        self.sequence, (first_operator, second_operator, third_operator))

                    sequences_with_one_parentheses = Calculator.insert_one_pair_parentheses(sequence_with_operators)
                    sequences_with_two_parentheses = Calculator.insert_two_pairs_parentheses(sequence_with_operators)

                    self.possible_arranges.extend(sequences_with_one_parentheses)
                    self.possible_arranges.extend(sequences_with_two_parentheses)

    @staticmethod
    def insert_operators(sequence_to_insert: list, operators: tuple) -> list:
        current_number_sequence = sequence_to_insert.copy()
        current_number_sequence.insert(1, operators[0])
        current_number_sequence.insert(3, operators[1])
        current_number_sequence.insert(5, operators[2])
        # ['1', '+', '2', '-', '3', '*', '4']
        return current_number_sequence

    @staticmethod
    def insert_one_pair_parentheses(current_number_sequence: list) -> list:
        res_ls = []

        for left_idx in range(0, 4, 2):
            for right_idx in range(left_idx + 3, 8, 2):
                current_sequence_with_parentheses = current_number_sequence.copy()
                if (left_idx != 0 and current_sequence_with_parentheses[left_idx-1] != '+') or \
                        (left_idx == 0 and right_idx != 7 and
                         current_sequence_with_parentheses[right_idx+1] in ["*", "/"]):

                    current_sequence_with_parentheses.insert(left_idx, "(")
                    current_sequence_with_parentheses.insert(right_idx+1, ")")
                    res_ls.append(current_sequence_with_parentheses)

        return res_ls

    @staticmethod
    def insert_two_pairs_parentheses(current_number_sequence: list) -> list:
        res_ls = []
        # ['(', '1', '-', '2', ')', '*', '(', '3', '/', '4', ')']

        # ['(', '1', '-', '(', '2', '*', '3', ')', ')', '/', '4']
        # ['(', '(', '1', '-', '2', ')', '*', '3', ')', '/', '4']

        # ['1', '-', '(',  '(', '2', '*', '3', ')', '/', '4', ')']
        # ['1', '-', '(', '2', '*', '(', '3', '/', '4', ')', ')']
        pos = [[(0, 4), (6, 10)],
               [(0, 6), (3, 7)], [(0, 6), (1, 5)],
               [(2, 8), (3, 7)], [(2, 8), (5, 9)]]
        for pos_pair in pos:
            current_sequence_with_parentheses = current_number_sequence.copy()

            for idxs in pos_pair:
                current_sequence_with_parentheses.insert(idxs[0], "(")
                current_sequence_with_parentheses.insert(idxs[1], ")")

            res_ls.append(current_sequence_with_parentheses)

        return res_ls

    def calculate_24(self):
        for seq in self.possible_arranges:
            formula = "".join(seq)
            try:
                outcome = eval(formula)
                if outcome == 24:
                    return formula
            except ZeroDivisionError:
                pass
        return ""

    def run(self):
        res = self.calculate_24()
        return res


