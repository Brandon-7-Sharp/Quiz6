from abc import ABC, abstractmethod

class Authentication(ABC):
    @abstractmethod
    def login(self, password:str):
        print("Loggin In With Verification")

class AuthenticationProcessor:
    def __init__(self, auth_method: Authentication):
        self.auth_method = auth_method

    def authentication_in(self, password:str):
        self.auth_method.login(password)


class GoogleAuth(Authentication):
    def login(self, password:str):
        if password == "mypassword123":
            print("GoogleAuth: You Are You")
        else:
            print("GoogleAuth: You Are NOT Who You Say You Are...")

class Logging(Authentication):
    def login(self, password:str):
        if password == "mypassword123":
            print("Logging: You Are You")
        else:
            print("Logging: You Are NOT Who You Say You Are...")

class Loguru(Authentication):
    def login(self, password:str):
        if password == "mypassword123":
            print("Loguru: You Are You")
        else:
            print("Loguru: You Are NOT Who You Say You Are...")




def main():
    google = AuthenticationProcessor(GoogleAuth())
    google.authentication_in("mypass")
    google.authentication_in("mypassword123")

    logging = AuthenticationProcessor(Logging())
    logging.authentication_in("mypass")
    logging.authentication_in("mypassword123")

    loguru = AuthenticationProcessor(Loguru())
    loguru.authentication_in("mypass")
    loguru.authentication_in("mypassword123")

if __name__=='__main__': 	
    main()