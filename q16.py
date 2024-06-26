def get_int():
    try:
        a = int(input("Enter any integer value"))
        return f"integer value"
    except ValueError:
        print("Invalid input ! plase enter only integer value")
        return get_int()

print(f"you enterd {get_int()}")
