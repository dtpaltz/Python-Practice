import numpy

def arrays(arr):
    float_list = list(map(lambda x: float(x), arr))
    print(float_list)


a = numpy.array([1,2,3,4,5])
print(a[1])          #2

b = numpy.array([1,2,3,4,5],float)
print(b[1])         #2.0




t_arr = ['1', '2', '3', '4', '-8', '-10']
arrays(t_arr)
