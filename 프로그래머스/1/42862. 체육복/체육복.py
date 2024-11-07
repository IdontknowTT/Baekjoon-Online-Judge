def solution(n, lost, reserve):
    
    count = 0
    
    # lost 중에 reserve 있나 확인
    lost_copy = lost[:]
    reserve_copy = reserve[:]
    print(lost_copy)
    
    for l in lost_copy:
        print(l)
        if l in reserve_copy:
            reserve.remove(l)
            lost.remove(l)
            print(reserve, lost)
    
    reserve.sort()
    lost.sort()
    for l in lost: # 모든 lost 탐색
        
        if (l-1) in reserve: # resrve에서 뒤져 앞에 애 있나
            reserve.pop(reserve.index(l-1)) # 뺀다
            count += 1
            continue
            
        elif (l+1) in reserve: # resrve에서 뒤져 앞에 애 있나
            reserve.pop(reserve.index(l+1)) # 뺀다
            count += 1
        
    
    answer = n-len(lost)+count

    return answer