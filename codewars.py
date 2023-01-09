def array_diff(a, b):
    c = []
    if len(b) == 1:
        for i in a:
            if b == []:
                c = a
            for j in b:
                if i != j:
                    c.append(i)
        print(c)
    else:
        for i in a[:]:
            if i in b:
                a.remove(i)
        print(a)



array_diff([1, 2], [1])
array_diff([1,2,2,2,3],[2])
array_diff([1,2,2], [])
array_diff([1,2,3], [1, 2])