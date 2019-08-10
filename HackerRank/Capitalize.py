



def solve(s):
    arr = s.split(' ')

    for x in arr[:]:
        s = s.replace(x, x.capitalize())
        print(s)

    for i in range(len(arr)):
        arr[i] = arr[i].capitalize()

    #print(arr[0], arr[1], ' ')


solve('dustin paltz')
