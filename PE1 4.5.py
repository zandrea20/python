def factorial(n):
    #Base Case
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    n=int(input("Please Input a non-negative number:"))
    if n < 0:
        print("The Factorial is not defined  for negative numbers ")
    else:
        print(f"The factoral of n is {factorial(n)}")


    main()