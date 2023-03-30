
class EmailNotValidError(Exception):
    pass


class PasswordNotValidError(Exception):
    pass


class UserNotExistError(Exception):
    pass


class UserAlreadyExistError(Exception):
    pass


class EmailOrPasswordIncorrectError(Exception):
    pass


class ServerError(Exception):
    pass


class ClientError(Exception):
    pass


class RequestRegistrationError(Exception):
    pass


