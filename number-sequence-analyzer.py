import keyboard
import sys



def fibonacci(fibmath):
    numb1 = [0,0,1]
    for useless_variable in range(fibmath+1):
        numb1.append(numb1[-1]+numb1[-2])
    print(numb1)

def prime_num_chk(primechk):
    prime = True
    if primechk not in (-1,0,1) and primechk > 0:
        for numb3 in range(2,int(primechk)):
            if (primechk/numb3)%1 == 0:
                prime = False
    else:
        prime = False
    return prime

def prime_num_rng(start, end):
    primes = []
    is_prime = False
    for numb in range(start, end):
        is_prime = prime_num_chk(numb)
        if is_prime == True:
            primes.append(numb)
        is_prime = False
    return primes

def mult_table(base, length):
    for numb in range(1,length + 1):
        print(f'{base}*{numb}={base * numb}')

def factorial(factor):
    if factor <= 0:
        return 1
    for fact in range(1, factor):
        if fact <= 2:
            facts = factor * fact
        else:
            facts = facts * fact
    return facts

def collatz_seq(collatz):
    numb_a1 = 0
    while collatz > 1:
        if collatz % 2 == 0:
            collatz = int(collatz / 2)
            numb_a1 += 1
            print(numb_a1,"1", collatz)
        else:
            collatz = collatz * 3 + 1
            numb_a1 += 1        
            print(numb_a1,"2", collatz)




going = True

while going == True:
    choices_print= ["Please Select a Letter Key That Coralates to go to The Math Calculation!", "A: Fibonacci Sequence", "S: Prime Number Check", "D: Prime Number Range", "F: Multiplication Table", "G: Factorial", "H: Collatz Sequence", "STOP: Exit app"]
    selection_print = print(choices_print)
    key = input("Input a key: ")

    if key == 'a' or key == 'A':  
        print("Number must be a integer")
        inputsmthn = int(input("How many times?: "))
        fibonacci(inputsmthn)

    elif key == 's' or key == 'S':
        print("Number must be a integer")
        inputsmthn = int(input("What Number?: "))
        print(prime_num_chk(inputsmthn))
                
    elif key == 'd' or key == 'D':
        print("Numbers in range must be integers")
        inputsmthn1 = int(input("Starting Number: "))
        inputsmthn2 = int(input("Ending Number: "))
        print(prime_num_rng(inputsmthn1, inputsmthn2))
    
    elif key == 'f' or key == 'F':
        print("The two numbers for the multiplaction table must be integers")
        inputsmthn1 = int(input("Number Base: "))
        inputsmthn2 = int(input("Number Legnth: "))
        mult_table(inputsmthn1, inputsmthn2)

    elif key == 'g' or key == 'G':
        print("Number must be integer")
        inputsmthn = int(input("Factorial Size?: "))
        print(factorial(inputsmthn))

    elif key == 'h' or key == 'H':
        print("Number must be integer")
        inputsmthn = int(input("Choose a Number: "))
        collatz_seq(inputsmthn)

    elif key == 'STOP':
        going = False
        sys.exit(0)
