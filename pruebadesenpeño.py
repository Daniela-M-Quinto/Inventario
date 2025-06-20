inventory={} # Dictionary for storing products 



print ("welcome to the inventory management system")

# Define the menu with a function 
def menu ():
    print("\n----- MENU -----")
    print("1) Add products to inventory: ")
    print("2) Consult product: ")
    print("3) update price: ")
    print("4) remove products")
    print("5) calculate the value of inventory")
    print("6) GO OUT")
    
# Function to add products to inventory
def Add_products_to_inventory():
    global inventory
    name = input("Enter the name of the product: ")
    price = float(input("Enter the price: "))
    amount = int(input("Enter the amount: "))
    
# Data validation
    if price <= 0 or amount < 0:
        print("Invalid input. Price must be positive and amount cannot be negative.")
        return
    
# Product storage
    inventory[name] = [price, amount]
    print(f"Product '{name}', Price '{price}', amount '{amount}' added successfully!")
    
# Function to update inventory
def consult_product():
    global inventory
    consult = input("Enter product name to consult: ")
    if consult in inventory:
        info = inventory[consult]
        print(f"Product: {consult}, Price: ${info[0]}, Amount: {info[1]}")
    else:
        print("Product not found.")
        
# Function to update the price
def update_price():
    global inventory
    consult = input("Enter product name to update price: ")
    if consult in inventory:
        new_price = float(input("Enter new price: "))
        inventory[consult][0] = new_price
        print(f"Price of '{consult}' updated to ${new_price}.")
    else:
        print("Product not found.")


# Function to consult product       
def Consult_product():
    global inventory
    consult=input("product nome to consult: ")
    if consult in inventory:
        info =inventory [consult]
        print("In inventory")
        print(f"Products: {consult}, price: {info[0]}, amount: {info[1]}")
    else:
        print("Not in inventory")
        
        
# Function to update price               
def update_price():
    global inventory
    consult= input("Product name update: ")
    if consult in inventory:
        pricenew=float(input("Product price: "))
        inventory [consult][0]= pricenew
    else:
        print ("Product not found")

def remove_products():
    global inventory
    Remove = input("Name of the producto to removed: ")
    if Remove in inventory:
       del inventory [Remove]
       print (f"the products {Remove}, was remove")
    else:
        print("product not found")
        
# Function to calculate the total value of the inventory
        
def calculate_the_value_of_inventory():
    
    total= (lambda:sum(info[0]*info[1] for info in inventory.values()))()
    print(f"total inventory value:${total:.2f}")

# Main program loop            
while True:
    menu()
    option= input("Choose an option (1-6): ")
    if option == "1":
        Add_products_to_inventory()
    elif option == "2":
        Consult_product()
    elif option == "3":
        update_price()
    elif option == "4":
        remove_products()
    elif option == "5":
        calculate_the_value_of_inventory()
    elif option == "6":
        print("GO OUT")
    else:
        ("Invalid option")
 
        
      
        