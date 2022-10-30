from Lab3.hashtable import HashTable


class SymbolTable:
    def __init__(self, size: int = 100):
        self.identifier_hash_table = HashTable(size)
        self.int_constants_hash_table = HashTable(size)
        self.string_constants_hash_table = HashTable(size)

    def add_identifier(self, name: str):
        """
        Add an identifier to the symbol Table
        :param name: name of the identifier
        :return: the position where the identifier has been added
        """
        pos = self.identifier_hash_table.add(name)
        return pos

    def add_int_constant(self, constant: int):
        """
        Add an int constant to the symbol Table
        :param constant: value of the constant
        :return: the position where the constant has been added
        """
        pos = self.int_constants_hash_table.add(constant)
        return pos

    def add_string_constant(self, string: str):
        """
        Add a string constant to the symbol Table
        :param string: value of the string constant
        :return: the position where the string has been added
        """
        pos = self.string_constants_hash_table.add(string)
        return pos

    def find_identifier(self, name: str):
        """
        Lookup an identifier
        :param name: name of the identifier
        :return: the positions where the identifier is found
        """
        return self.identifier_hash_table.get(name)

    def find_int_constant(self, constant: int):
        """
        Lookup an int constant
        :param constant: name of the constant
        :return: the positions where the constant is found
        """
        return self.int_constants_hash_table.get(constant)

    def find_string_constant(self, string: str):
        """
        Lookup a string constant
        :param string: name of the constant
        :return: the positions where the constant is found
        """
        return self.string_constants_hash_table.get(string)

    def get_identifier(self, pos_in_bucket: int, pos_in_list: int):
        """
        Get an identifier by position in bucket and in list
        :param pos_in_bucket: position in bucket
        :param pos_in_list: position in list
        :return: the name of the found identifier
        """
        return self.identifier_hash_table.find_by_pair(pos_in_bucket, pos_in_list)

    def get_int_constant(self, pos_in_bucket: int, pos_in_list: int):
        """
        Get an int constant by position in bucket and in list
        :param pos_in_bucket: position in bucket
        :param pos_in_list: position in list
        :return: the value of the int constant
        """
        return self.int_constants_hash_table.find_by_pair(pos_in_bucket, pos_in_list)

    def get_string_constant(self, pos_in_bucket: int, pos_in_list: int):
        """
        Get a string constant by position in bucket and in list
        :param pos_in_bucket: position in bucket
        :param pos_in_list: position in list
        :return: the value of the string constant
        """

        return self.string_constants_hash_table.find_by_pair(pos_in_bucket, pos_in_list)
