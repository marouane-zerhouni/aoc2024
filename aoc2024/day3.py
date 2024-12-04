import re

def day3data(filename: str) -> str:
    with open(filename) as text_input:
        input_text = text_input.read().strip()
        #input_text = list(map(str, input_text))
        return input_text

day3puzzle = day3data("day3input.txt")

def firststar(input_string: str) -> int:
    multiplications = re.findall("mul\(\d{1,3},\d{1,3}\)", input_string)
    multiplications_sum = 0
    for i in range(len(multiplications)):
        multiplication_factors = re.findall("\d{1,3}",multiplications[i])
        multiplications_sum += int(multiplication_factors[0])*int(multiplication_factors[1])
    return multiplications_sum

print(firststar(day3puzzle))

def secondstar(input_string: str) -> int:
    multiplications = re.findall("do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", input_string)
    multiplications_sum = 0
    do_or_dont = 1
    for i in range(len(multiplications)):
        if multiplications[i] == "don't()":
            do_or_dont = 0
        elif multiplications[i] == "do()":
            do_or_dont = 1
        else:
            multiplication_factors = re.findall("\d{1,3}",multiplications[i])
            multiplications_sum += int(multiplication_factors[0])*int(multiplication_factors[1])*do_or_dont
    return multiplications_sum

print(secondstar(day3puzzle))