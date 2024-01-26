"""BPP Pizza Price Calculator

This program calculates the total price for pizza orders based on various factors such as the number of pizzas ordered, delivery requirement, day of the week, and whether the customer used the app for ordering.

Functions:
    - get_user_input(prompt, input_type=int): Takes user input with error handling and returns the input of the specified type.
    
    - calculate_price(num_pizzas, delivery_required, is_tuesday, used_app): Calculates the total price for pizza orders considering the base price, Tuesday discount, delivery charge, and app discount.
    
    - main(): The main function that interacts with the user, gathers input, calls the calculate_price function, and prints the total price.

Variables:
    - base_price (float): The base price of a pizza.
    
    - tuesday_discount (float): The discount applied on Tuesdays.
    
    - delivery_charge (float): The charge for delivery if applicable.
    
    - app_used_discount (float): The discount applied when the customer uses the app for ordering.
"""


base_price = 12
tuesday_discount = 0.5
delivery_charge = 2.50
app_used_discount = 0.25

def get_user_input(prompt, input_type=int):
    while True:
        try:
            user_input = input_type(input(prompt))
            return user_input
        except ValueError:
            print("Please enter a valid input.")

def calculate_price(num_pizzas, delivery_required, is_tuesday, used_app):
   

    total = num_pizzas* base_price
    # Apply Tuesday discount
    if is_tuesday:
        total *= tuesday_discount

    # Apply delivery cost
    if delivery_required and num_pizzas < 5:
        total += delivery_charge

    # Apply app discount
    if used_app:
        total *= (1 - app_used_discount)


    return total

def main():
    print("BPP Pizza Price Calculator")
    print("==========================")

    num_pizzas = get_user_input("How many pizzas ordered? ", input_type=int)
    delivery_required = get_user_input("Is delivery required? (Y/N) ", input_type=str).upper() == "Y"
    is_tuesday = get_user_input("Is it Tuesday? (Y/N) ", input_type=str).upper() == "Y"
    used_app = get_user_input("Did the customer use the app? (Y/N) ", input_type=str).upper() == "Y"

    total_price = calculate_price(num_pizzas, delivery_required, is_tuesday, used_app)
    print(f"\nTotal Price: £{total_price:.2f}.")

if __name__ == "__main__":
    main()
