def solution(num_list):
    sum = 0
    mul = 1
    for i in num_list:
        sum += i
        mul *= i
    sum *= sum
    if sum > mul :
        return 1
    else : 
        return 0
    


# def solution(num_list):
#     s=sum(num_list)**2
#     m=eval('*'.join([str(n) for n in num_list]))
#     return 1 if s>m else 0