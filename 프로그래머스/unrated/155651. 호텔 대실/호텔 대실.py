import heapq

# 시각을 정수 분으로 바꿔주는 함수
def change(time):   
    hh, mm = int(time[:2]), int(time[3:])

    return 60*hh+mm
        

def solution(book_time):
    book_time.sort(key = lambda x: x[0])    # 대실 시작 시각 기준 오름차순 정렬
    hotel = []                              # 방별, 대실 종료 시각을 기준으로 오름차순 정렬되는 배열
    answer = 1                              
    heapq.heappush(hotel,change(book_time[0][1])+10)   # 첫번째 예약을 받고 시작
    
    
    for i in range(1, len(book_time)):
        s_time, e_time = change(book_time[i][0]), change(book_time[i][1])   # 두번째 예약의 시작, 종료 시각부터
        
        if s_time >= hotel[0]:              # 방을 이어 받을 수 있는 경우
            heapq.heappop(hotel)            # 대실 종료 시각이 가장 빠른 방 빼기
        else:                               # 새로운 방을 받아야하는 경우
            answer += 1                     # 방 추가
            
        heapq.heappush(hotel,e_time+10)     # 방별 대실 종료 시각 갱신
    
    return answer