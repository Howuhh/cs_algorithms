
# TODO: wrong answer
def longest_playlist(songs):
    series, max_count = dict(), 0

    count = 0
    for idx, song in enumerate(songs):
        if song in series:
            count = abs(idx - series[song])
        else:
            count += 1
        
        series[song] = idx
        max_count = max(max_count, count)

    return max_count
            

def main():
    n = input()
    playlist = [int(i) for i in input().split()]

    print(longest_playlist(playlist))


if __name__ == "__main__":
    main()