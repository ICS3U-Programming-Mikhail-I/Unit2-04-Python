#!/usr/bin/env python3
# Author: Mikhail Ibrahim
# Date: Mar 4, 2025
# Description: A Python program that calculates the total cost of a pizza, including HST, based on user input for the diameter.

def calculate_pizza_cost(diameter):
    """Function to calculate the total cost of a pizza based on the given diameter."""
    
    # Fixed costs
    labour_cost = 2.00
    rental_cost = 2.25
    
    # Ingredient cost per diameter inch
    ingredient_cost = 1.50 * diameter
    
    # Calculate subtotal and tax
    subtotal = labour_cost + rental_cost + ingredient_cost
    tax = subtotal * 0.13  # HST tax at 13%
    
    # Total cost including tax
    total_cost = subtotal + tax
    
    return round(total_cost, 2)

def main():
    """Main function to get user input for pizza diameter and display the total cost."""
    
    try:
        # Prompt the user to enter the diameter of the pizza
        diameter = float(input("Enter the diameter of the pizza in inches: "))
        
        # Calculate the total cost of the pizza
        total_cost = calculate_pizza_cost(diameter)
        
        # Display the result with two decimal places
        print(f"\nThe total cost of the pizza with a diameter of {diameter} inches is: ${total_cost:.2f}")
    
    except ValueError:
        # Handle invalid input if the user does not enter a number
        print("Invalid input! Please enter a numeric value.")

# Check if this script is being run directly (not imported) and call the main function
if __name__ == "__main__":
    main()
