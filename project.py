# Syntax Practice Code

def check_number(num):
    """Check if number is positive, negative or zero."""
    if num > 0:
        print(f"{num} is Positive ✅")
    elif num < 0:
        print(f"{num} is Negative ❌")
    else:
        print("Number is Zero ⚡")

# Loop for 3 attempts
for i in range(3):
    try:
        n = int(input(f"Enter number {i+1}: "))
        check_number(n)
    except ValueError:
        print("❗ Please enter a valid integer.")
