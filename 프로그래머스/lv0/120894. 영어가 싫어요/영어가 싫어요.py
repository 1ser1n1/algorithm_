def solution(numbers):
    numbers_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    answer = ""
    for i, num in enumerate(numbers_list):
        numbers = numbers.replace(num,str(i))
    return int(numbers)