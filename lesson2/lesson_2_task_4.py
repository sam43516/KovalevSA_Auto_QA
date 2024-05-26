def fizz_buzz(n):
    x = 1
    while x <= n:
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
        elif x % 5 == 0:
            print("Buzz")
        elif x % 3 == 0:
            print("Fizz")
        else:
            print(x)
        x = x + 1   

fizz_buzz(25)
               
