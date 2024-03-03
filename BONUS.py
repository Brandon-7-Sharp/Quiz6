# Created By: Brandon Sharp
# SOLID Principles Satisfied:
# S: Each of my classes does a specific task. My DataStorage only does actions with data, my activities only execute their activity through the ActivityMonitor, my Distance and Steps classes 
#       only return a random distance and num of steps
# O: New Classes can be added and the program would still function. 
#       For outputting the available activities, I use the __subclasses__() function to see the available classes that implement the Activity class. I store this in an array and loop through it for the
#       number of activities(running, swimming, yoga) that there are. My Activity class can be used by any new activity with any new variable that they might add since I will always loop through a dictionary
#       of the available data for each activity. A List is added that holds the objects of each activity type class, so if a new class is added, that new class will be displayed and can be chosen without altering 
#       the code
# L: I have the Distance and Steps class that some of the subcalsses of Actitivy implement, that way no new Actitivy or the activity Yoga will be forced to contain data that does not make sense for that 
#       activity. For example, Yoga class does not implement Distance since you are stationary
# I: My Yoga class is not forced to implement Distance or Steps, and my Cycling class is not inforced to implement Steps
# D: My code does not have dependencies from low level modules on high level modyles beacuse none of my variables are hard coded. Each variable is only depended on the level it is in



import random
from abc import ABC, abstractmethod

# User Class created for each user
class User:
    def __init__(self, id:str) -> None:
        self.user_id = id

# Activity Class used for creating a new activity, each new activity type must inherit Activity. New Activity classes can be created later
class Activity(ABC):
    # Initializes each Activity with the following vars
    def __init__(self, name:str, avg_heart_rate:str, high_heart_rate:str, calories:int, time:int) -> None:
        self.name = name
        self.avg_heart_rate = avg_heart_rate
        self.high_heart_rate = high_heart_rate
        self.calories_burned = calories
        self.avg_time_for_completion = time

    # Abstract method that ensures all children of Activity must have. The method creates data for the user's activity
    @abstractmethod
    def activity(self):
        rand = random.random() + 0.5
        return{"Activity":self.name, "Average Heart Rate": round(self.avg_heart_rate * rand), "Highest Heart Rate": round(self.high_heart_rate * rand), "Total Time":round(self.avg_time_for_completion * rand), "Calories Burned":round(self.calories_burned * rand)}
        
# Distance Class that is inherited if a child of Activity needs Distance parameters
class Distance(ABC):
    # Abstract method that the children of Distance have to implement. Returns a random distance based on a specific Activity's distance parameters
    @abstractmethod
    def distance(self):
        return str(round((2 * random.random()) + 0.5, 2))

# Steps Class that is inherited if a child of Activity needs Steps parameters
class Steps(ABC):
    # Abstract method that the children of Steps have to implement. Returns a random number of steps based on a specific Activity's steps parameters
    @abstractmethod
    def steps(self):
        return str(round(1000 * random.random()))

# Running class that is a child of Activity, Distance, and Steps, meaning it has to implement all of their abstract methods
class Running(Activity, Distance, Steps):
    def __init__(self) -> None:
        super().__init__("Running", 110, 140, 700, 60)

    def activity(self):
        # Gets the random activity data(Heart Rate, How Long) and stores it in info var
        info = super().activity()
        # Appends the additional vars to the info of Running activity
        info["Distance"] = self.distance()
        info["Steps"] = self.steps()
        return info

    def distance(self):
        # Returns a random number for distance
        return super().distance()
    
    def steps(self):
        # Returns a random number for steps
        return super().steps()

# Yoga class that is a child of ONLY Activity, meaning it has to implement all of its abstract methods
class Yoga(Activity):
    def __init__(self) -> None:
        super().__init__("Yoga", 50, 80, 200, 30)

    # Gets the random activity data(Heart Rate, How Long) and returns it
    def activity(self):
        return super().activity()

# Cycling class that is a child of Activity, Distance, and Steps, meaning it has to implement all of their abstract methods
class Cycling(Activity, Distance):
    def __init__(self) -> None:
        super().__init__("Cycling", 70, 140, 1200, 90)

    def activity(self):
        # Gets the random activity data(Heart Rate, How Long) and stores it in info var
        info = super().activity()
        # Appends the additional vars to the info of Running activity
        info["Distance"] = self.distance()
        return info

    def distance(self):
        # Returns a random number for distance
        return super().distance()

# Each Activity has to access ActivityMonitor to get to Activity, ensuring more Activities can be created later, such as swimming and rock climbing
class ActivityMonitor:
    def __init__(self, activity:Activity) -> None:
        self.activity = activity

    def activity_monitor(self):
        self.activity.activity()

class DataStorage:
    # Initialize DataStorage With 'Dummy" Data
    def __init__(self) -> None:
        self.users = {"Bob": {"Excercise1": {"Activity": "Running", "Average Heart Rate": "108", "Highest Heart Rate": "146", "Total Time": "65", "Calories Burned": "800"}, 
                              "Excercise2": {"Activity": "Yoga", "Average Heart Rate": "60", "Highest Heart Rate": "90", "Total Time": "47", "Calories Burned": "60"},
                              "Excercise3": {"Activity": "Cycling", "Average Heart Rate": "111", "Highest Heart Rate": "141", "Total Time": "62", "Calories Burned": "850"}} ,
                      "Sandy":{"Excercise1": {"Activity": "Running", "Average Heart Rate": "103", "Highest Heart Rate": "168", "Total Time": "80", "Calories Burned": "1020"},
                               "Excercise2": {"Activity": "Yoga", "Average Heart Rate": "50", "Highest Heart Rate": "78", "Total Time": "27", "Calories Burned": "57"},
                               "Excercise3": {"Activity": "Cycling", "Average Heart Rate": "103", "Highest Heart Rate": "168", "Total Time": "80", "Calories Burned": "1020"}},
                      "Gordon": {"Excercise1":{"Activity": "Running", "Average Heart Rate": "97", "Highest Heart Rate": "155", "Total Time": "64", "Calories Burned": "780"},
                                 "Excercise2": {"Activity": "Yoga", "Average Heart Rate": "55", "Highest Heart Rate": "73", "Total Time": "38", "Calories Burned": "48"},
                                 "Excercise3": {"Activity": "Cycling", "Average Heart Rate": "95", "Highest Heart Rate": "152", "Total Time": "68", "Calories Burned": "750"}}}

    # Returns the data based on the specified user id
    def get_data(self, user_id: str):
        if user_id in self.users:
            return(self.users[user_id])

    # Creates a new user based on the specified user id
    def add_user(self, user:str):
        self.users[user] = {}

    # Adds data to the specified user id
    def add_data(self, user:str, data):
        i = 1
        # While there are data entries with this Excercise Number, continue until it is a new Excercise Number
        while ("Excercise" + str(i)) in self.users[user]:
            i += 1
        self.users[user]["Excercise" + str(i)] = data

# Displays The Information For a specified user
class Display:
    def display_user_info(self, user_id:str, data_storage:DataStorage):
        # Gets the data based on user id
        info = data_storage.users[user_id]
        for key in info:
            print(f"{key}:")
            for innerkey in info[key]:
                print(f"\t{innerkey}: {info[key][innerkey]}")
        print("All Units Are In Minutes and Miles\n")

def main():
    
    # Creates the Display and DataStorage Objects
    continues = True
    display = Display()
    data_storage = DataStorage()

    # Creates an array of all the Subclasses of Activity to later decide which class to create
    activities = Activity.__subclasses__()
    print(activities)
    
    # While User wants to use program, continue
    while continues:
        # Asks the user what they want to do and follows that if/elif statement
        user_input = input("Input 0 To Quit:\nInput 1 To View Data:\nInput 2 To Choose An Activity\nInput 3 To Add User:\n")

        # User wants to quit
        if user_input == "0":
            continues = False
            print("Goodbye!")
            exit()

        # User wants to view the data of the specififed user
        elif user_input == "1":
            user_id = input("Enter Your User Id: \n")
            # Displays the user's data
            display.display_user_info(user_id, data_storage)

        # User wants to do an activity, which will automatically add that data to the users data in DataStorage
        elif user_input == "2":
            # Asks the user which activity they want to do and follows that if/elif statement
            i = 0
            dic = {}
            # Loops through the available activities, ensuring new Activity Classes can be added in the future
            for activ in activities:
                print(f"Input {i} For {str(activ)[17:-2]}:")
                dic[i] = {str(activ)[17:-2]}
                i += 1
            activity = input()
            
            # Depending on the activity, a different class is created and inputed data into
            users_id = input("Input User Id: \n")
            # Uses the input of the user(which mathces the index of the array of Activit classes made earlier) to create a class on the activity the user chose
            type = activities[int(activity)]
            # Creates a new class for the chosen activity and gets data for it 
            new_activity = ActivityMonitor(type())
            info = new_activity.activity.activity()
            # Adds the data to the specified user
            data_storage.add_data(users_id, info)

        # Create a new user
        elif user_input == "3":
            user_new_id = input("Type A User Id: \n")
            user = User(user_new_id)
            # Adds a new empty dictionary to the DataStorage
            data_storage.add_user(user.user_id)
            print("Successfully Created A New User!\n")
            continue


if __name__=='__main__': 	
    main()