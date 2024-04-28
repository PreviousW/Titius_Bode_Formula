def defining_distances(index: int):
    return 0.4 + (0.3 * (2 ** index)) # a = 0.4 + (0.3 * 2^n)

def god(index):
    if index == -1:
        return 0.4 # 수성
    else: 
        return defining_distances(index)

index_of_planets = {
    "Mercury": -1,
    "Venus": 0,
    "Earth": 1,
    "Mars": 2,
    # "Ceres": 3 소행성대에 있는 가장 큰 소행성이라 제외. 
    "Jupiter": 4,
    "Saturn": 5,
    "Uranus": 6,
    # "Neptune": 7 해왕성 부터는 정확도 급감 (만족 X) 으로 인해 제외
}

def main():
    for planets, index in index_of_planets.items():
        print(f"{planets} | {round(god(index), 2)}AU.")
main()
