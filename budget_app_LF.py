#!/usr/bin/env python
# coding: utf-8

# In[48]:


#foundations
import csv
import os
headings = ['Date','Income or Expense','Amount','Description']

#if csv file doesn't exist create it
if not os.path.exists('./transactions.csv'):
    #write new file by opening csv in write mode
    with open('./transactions.csv', 'w') as transactions_file:
        #use csv.DictWriter to write the headings into the csv
        csv_writer = csv.DictWriter(transactions_file,headings)
        csv_writer.writeheader()
        
#if the csv file does exist check that it has headings and the right heads
if os.path.exists('./transactions.csv'):
    #open csv in read mode
    with open("transactions.csv", "r") as transactions_file:
        #test for csv headings with .feildnames
        reader = csv.DictReader(transactions_file).fieldnames
        
        #start try except block because if csv is completely empty it will return a None TypeError
        try:
            #iterate through headings in csv
            for header in reader:
                #if csv has same headings as specified in the headings list then pass
                if header in headings:
                    pass
                #if csv is missing any headings then write a fresh csv with headings
                else:
                    with open('./transactions.csv', 'w') as transactions_file:
                        transactions_file.write("Date,Income or Expense,Amount,Description\n")
        #if csv is completely empty and returns None TypeError then write a fresh csv with headings
        except TypeError:
            with open('./transactions.csv', 'w') as transactions_file:
                transactions_file.write("Date,Income or Expense,Amount,Description\n")
                


#micro function
#called upon user command 'a'
def add_transaction():
    
    #a dictionary to temporarily store user input appropriately
    new_transaction = {
        "Date": 'MM-DD-YYYY',
        "Income or Expense": 'E',
        "Amount": 0.0,
        "Description": 'word'
        }
    
    #take user input in a functional type
    new_transaction["Date"] = str(input("Enter date of transaction in MM-DD-YYYY format:\n"))
    new_transaction["Income or Expense"] = str(input("\nEnter 'I' for income, or 'E' for expense:\n").upper())
    new_transaction["Amount"] = float(input("\nEnter the monetary amount of the budget item:\n"))
    #allocate pos or neg to amount based on income or expense
    if 'E' == new_transaction["Income or Expense"]:
        new_transaction["Amount"] = -abs(new_transaction["Amount"])
    elif 'I' == new_transaction["Income or Expense"]:
        new_transaction["Amount"] = abs(new_transaction["Amount"])
    new_transaction["Description"] = str(input("\nEnter a description for the budget item:\n"))


    #open the file and append the user input into it
    with open('transactions.csv', 'a') as transactions_file:
        transactions_file.write(f"{new_transaction['Date']},{new_transaction['Income or Expense']},{new_transaction['Amount']},{new_transaction['Description']}\n")

    print("\n\t\t\t\tTransaction added\n")
    #signify end of function
    print("\t\t\t"+("\u2500"* 32))




#micro function
#called upon user command 'b'
def view_account_balance():
    
    #open csv for read-only
    with open("transactions.csv", "r") as transactions_file:

        #setup variable for dictreader to pass csv into
        reader = csv.DictReader(transactions_file)    

        #set neutral flt account starting balance
        balance = 0.0

        #start loop to iterate through amounts which have already been forced into +/-
        for row in list(reader):
            #iterate through and tally amounts into the balance
            balance += float(row["Amount"])

        #print the balance as a float with only 2 decimal points
        print("Net balance:")
        print(float("{:.2f}".format(balance)))
    
    #signify end of function
    print("\n\n\t\t\t"+("\u2500"* 32))
        


#micro function
#called upon user command 'v'
def view_all_transactions():

    #open csv file
    with open("transactions.csv", "r") as transactions_file:

        #use csv.DictReader method to open csv as dictionary
        reader = csv.DictReader(transactions_file)
        
        #first, print a set of headings
        print("MM-DD-YYYY:\t\tIncome or Expense:\tAmount:\t\tDescription:")
        
        #then print the contents of the csv/DictReader via the reader variable
        for row in list(reader):
            print(f"{row['Date']}\t\t{row['Income or Expense']}\t\t\t{row['Amount']}\t\t{row['Description']}",sep=', ')
    
    #signify end of function
    print("\n\n\t\t\t"+("\u2500"* 32))
    


#macro function
#initialises the program
def start_app():

    current_task = ""
    try:
        while current_task != "q":
            print("Press [a] to add a transaction, [b] to view the account balance, [v] to view all transactions, or [q] to quit.\n")

            #get user input as lower case
            current_task = input("What would you like to do?\n")
            current_task = current_task.lower()

            #if "a" command is given, run add_transaction()
            if current_task == "a":
                #signify starting of a function
                print("\t\t\t"+("\u2500"* 32))
                print("\n\t\t\t\tADD TRANSACTION\n")
                add_transaction()

            #if "b" command is given, run view_account_balance()
            if current_task == "b":
                #signify starting of a function
                print("\t\t\t"+("\u2500"* 32))
                print("\n\t\t\t\tACCOUNT BALANCE\n")
                view_account_balance()

            #if "v" command is given, run view_all_transactions()
            if current_task == "v":
                #signify starting of a function
                print("\t\t\t"+("\u2500"* 32))
                print("\n\t\t\t\tALL TRANSACTIONS\n")
                view_all_transactions()

            #if user inputs 'q' say goodbye
            if current_task == "q":
                print("\n\t\t\t\t    Goodbye\n")
                #signify end
                print("\t\t\t"+("\u2500"* 32))

            #deal with the return from functions and wrong commands
            else:
                print("\n\t\t\t\tEnter a command\n")
    except ValueError:
        print("\nPlease input correctly...\n")
        start_app()

#ceremonial initialisation
print("""\t\t\t\t..................
\t\t\t\t| LEMONADE STAND |
\t\t\t\t| BUDGET TRACKER |
\t\t\t\t******************\n""")        

#initialise
start_app()


# In[ ]:




