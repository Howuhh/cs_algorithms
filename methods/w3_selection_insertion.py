
def insertion_sort(arr):
    arr = arr.copy()
    # каждый новый элемент просеиваем назад пока он меньше
    for i in range(1, len(arr)):
        j = i
        while (j > 0) and (arr[j] < arr[j - 1]):
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j = j - 1
    
    return arr


def selection_sort(arr):
    arr = arr.copy()
    # за каждый подход находим минимум и свапаем с первым -> улучшение == heapsort
    for i in range(len(arr)):
        min_idx = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        if arr[i] > arr[min_idx]:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


def buble_sort(arr):
    arr = arr.copy()

    # смотрим по два, если первые больше - меняем местами
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j - 1] > arr[j]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

    return arr


if __name__ == "__main__":
    test = [9, 8, 7, 6, 5, 3, 2, 1]

    print(selection_sort(test))
    print(buble_sort(test))
    print(insertion_sort(test))