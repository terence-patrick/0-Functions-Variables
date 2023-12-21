def dollars_to_float(d):
    """converts dollars_to_float string to float and strips '$'."""
    return float(d.replace("$", ""))


def percent_to_float(p):
    """converts string to a float and returns a decimal."""
    return float(p.strip("%")) / 100


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


main()
