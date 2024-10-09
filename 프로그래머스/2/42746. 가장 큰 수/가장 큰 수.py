def solution(numbers):
    # 숫자를 문자열로 변환
    numbers = list(map(str, numbers))
    
    # 두 숫자를 붙였을 때 더 큰 순서로 정렬
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    # 정렬된 숫자들을 이어 붙임
    answer = ''.join(numbers)
    
    # '000' 같은 경우를 처리하기 위해 int로 변환 후 다시 문자열로 변환
    return str((int(answer)))
