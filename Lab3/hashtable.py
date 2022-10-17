
class HashTable:
    def __init__(self, size: int = 100):
        self.__size = 100
        self.__bucket = [[] for _ in range(size)]

    pass

    def __hash(self, element: any):
        return abs(hash(element) % self.__size)

    def add(self, element: any):
        """
        Add an element to the HashTable. Each element can be added only once in the hashtable
        :param element: object to be added
        :return: a tuple containing the position of the element in the bucket and then in the list
        """
        lookup = self.get(element)
        if lookup is not None:
            return lookup
        pos_in_bucket = self.__hash(element)
        pos_in_list = len(self.__bucket[pos_in_bucket])
        self.__bucket[pos_in_bucket].append(element)

        return pos_in_bucket, pos_in_list

    def find_by_pair(self, pos_in_bucket: int, pos_in_list: int):
        """
        Find an element in the hashTable by position in bucket and in list. If the index is not valid
        exceptions are raised
        :param pos_in_bucket: position in bucket
        :param pos_in_list: position in list
        :return: the found object
        """
        if pos_in_bucket < 0 or pos_in_bucket > self.__size:
            raise Exception("Invalid bucket position given")
        if pos_in_list < 0 or pos_in_list > len(self.__bucket[pos_in_bucket]):
            raise Exception("Invalid list position given")
        return self.__bucket[pos_in_bucket][pos_in_list]

    def get(self, element: any):
        """
        Look for an object in the hashTable.
        :param element: object to lookup
        :return: a tuple containing the position of the element in the bucket and then in the list
        """
        pos_in_bucket = self.__hash(element)
        for (pos_in_list, element_in_bucket) in enumerate(self.__bucket[pos_in_bucket]):
            if element_in_bucket == element:
                return pos_in_bucket, pos_in_list
        return None

