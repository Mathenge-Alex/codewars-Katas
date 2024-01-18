# Test 2

# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

# Examples
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"
# Notes
# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number is first.



def high_and_low(numbers):
    nums = numbers.split()
    print("Nums: ", nums)
    numbers_list = []
    numbers_list = [int(i) for i in nums]
    print("Numbers List: ", numbers_list)
    
    high = max(numbers_list)
    low = min(numbers_list)
    numbers = [high, low]
    return numbers

print(high_and_low("1 2 3 4 5"))  # return "5 1"
print(high_and_low("1 2 -3 4 5")) # return "5 -3"
print(high_and_low("1 9 3 4 -5")) # return "9 -5"
