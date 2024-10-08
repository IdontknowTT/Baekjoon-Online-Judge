def solution(brown, yellow):
    
    #일단 yellow 가지고 소인수분해 해야함
    #소인수 분해 결과 가로*세로 해서 나오는데 - 가로가 세로보다 크거나 같아야함
    
    #1. 추가 - 세로 
    lst = []
    for i in range(1,yellow+1):  #범위 조심하기(yellow까지 꼭 해줘야 함)
        if yellow%i==0:
            lst.append(i)   #yellow를 나누는 i 모두 a추가

    
    ans_lst = []
    #2. 가로 세로 사용해서 만들어주기, 크기 조절해주기
    for i in range(len(lst)):
        tmp = yellow//lst[i]
        if lst[i]<=tmp:  #세로<=가로 면
            ans_lst.append((lst[i],tmp)) #세로, 가로 - 저장해주기
        
    
    
    #3. 이제 ans_lst에서 하나씩 받아가지고 *2, *2, +4 한게 brown 개수랑 같아지면 그게 yellow의 세로 가로 이다
    for ans in (ans_lst):
        x,y = ans
        if (x*2+y*2+4) == brown:
            break
    
    answer = [y+2, x+2]
    

    return answer