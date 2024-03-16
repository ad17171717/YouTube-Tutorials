#simple Python script that prompts a user for a number and returns the square root of the number

def sqroot(x):
    return x**0.5

if __name__ == "__main__":
    num = float(input('Input a real number to find the square root\n'))

    print(sqroot(num))
