def solution(my_string, letter):
    answer = ''
    for i in my_string:
        if i != letter:
            answer += i
    return answer


# def solution(my_string, letter):
#     return my_string.replace(letter, '')