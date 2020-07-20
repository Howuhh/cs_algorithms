

def longest_playlist(songs):
    seen = {}
    max_playlist = 0

    start = 0
    for end, song in enumerate(songs):
        if song in seen:
            # start playlist from next char
            start = max(start, seen[song] + 1)
        
        seen[song] = end
        max_playlist = max(max_playlist, end - start + 1)

    return max_playlist
            

def main():
    n = input()
    playlist = [int(i) for i in input().split()]

    print(longest_playlist(playlist))


if __name__ == "__main__":
    main()