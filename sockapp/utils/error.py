class InvalidSocketProtocol(Exception):
    def __init__(self, message):
        self.__message = message

        super().__init__(self.__message)