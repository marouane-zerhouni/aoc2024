import re

def day1data(filename: str) -> list:
    with open(filename) as text_input:
        input_list = text_input.read().strip()
        input_list = re.split('\n|   ', input_list)
        input_list = list(map(str, input_list))
        return input_list

day1puzzle = day1data("day1input.txt")

def firststar(id_list: list) -> int:
    left_list = [int(id_list[x]) for x in range(len(id_list)) if x % 2 == 0]
    right_list = [int(id_list[x]) for x in range(len(id_list)) if x % 2 == 1]
    left_list.sort()
    right_list.sort()
    distance_sum = 0
    for i in range(len(left_list)):
        distance_sum += abs(left_list[i] - right_list[i])
    return distance_sum

print(firststar(day1puzzle))

def secondstar(id_list: list) -> int:
    left_list = [int(id_list[x]) for x in range(len(id_list)) if x % 2 == 0]
    right_list = [int(id_list[x]) for x in range(len(id_list)) if x % 2 == 1]
    similarity_score = 0
    for i in range(len(left_list)):
        similarity_score += left_list[i] * right_list.count(left_list[i])
    return similarity_score

print(secondstar(day1puzzle))
