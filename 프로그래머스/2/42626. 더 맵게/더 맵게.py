import heapq

def solution(scoville, K):
    heapq.heapify(scoville)  # 일단 heap으로 바꾸기
    count = 0
    answer = -1  # 기본값으로 -1 설정 (목표 달성 불가능할 경우 반환)
    
    while len(scoville) > 1:  # 최소 2개 이상의 음식이 있을 때만 진행
        if scoville[0] >= K:  # 가장 작은 스코빌 지수가 K 이상이면
            answer = count  # 목표 달성, count 반환
            break
        # 두 개의 최소값을 뽑아 새로운 음식을 만들기
        min_1 = heapq.heappop(scoville)
        min_2 = heapq.heappop(scoville)
        mix = min_1 + min_2 * 2
        heapq.heappush(scoville, mix)  # 새로 만든 음식을 다시 힙에 추가
        count += 1
    
    # 마지막 남은 하나의 음식의 스코빌 지수가 K 이상인지 확인
    if scoville[0] >= K:
        answer = count
    # answer이 기본값 -1인 경우는 목표를 달성할 수 없는 경우

    return answer
