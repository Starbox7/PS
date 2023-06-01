def solution(my_string):
    answer = ''

    for i in my_string:
        if i!='a' and i!='e' and i!='i' and i!='o' and i!='u':
            answer = answer+i
    print(answer)


    return answer

solution('nice to meet you')


# def solution(my_string):
#     return "".join([i for i in my_string if not(i in "aeiou")])