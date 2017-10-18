__author__ = 'Xazlin'


def test():
    array = [[3872, -912],[3872, -912],[3874, -922],[3874, -922],[3874, -912],[3883, -909],[3883, -909],[3883, -909]]

    print findgroups(array)


def findgroups(array):
    seen = []
    seen2 = []
    index = []
    result = []

    for i in array:
        if i[1] not in seen:
            seen.append(i[1])
            seen2.append(i)

    for i in seen2:
        index.append(array.index(i))

    print index

    for i in range(len(index)):
        current = index[i]
        last = len(array)
        if i != len(index)-1:
            last = index[i+1]-1
        if current != last:
            result.append([current, last])

    return result

test()