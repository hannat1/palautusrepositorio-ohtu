from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)
import string


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        for letter in username:
            if letter not in string.ascii_lowercase:
                raise UserInputError("Username should contain only lowercase letters from a to z")
        
        valid_password = False
        for char in password:
            if char not in string.ascii_letters:
                valid_password = True
        if not valid_password:
            raise UserInputError("Password must contain some other character than letters")
            
        if len(username) < 4:
            raise UserInputError("Username should be more than 3 characters") 
        
        elif self._user_repository.find_by_username(username) is not None:
            raise UserInputError("Username is already in use")
        
        elif len(password) < 8:
            raise UserInputError("Password should be more than 8 characters")

        elif password != password_confirmation:
            raise UserInputError("Passwords differ")

user_service = UserService()
