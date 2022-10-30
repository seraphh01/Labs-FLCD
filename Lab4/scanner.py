import re

from Lab3.symbol_table import SymbolTable


class Scanner:
    def __init__(self, program: str, tokens: list[str], scanner_tokens: list[str]):
        self.program = program
        self.tokens = tokens
        self.symbol_table = SymbolTable()
        self.pif = []
        self.index = 0
        self.current_line = 1
        self.line_index = 0
        self.scanner_tokens = scanner_tokens
        pass

    def is_reserved_keyword_operator_separator(self, token: str):
        """
        Check if token is a reserved keyword, an operator, or a separator
        :param token: string
        :return: True if it is, False otherwise
        """
        return token in self.scanner_tokens

    def is_identifier(self, token: str):
        """
        Check if the token is an identifier
        :param token: string
        :return: True if it is, False otherwise
        """
        return re.fullmatch(r'[_a-zA-Z][_a-zA-Z0-9]{0,30}', token) is not None

    def is_int_constant(self, token: str):
        """
        Check if the token is an int constant
        :param token: string
        :return: True if it is, False otherwise
        """
        return re.fullmatch(r'(^[-+]?[1-9][0-9]*$)|(^0$)', token) is not None

    def is_string_constant(self, token: str):
        """
        Check if the token is a string constant
        :param token: string
        :return: True if it is, False otherwise
        """
        return re.fullmatch(r'^"[^"\\]*(?:\\.[^"\\]*)*"$', token) is not None

    def gen_PIF(self, token: str, index: int):
        """
        Add index of token to the program internal form
        :param token: string
        :param index: index of token in the symbol table
        :return: nothing
        """
        self.pif.append((token, index))
        pass

    def scan(self):
        """
        Scan the program and generate PIF and feed Symbol Table with each token
        :raise Exception: if an invalid token is found
        :return:
        """
        while len(self.tokens) > 0:
            current_token = self.tokens.pop(0)
            if current_token == '\n':
                self.current_line += 1
                self.line_index = 0
                self.index += 1
                continue
            elif current_token.isspace():
                self.line_index += 1
                self.index += 1
                continue

            while self.index < len(self.program) and self.program[self.index:].find(current_token) != 0:
                self.index += 1
                self.line_index += 1

            if self.is_reserved_keyword_operator_separator(current_token):
                self.gen_PIF(current_token, 0)
            elif self.is_int_constant(current_token):
                index = self.symbol_table.add_int_constant(int(current_token))
                self.gen_PIF(current_token, index)
            elif self.is_string_constant(current_token):
                index = self.symbol_table.add_string_constant(current_token)
                self.gen_PIF(current_token, index)
            elif self.is_identifier(current_token):
                index = self.symbol_table.add_identifier(current_token)
                self.gen_PIF(current_token, index)
            else:
                raise Exception(
                    f"Lexical error at line {self.current_line}, character {self.line_index}, invalid token: {current_token}")

            self.index += len(current_token)
            self.line_index += len(current_token)
