def solution(price):
    answer = 0

    if price >= 500000 :
        answer = (price/5)*4
    elif price >= 300000 : 
        answer = (price/10)*9
    elif price >= 100000 :
        answer = (price/20)*19
    else :
        answer = price

    answer = int(answer)

    return answer


# def solution(price):
#     discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
#     for discount_price, discount_rate in discount_rates.items():
#         if price >= discount_price:
#             return int(price * discount_rate)