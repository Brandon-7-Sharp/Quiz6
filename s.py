class Order:
    def __init__(self) -> None:
        self.order_details = {}
        self.order_details["items"] = []

    def add_item(self, item:str, price:str) -> None:
        self.order_details["items"] += [[item, price]]


    def remove_item(self, item:str, price:str) -> None:
        self.order_details["items"].remove([item, price])


class CustomerInfo:
    def __init__(self) -> None:
        self.customer_info = {}

    # Allows the addition of info and their values
    # You can add email and name. Do not have to add code to add an additional value of a person's address
    def add_info(self, type:str, info:str):
        self.customer_info[type] = (info)
        

# Class that calculates order total
class OrderTotal:
    def __init__(self) -> None:
        self.total = 0
        
    def add_costs(self, order:Order) -> None:
        for item in order.order_details["items"]:
            self.total += int(item[1])
            
    def calculate_total(self, discount:str) -> str:
        self.total -= (self.total * discount)

# Class that validates order details
class ValidateOrder:
    def __init__(self) -> None:
        self.orderPossible = True

    # Check to see if we have enouugh in inventory
    def validate_order(self, order:Order, inventory) -> None:
        for key, value in order.order_details["items"]:
            print()
            # print(inventory[value[key]])
            # if not int(inventory[item[index]]) > 0:
            print(inventory.inventory[key])
            if not int(inventory.inventory[key]) > 0:
                self.orderPossible = False
        
        if self.orderPossible:
            print("The order is possible")
        else:
            print("There is not enough stock in inventory...")

# Class that sends order confirmation
class ConfirmationEmail:
    def __init__(self) -> None:
        self.email = ""

    def send_email(self, email:str) -> None:
        print(f"Sending Email to {email}")
        print("Email Sent!")


# Class that updates inventory levels
class UpdateInventory:
    def __init__(self) -> None:
        self.inventory = {"car": 5, "toy": 10, "truck": 2}

    def update_inventory(self, order:Order):
        for key, value in order.order_details["items"]:
            print(key)
            print(value)
            self.inventory[key] -= 1


def main():

    # This way of structing adding info to the customer ensures you can create more categories. 
    # So, you can add email, name, ...,  and later have customers start adding their address.
    # Pass in the type of info, ie Name, address, email, and add 

    customer = CustomerInfo()
    customer.add_info("Name", "Shandra")
    customer.add_info("Age", "50")
    customer.add_info("Email", "shantastic007@gmail.com")

    order = Order()
    order.add_item("car", "20")
    order.add_item("toy", "50")
    order.add_item("truck", "10")
    print(order.order_details["items"])
    order.remove_item("toy", "50")
    print(order.order_details["items"])

    inventory = UpdateInventory()

    validtion = ValidateOrder()
    validtion.validate_order(order, inventory)

    total = OrderTotal()
    total.add_costs(order)
    print(f"Before Discount Total: {total.total}")
    total.calculate_total(0.1)
    print(f"After Discount Total: {total.total}")

    email = ConfirmationEmail()
    email.send_email(customer.customer_info["Email"])

    print(f"Previous Inventory:\n {inventory.inventory}")
    inventory.update_inventory(order)
    print(f"Updated Inventory:\n {inventory.inventory}")


if __name__=='__main__': 	
    main()