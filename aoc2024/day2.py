import re

def day2data(filename: str) -> list:
    with open(filename) as text_input:
        input_list = text_input.read().strip().split('\n')
        input_list = list(map(str, input_list))
        input_list = [list(map(int, x.split(' '))) for x in input_list]
        return input_list

day2puzzle = day2data("day2input.txt")

def firststarcheck(report: list) -> int:
    step_sum = 0
    actual_step = abs(report[len(report)-1] - report[0])
    for i in range(len(report)-1):
        step = abs(report[i] - report[i+1])
        if step > 3 or step < 1:
            return 0
        else:
            step_sum += step
    if step_sum == actual_step:
        return 1
    else:
        return 0
        
def firststar(reports: list) -> int:
    safe_reports = 0
    for report in reports:
        safe_reports += firststarcheck(report)
    return safe_reports

print(firststar(day2puzzle))

def secondstarcheck(report: list) -> int:
    if firststarcheck(report) == 1:
        return 1
    else:
        safe_combination = 0
        for i in range(len(report)):
            tmp_report = [n for n in report]
            tmp_report.pop(i)
            safe_combination += firststarcheck(tmp_report)
        if safe_combination >= 1:
            return 1
        else:
            return 0
    
def secondstar(reports: list) -> int:
    safe_reports = 0
    for report in reports:
        safe_reports += secondstarcheck(report)
    return safe_reports

print(secondstar(day2puzzle))