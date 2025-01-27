"""
    Name: Patricia Gariando
    Student ID: 991 446 494
    Task: Assignment 4
    Date: Dec. 7 2023
"""
menuBoard = """
+ - - - + - - - + - - - + - - - +
|      - SALES MANAGEMENT -     |
+ - - - + - - - + - - - + - - - +
|   1. Add Salesperson          |
|   2. Delete Salesperson       |
|   3. Display Salesforce       |
|   4. Add Sales                |
|   5. Displays Sales           |
|   6. End Program              |
+ - - - + - - - + - - - + - - - +"""
displaySales = """
+ - - - + - - - - + - - - - + - - - +
|          2023 SalesForce          |
+ - - - + - - - - + - - - - + - - - +
ID       Name            City        """
salesHeader = """
+ - - - + - - - - + - - - - + - - - - - + - - - + - - - + - - - +
|                   S A L E S     T A B L E                     |
+ - - - + - - - - + - - - - + - - - - - + - - - + - - - + - - - +"""

furnitureSales = ["ID", "Tables", "Desks", "Chairs"]
processedSales = []

def loadSales(): # save SalesPerson data into list 
    salesList = []
    with open("SalesPerson.dat", 'r') as rFile:
        for person in rFile:
            person = person.replace('\n' , ' ')
            salesList.append(person)
    return salesList

def searchID(idNum, salesPersonList): # search if the ID is available or not  
    for salesPerson in salesPersonList:
        fields = salesPerson.split(",")
        if idNum == fields[0]:
            return True
    else: return False
    
def deleteID(idNum, salesPersonList): # remove the line if ID is in the list 
    for salesPerson in salesPersonList:
        if idNum in salesPerson:
            salesPersonList.remove(salesPerson)
    
def displaySalesForce(salesPersonList): # display salesforce 
    display = ''
    for worker in salesPersonList:
        worker = worker.replace(',' , '\t')
        display += worker + '\n'
    return display

def addSalesForce(salesDataList): # add salesforce into .dat file 
    with open("Sales.dat", 'w') as wFile:
        for salesPerson in salesDataList:
            wFile.write(salesPerson)

def addSalesPerson(salesPersonList): # add salesperson back into .dat file 
    with open("SalesPerson.dat", 'w') as wFile:
        for salesPerson in salesPersonList:
            data = salesPerson + "\n"
            wFile.write(data)

def main():
    salesPersonList = loadSales() # load the records of SalesPerson.dat into a list 
    salesDataList = []
    totalTableSales = totalDeskSales = totalChairSales = 0 # counters

    print(menuBoard) # display menu board 
    userNum = int(input("\nEnter choice: ")) # prompt the user for a choice 

    while userNum < 1 or userNum > 6:
        userNum = int(input("Invalid Entry! --- Enter choice: ")) 

    while userNum != 6:
        if userNum == 1: # Add Salesperson 
            idNum = input("\nEnter ID number: ")
            while searchID(idNum, salesPersonList):
                idNum = input("\nThe following ID number is unavailable --- Please enter ID number: ")
            else:
                idName = input("\nEnter ID name: ")
                idCity = input("\nEnter ID city: ")
            processedWorker = idNum + ", " + idName + ", " + idCity
            salesPersonList.append(processedWorker)

        elif userNum == 2: # Delete Salesperson 
            idNum = input("\nEnter ID number of salesperson to remove from the list: ")
            while searchID(idNum, salesPersonList) == False : 
                idNum = input("\nThe following ID number does not exist  --- Please enter ID number: ")
            else: 
                deleteID(idNum, salesPersonList)
                print("Warning: Salesperson has been removed from the list!")

        elif userNum == 3: # Display Salesforce
            print(displaySales)
            print(displaySalesForce(salesPersonList))

        elif userNum == 4: # Add Sales 
            idNum = input("\nEnter ID number: ")
            while searchID(idNum, salesPersonList) == False:
                idNum = input("\nThe following ID number does not exist --- Please enter ID number: ")
            while idNum in processedSales:
                idNum = input("\nThe following ID has already been processed --- Enter another ID number to process: ")
            else: 
                furnitureSales.append(idNum)
                processedSales.append(idNum)
                tables = int(input("Enter table sales: ")) # prompt the user for table sales 
                while tables < 0: tables = int(input("Invalid --- Enter table sales: "))
                else:
                    furnitureSales.append(tables)
                    totalTableSales += tables
                desks = int(input("Enter desk sales: ")) # prompt the user for desk sales
                while desks < 0: desks = int(input("Invalid --- Enter desk sales: "))
                else: 
                    furnitureSales.append(desks)
                    totalDeskSales += desks
                chairs = int(input("Enter chair sales: ")) # prompt the user for chair sales 
                while chairs < 0: chairs = int(input("Invalid --- Enter chair sales: "))
                else:
                    furnitureSales.append(chairs)
                    totalChairSales += chairs
                processedData = idNum + ", " + str(tables) + ", " + str(desks) + ", " + str(chairs) + "\n"
                salesDataList.append(processedData)

        elif userNum == 5: # display Sales Table 
            furnitureSales.append("Total") # we want the [Total] to be at the end of the entries 
            furnitureSales.append(totalTableSales)
            furnitureSales.append(totalDeskSales)
            furnitureSales.append(totalChairSales)
            if len(furnitureSales) > 4:
                count = 0
                print(salesHeader)
                for row in range(0, len(furnitureSales)):
                    print("|".ljust(5), furnitureSales[row], end="\t")
                    count += 1
                    if count%4 == 0: print("|")
                print("+ - - - + - - - - + - - - - + - - - - - + - - - + - - - + - - - +")  
            else: 
                print("No data has been processed.")
        userNum = int(input("\nEnter choice: ")) # prompt the user for a choice
    else: 
        addSalesPerson(salesPersonList) # rewrite existing data 
        addSalesForce(salesDataList) # save new data 

if __name__ == "__main__": main() # call the main function 
print("\nPatricia J. Gariando: 991 446 494\n") # display name and student ID