#Exercises

# print Hello World
print("check check hello world")

# : fizz buzz : classic do you know it or do you not know it interview coding question: write a function that takes in a number (N) and prints numbers 1..N, and if the num is divisible by 3, return 'fizz', divisible by 5, return buzz, divisible by 3 & 5, return 'fizzbuzz'

def fizzbuzz(n):
    for i in range(n):
        if i%3 == 0 and i%5 == 0:
            print("fizzbuzz")
        elif i%3 == 0:
            print("fizz")
        elif i%5 == 0:
            print("buzz")
        else:
            print(i)
    return "Fizzbuzz complete!"

# : self dividing numbers : numbers in which the digits in the number can divide the original number, self dividing number cannot contain a 0 digit, and we are given the left and right boundaries, inclusive

# : thoughts : we have to go through every number, so runtime is n, at least

# : take aways : definitely read the prompt 2-3 times, ask questions, run through examples, and make sure you understand the question before bludgeoning off on the key board

# : solutions
def selfDividingNumber(a, b):
    return 0
    
# : look into unix commands
        
