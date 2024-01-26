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
