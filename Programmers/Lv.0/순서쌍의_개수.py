def solution(n):
    answer = 0

    for i in range(1, n+1):
        if n%i == 0 :
            answer += 1
    print(answer)
    return answer

solution(20)

# def solution(n):
#     return len(list(filter(lambda v: n % (v+1) == 0, range(n))))