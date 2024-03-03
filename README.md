# EXTRA CREDIT CODE:
## How To Use
To use the program, start by running it.
In the terminal there will be several options to choose from
```
Input 0 To Quit:
Input 1 To View Data:
Input 2 To Choose An Activity
Input 3 To Add User:
```
If you choose 0, the program ends
If you choose 1, it will then ask you to enter a user id
```
Enter Your User Id: 
```
The program will then display the user's data
If you choose 2, it will then ask you to enter a user id
Afterwards it will generate random values for data, which will be stored to the user id you entered

If you choose 3, it will then as you to enter a user id and it will add it to the 'database'

## Suggested Method of Testing
First start the program
Then Enter 3 to add a new user
Input 'user' as the user id

Now you will be back in the main loop
Next Enter 2 to do an activity
Enter the new user id we just created: 'user'
Enter 0 for Running
Now you will be back in the main loop

Next Enter 2 to do an activity
Enter the new user id we just created: 'user'
Enter 1 for Yoga
Now you will be back in the main loop

Next Enter 2 to do an activity
Enter the new user id we just created: 'user'
Enter 2 for Cycling
Now you will be back in the main loop

Each time you did an activity, the program automatically added the data to your specified user id
To test if the data is there follow these commands
Enter 1 to view data
Enter 'user' 
The program now displays the new activities that you just did in the order you did them with the dummy data
