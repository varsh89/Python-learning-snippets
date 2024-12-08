import math
def simple_interest(principal:float, rateofinterest:float, time:float) -> int:
    si=(principal * rateofinterest * time)/100
    return math.floor(si)

def get_valid_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
        
principal = get_valid_number("Enter the principal amount: ")
rateofinterest = get_valid_number("Enter the rate of interest: ")
time = get_valid_number("Enter the time in years: ")

result = simple_interest(principal, rateofinterest, time)
print(f"Simple Interest: {result}")