import copy
a = {(1,2):3}
b = 0
c = [1,2,3,4,[5,6]]
d = [[[1,2,3],[5,89]],[[4,8]]]
e = copy.deepcopy(c)
c = 3
try:
    a[(1,3)] == 6
    b = 7
except:
    b = 1
print(3//2)