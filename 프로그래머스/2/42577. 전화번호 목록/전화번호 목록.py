def solution(phone_book):
    
    phone_book.sort() #먼저 정렬해준다 -> 그럼 다음게 내거의 접두어는 절대 될 수 없어 = 내가 다음거 접두사가 아니면 걍 끝
    
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]): #나 다음게 나로 시작한다면
            answer = False
            break
        answer = True
    

    return answer