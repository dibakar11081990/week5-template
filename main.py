# 1. Basic Function Definitions
def greet(name):
    return f"Hello, {name}!"


# 2. Sum of Two Numbers
def sum_of_two(a:float, b:float):
    return a+b

# 3. Maximum of Three Numbers
def max_of_three(a:int, b:int, c:int):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b 
    
    return c

# 4. Factorial Calculation
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


# 5. Check Prime Number
def is_prime(a):
    if a<2:
        return False
    
    for i in range(2, (a//2 + 1)):
        if a%i == 0:
            return False
    return True

# 6. Count Vowels in a String
def count_vowels(stc:str):
    stc = stc.lower()
    v_cnt = 0

    for alp in stc:
        if alp in ('a', 'e', 'i', 'o', 'u'):
            v_cnt += 1

    return v_cnt 


