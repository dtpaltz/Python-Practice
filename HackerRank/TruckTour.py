

def truckTour(petrolpumps):
    petrol = -1
    start = 0
    n = len(petrolpumps)

    for i in range(n):
        if petrol > -1:
            petrol += petrolpumps[i][0] - petrolpumps[i][1]
        else:
            petrol = petrolpumps[i][0] - petrolpumps[i][1]
            start = i

    return start





a1 = [[1, 5], [10, 3], [3, 4]]
print(truckTour(a1))

