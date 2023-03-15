import math

def timeToVal(string):
    hh, mm = int(string[:2]), int(string[3:])
    
    return 60*hh + mm

def feesCal(fees, m):
    basic_m, basic_cost, unit_time, unit_cost = fees[0], fees[1], fees[2], fees[3]
    m -= basic_m
    if m < 0:
        m = 0
    
    return basic_cost + math.ceil(m/unit_time)*unit_cost

def solution(fees, records):
    answer = []
    
    parking_time = {}
    
    temp = {}
    
    for string in records:
        time, number, status = map(str,string.split())
        if status == "IN":
            temp[number] = timeToVal(time)
        elif status == "OUT":
            parking = timeToVal(time) - temp[number]
            temp[number] = -1
            if number not in parking_time:
                parking_time[number] = parking
            else:
                parking_time[number] += parking
                
    for key, val in temp.items():
        if val >= 0:
            parking = 23*60 + 59 - val
            if key not in parking_time:
                parking_time[key] = parking
            else:
                parking_time[key] += parking
                
    for key, val in parking_time.items():
        parking_time[key] = feesCal(fees,val)
    
    parking_time = sorted(parking_time.items(), key = lambda x : x[0])
    
    for key, val in parking_time:
        answer.append(val)
            
    return answer