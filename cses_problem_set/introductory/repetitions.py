
def max_substr(string):
    max_sub = 1

    sub_len = 1
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            sub_len += 1
        else:
            sub_len = 1
        max_sub = max(max_sub, sub_len)

    return max_sub


def main():
    string = input()
    
    print(max_substr(string))


if __name__ == "__main__":
    main()