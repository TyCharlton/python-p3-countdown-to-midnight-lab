# your code goes here!

import time

def countdown(num):
    while num > 0:
        print(f'{num} SECOND(S)!')
        num -= 1
    print('HAPPY NEW YEAR!')

def countdown_with_sleep(num):
    while num > 0:
        print(f'{num} SECOND(S)!')
        time.sleep(1)
        num -= 1
    print('HAPPY NEW YEAR!')

# Test the functions
countdown(10)  # Test countdown without sleep
print("\n")  # Just for separation

# def countdown(num):
#     while num > 0:
#         print(num)
#         num -= 1
#     print("HAPPY NEW YEAR!")

# def countdown_with_sleep(num):
#     while num > 0:
#         print(num)
#         time.sleep(1)
#         num -= 1
#     print("HAPPY NEW YEAR!")

# Test the function
# countdown(10)  





