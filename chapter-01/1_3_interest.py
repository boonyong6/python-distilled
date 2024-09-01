# interest.py

principal = 1000  # Initial amount
rate = 0.05  # Interest rate
num_years = 5  # Number of years
year = 1
while year <= num_years:
    principal = principal * (1 + rate)
    # print(year, principal)
    print(f"{year:>3d} {principal:0.2f}")
    year += 1
