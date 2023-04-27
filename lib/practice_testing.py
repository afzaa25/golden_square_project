def divisible_by_three(number):
    if number % 3 == 0:
        return True
    else:
        return False

def divisible_by_five(number):
    if number % 5 == 0:
        return True
    else:
        return False
    
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply_number_string(string1, string2):
    return int(string1) * int(string2)

def make_snippet(text):
    words = text.split()
    if len(words) <=5:
        return text
    else:
        return " ".join(words[:5]) + "..."

print(make_snippet("the quick brown fox jumped over the fence and ran away from home"))

def count_words(string):
    words = string.split()
    return len(words)
