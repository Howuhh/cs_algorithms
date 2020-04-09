import math
import heapq
import sys

from copy import deepcopy
from math import inf
from bisect import bisect_left
from collections import defaultdict

def triangle_area(a, b, c):
    "area by Heron's formula"
    s = (a + b + c) / 2
    area = math.sqrt(s*(s - a)*(s - b)*(s - c))

    return area


def series_sum(n):
    s_sum = 0
    for i in range(1, n + 1):
        s_sum += (1/i**2)
    return s_sum


def fractional_part(num):
    return round(num % math.floor(num), 4)


def fractional_part2(num):
    print(math.floor(num), round(num % math.floor(num), 2) * 100)


def rus_round(num):
    if fractional_part(num) >= 0.5:
        return math.ceil(num)
    else:
        return math.floor(num)


def solve_quadratic(a, b, c):
    d = b**2 - 4*a*c
    if d >= 0:
        x1 = (- b + math.sqrt(d)) / 2*a
        x2 = (- b - math.sqrt(d)) / 2*a
        return (x1, x2) if x1 != x2 else x1


def solve_linear(a, b, c, d, e, f):
    "2x2 cramer"
    delta = a * d - c * b

    if delta != 0:
        delta_x = e * d - f * b
        delta_y = a * f - c * e
        return (delta_x / delta), (delta_y / delta)


def del_between_h(string):
    return string[:string.find("h")] + string[string.rfind("h") + 1:]
    

def find_second_f(string):
    first = string.find("f")

    if first < 0:
        return -2
    else:
        second = string.find("f", first + 1)
        return second if second >= 0 else -1


def swap_words(string):
    return " ".join(string.split()[::-1])


def only_two_min(a, b, c, d):
    return min(a, min(b, min(c, d)))


def IsPointInSquare(x, y):
    "square in (1,1), (-1, 1), (-1, -1), (1, -1)"
    return abs(x) <= 1 and abs(y) <= 1


def IsPointInCircle(x, y, xc, yc, r):
    return (x - xc)**2 + (y - yc)**2 <= r**2


def MinDivisor(n):
    "at least one divisor should be <= sqrt(n)"
    div = 2
    while div <= math.sqrt(n):
        if n % div == 0:
            return div
        div += 1

    return n


def isPrime(n):
    return MinDivisor(n) == n


def power(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a
    else:
        return a * power(a, n - 1)


def sum_rec(a, b):
    if b == 0:
        return a
    else:
        return sum_rec(a + 1, b - 1)


def fast_pow(a, n):
    if n == 1:
        return a
    if n == 0:
        return 1

    if n % 2 == 0:
        return fast_pow(a**2, n / 2)
    else:
        return a * fast_pow(a, n - 1)


def ReduceFraction(n, m):
    def gcd(n, m):
        if n == 0 or m == 0:
            return max(n, m)
        if n > m:
            return gcd(n % m, m)
        else:
            return gcd(n, m % n)

    gcd_ = gcd(n, m)
    return n / gcd_, m / gcd_


def sum_rec_noloop(acc=0):
    new_n = int(input())
    if new_n == 0:
        return acc
    else:
        return sum_rec_noloop(acc + new_n)


def reverse_seq_rec(n=0):
    n = int(input())
    if n == 0:
        print(n)
        return
    reverse_seq_rec()
    print(n) 


def last_max(arr):
    curr_max, idx = -math.inf, None
    for i, el in enumerate(arr):
        if el > curr_max:
            curr_max, idx = el, i
    return curr_max, idx


def merge(arr1, arr2):
    merged = []

    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    if i < len(arr1):
        [merged.append(arr1[k]) for k in range(i, len(arr1))]
    
    if j < len(arr2):
        [merged.append(arr2[k]) for k in range(j, len(arr2))]

    return merged


def max_users(users, disk_space):
    users = sorted(users)

    max_user = 0
    for user in users:
        disk_space -= user
        if disk_space <= 0:
            break
        max_user += 1
    return max_user


def nearest_bomb_shelter_nlogn(cities, shelters):
    shelters = sorted([(v, i) for i, v in enumerate(shelters)])
    nearests, n = [], len(shelters)

    for city in cities: 
        idx = bisect_left(shelters, (city, inf))

        before = (inf, inf) if idx - 1 < 0 else (abs(city - shelters[idx - 1][0]), idx - 1)
        on = (abs(city - shelters[idx][0]), idx) if idx < n else (inf, inf)
        after = (inf, inf) if idx + 1 >= n else (abs(city - shelters[idx + 1][0]), idx + 1)

        nearests.append(shelters[min(before, on, after)[1]][1] + 1)

    return nearests


def nearest_bomb_shelter_naive(cities, shelters):
    cities = sorted([(v, i) for i, v in enumerate(cities)])
    shelters = sorted([(v, i) for i, v in enumerate(shelters)])

    nearest = [None] * len(cities) 

    prev_shelter = 0
    for city, c_id in cities:
        curr_min = inf
        for j in range(prev_shelter, len(shelters)):
            shelter, s_id = shelters[j]

            diff = abs(city - shelter)
            if diff > curr_min: 
                break

            curr_min = diff
            nearest[c_id] = s_id + 1
            prev_shelter = j

    return nearest


def CountSort(arr, buffer=100):
    counts = [0] * buffer
    new_arr = [None] * len(arr)

    for el in arr:
        counts[el] += 1

    for i in range(1, len(counts)):
        counts[i] = counts[i - 1] + counts[i]

    print(counts)
    for el in arr:
        new_arr[counts[el] - 1] = el
        counts[el] -= 1

    return new_arr


def uni_passing_score(scores, k):
    counts = defaultdict(lambda: 0)

    for score in scores:
        counts[score] += 1
    
    scores, top_scores = sorted(scores, reverse=True), []

    for score in scores:
        if len(top_scores) + counts[score] > k:
            break
        top_scores.append(score)
        counts[score] -= 1

    return top_scores[-1]


def count_strings(word_arr):
    counts = defaultdict(lambda: 0)
    for word in word_arr:
        counts[word] += 1

    return sorted(counts, key=counts.get, reverse=True)


def transpose(matrix):
    t_matrix = [[None] * len(matrix) for _ in range(len(matrix[0]))]

    for i, row in enumerate(matrix):
        for j, _ in enumerate(row):
            t_matrix[j][i] = matrix[i][j]

    return t_matrix


def print_matrix(matrix):
    for row in matrix:
        print(row)


def main():
    test = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    t_test = transpose(test)

    print_matrix(test)
    print_matrix(t_test)

    # print(transpose(test))


if __name__ == "__main__":
    main()