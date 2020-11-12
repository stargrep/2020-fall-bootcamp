# Assignment 1 Answers


# Q1
def is_prime(n):
    if n <= 1:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


def test_is_prime():
    print("1. test is_prime()")
    assert not is_prime(1)
    assert is_prime(97)
    assert not is_prime(91)
    assert not is_prime(0)
    assert is_prime(114643)
    print("1. all passed\n")


# Q2
def rotate(ar, d):
    d = d % len(ar)
    inplace_reverse(ar, 0, d - 1)
    inplace_reverse(ar, d, len(ar) - 1)
    inplace_reverse(ar, 0, len(ar) - 1)
    return ar


def inplace_reverse(ar, start, end):
    while start < end:
        ar[start], ar[end] = ar[end], ar[start]
        start += 1
        end -= 1


def test_rotate():
    print("2. test rotate()")
    print(rotate([1, 2, 3, 4, 5], 10))
    assert rotate([1, 2, 3, 4, 5], 0) == [1, 2, 3, 4, 5]
    assert rotate([1, 2, 3, 4, 5], 1) == [2, 3, 4, 5, 1]
    assert rotate([1, 2, 3, 4, 5], 3) == [4, 5, 1, 2, 3]
    assert rotate([1, 2, 3, 4, 5], 7) == [3, 4, 5, 1, 2]
    assert rotate([1, 2, 3, 4, 5], 9) == [5, 1, 2, 3, 4]
    print("2. tests passed \n")


# Q3
def selection_sort(students):
    for i in range(len(students)):
        min_idx = i
        for j in range(i + 1, len(students)):
            if students[min_idx][1] > students[j][1]:
                min_idx = j
        students[i], students[min_idx] = students[min_idx], students[i]
    return students


def test_selection_sort():
    print("3. test selection_sort()")
    assert selection_sort([]) == []
    assert selection_sort([[1, 100], [2, 70], [3, 95], [4, 66], [5, 98]]) == \
           [[4, 66], [2, 70], [3, 95], [5, 98], [1, 100]]
    print("3. all tests passed")


# Q4
def convert(tup, di):
    for i in range(0, len(tup), 2):
        di[tup[i]] = tup[i + 1]


def test_convert():
    print("4. test convert()")
    expected_dict = {}
    convert(('key1', 'val1', 'key2', 'val2', 'k', 'v'), expected_dict)
    print(expected_dict)
    assert expected_dict == {'key1': 'val1', 'key2': 'val2', 'k': 'v'}
    print("4. all tested")


if __name__ == '__main__':
    test_is_prime()
    test_rotate()
    test_selection_sort()
    test_convert()
