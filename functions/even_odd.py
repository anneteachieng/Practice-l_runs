#checks if number is even or odd

def even_odd():
    number = int(input("Enter a number."))
#use % to check if it divides completely without leaving any value
    if number%2 == 0:
        print(f"Even number")
    else:
        print(f"Odd number")
even_odd()
