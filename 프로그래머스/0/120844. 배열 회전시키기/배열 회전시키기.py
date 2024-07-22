def solution(numbers, direction):
    if direction == "right":
        a = numbers[-1]
        numbers.remove(numbers[-1])
        numbers.insert(0, a)
    else:
        a = numbers[0]
        numbers.remove(numbers[0])
        numbers.append(a)
    return numbers