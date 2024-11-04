def solution(todo_list, finished):
    answer = []
    for i in range(len(todo_list)):
        if finished[i] == False:
            answer.append(todo_list[i])
        else:
            pass
    return answer