

#  main idea: maintain space pointers and replace
def remove_spaces(char_arr):  # O(n) and inplace
    space_idx = 0
    for i in range(len(char_arr)):
        if char_arr[i] != " ":
            char_arr[space_idx], char_arr[i] = char_arr[i], char_arr[space_idx]
            space_idx += 1

            # если конец слова, то прибавить один пробел
            if char_arr[i + 1] == " ":
                space_idx += 1

    return char_arr[:space_idx - 1]


def main():
    string = list(input())
    print(f"BEFORE:{''.join(string)}")
    print(f"REMOVED:{''.join(remove_spaces(string))}")


if __name__ == "__main__":
    main()