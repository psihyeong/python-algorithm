import math

# 시간 문자열을 정수분으로 변환해주는 함수
def timeToVal(string):
    hh, mm = int(string[:2]), int(string[3:])
    
    return 60*hh + mm

# 요금 계산 함수
def feesCal(fees, m):
    basic_m, basic_cost, unit_time, unit_cost = fees[0], fees[1], fees[2], fees[3]
    m -= basic_m
    if m < 0:
        m = 0
    return basic_cost + math.ceil(m/unit_time)*unit_cost



def solution(fees, records):
    answer = []
    
    parking_time = {}       # 차량별 총 주차시간을 담는 해시
    
    temp = {}               # 차량의 1회 입출차를 임시로 기록하는 해시
    
    for string in records:
        time, number, status = map(str,string.split())
        
        if status == "IN":          # 입차 시간 기록
            temp[number] = timeToVal(time)
            
        elif status == "OUT":
            parking = timeToVal(time) - temp[number]    # 출차 시 주차시간 계산 
            temp[number] = -1            # 23:59까지 출차하지 않은 차를 확인하기 위한 -1
            
            if number not in parking_time:              # 총 주차시간 갱신
                parking_time[number] = parking
            else:
                parking_time[number] += parking
                
    for key, val in temp.items():               # 23:59까지 안나간 차량 확인
        if val >= 0:
            parking = 23*60 + 59 - val
            if key not in parking_time:         # 총 주차시간 갱신
                parking_time[key] = parking
            else:
                parking_time[key] += parking
                
    for key, val in parking_time.items():       # 요금 계산
        parking_time[key] = feesCal(fees,val)
    
    parking_time = sorted(parking_time.items(), key = lambda x : x[0])
    
    for key, val in parking_time:
        answer.append(val)
            
    return answer
