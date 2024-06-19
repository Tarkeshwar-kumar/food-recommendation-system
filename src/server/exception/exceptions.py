
class CustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class NotAuthoriseError(CustomException):
    pass

class InValidRequest(CustomException):
    pass

class FoodDoesNotExist(CustomException):
    pass


class FoodAlreadyExists(Exception):
    pass