from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.queue = list()
        self.__length = 0

    def __len__(self):
        return self.__length

    def enqueue(self, value):
        self.queue.append(value)
        self.__length += 1

    def dequeue(self):
        if self.__length > 0:
            self.__length -= 1
            return self.queue.pop(0)
        return -1

    def search(self, index):
        try:
            if index < 0 or index > (self.__length - 1):
                raise IndexError
        except IndexError:
            raise IndexError("Índice Inválido ou Inexistente")
        return self.queue[index]
