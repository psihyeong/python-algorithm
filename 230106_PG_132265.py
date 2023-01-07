# 프로그래머스 132265번 롤케이크 자르기

def solution(topping):
    answer = 0
    hash = {}       # 동생의 토핑 정보를 담는 해시

    # 최초 모든 롤케이크는 동생의 것.
    for i in topping:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1

    opp_set = set()     # 형의 토핑 정보를 담는 집합
    for i in topping:   # 롤케이크 자르기
        hash[i] -= 1
        opp_set.add(i)  # 형의 토핑 정보는 집합으로 처리하면서 중복을 제거.
        if hash[i] == 0:    # 한 종류의 토핑을 모두 형에게 줬으면 해시에서 pop
            hash.pop(i)

        if len(hash) == len(opp_set):   # 공평할 경우
            answer += 1

    return answer

# 시간복잡도 해결을 위해 해시와 집합, 두 가지 자료구조를 사용하는 방법도 염두하자.