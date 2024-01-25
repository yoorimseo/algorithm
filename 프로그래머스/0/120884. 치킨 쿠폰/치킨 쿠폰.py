def solution(chicken):
    coupon = chicken
    service = answer = 0

    while coupon >= 10:
        service = coupon // 10
        coupon = (coupon % 10) + service
        answer += service
        
    return answer