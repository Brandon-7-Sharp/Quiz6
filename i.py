from abc import ABC, abstractmethod

class Library(ABC):
    @abstractmethod
    def searching(self, title:str):
        print(f"Searching for book with title {title}...")
        print("Book Found!")

    @abstractmethod
    def borrowing(self):
        print("You are borrowing a book")

    @abstractmethod
    def returning(self):
        print("You are returning a book")

class Catalog(ABC):
    @abstractmethod
    def changing_catalog(self, choice: str, title:str):
        if choice == "add":
            print(f"Adding {title} to the catalog")
        elif choice == "remove":
            print(f"Removing {title} from the catalog")

class Reports(ABC):
    @abstractmethod
    def generate_report(self, choice: str, title:str):
        if choice == "borrowing":
            print(f"Creating a report on borrowing for {title}")
        elif choice == "overdue":
            print(f"Creating a report for an overdue book for {title}")
        elif choice == "popularity":
            print(f"Creating a report on book popularity for {title}")

class User(Library):
    def searching(self, title:str):
        return super().searching(title)
    def borrowing(self):
        return super().borrowing()
    def returning(self):
        return super().returning()
    
class Librarian(Library, Catalog, Reports):
    def searching(self, title:str):
        return super().searching(title)
    def borrowing(self):
        return super().borrowing()
    def returning(self):
        return super().returning()
    def changing_catalog(self, choice: str, title:str):
        return super().changing_catalog(choice, title)
    def generate_report(self, choice: str, title:str):
        return super().generate_report(choice, title)

def main():
    user = User()
    librarian = Librarian()

    user.searching("The Great Gatsby")
    user.borrowing()
    user.returning()

    librarian.searching("The Ballad of Songbirds and Snakes")
    librarian.borrowing()
    librarian.returning()
    librarian.generate_report("borrowing", "The Ballad of Songbirds and Snakes")
    librarian.generate_report("overdue", "Under the Whispering Door")
    librarian.generate_report("popularity", "Scythe")
    librarian.changing_catalog("add", "Of Mice and Men")
    librarian.changing_catalog("remove", "Everlost")

if __name__=='__main__': 	
    main()