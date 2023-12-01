# Get input from the user
#user_input = input("Enter a number: ")

# Convert the input to a float (in case the user enters a decimal number)
#number = float(user_input)

# Calculate the square
#square = number ** 2

# Display the result
#print(f"The square of {number} is: {square}")




def classify_switch(model_number, placementlelo):
    # Extract numeric part from the model number
    model_numeric = ''.join(c for c in model_number if c.isdigit())

    # Convert placementlelo to an integer
    placementlelo = int(placementlelo)

    # Check conditions and classify the switch
    if model_numeric in ['5200', '5250', '5270'] and placementlelo <= 24:
        return "Type 1"

    elif model_numeric in ['5200', '5250', '5270', '5300', '5350', '5370'] and (placementlelo > 24 or model_numeric == '5400'):
        return "Type 2"

    elif "-S" in model_number or model_number.endswith("NX"):
        return "Core"

    else:
        return "Unknown"
