def solution(lottos, win_nums):  #lottos: 산거, win_nums: 정답
    
    
    # 같은거 개수
    count_win = 0
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            count_win += 1
            win_nums.remove(lottos[i])
        
    
    
    #0의 개수
    count_0 = 0
    for i in range(len(lottos)):
        if lottos[i] == 0:
            count_0 += 1

            
    #2개 일치 -> 5등 : count_win
    #4개 일치 -> 4등 : count_win+count_0
    #개수가 key, 등수가 value
    dict_num = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    num1 = dict_num[(count_win+count_0)]
    num2 = dict_num[count_win]
    
    answer = [num1, num2]

    return answer