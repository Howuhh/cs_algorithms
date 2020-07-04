
N = 7

# works but slow, so not solved 
def count_paths(pattern):
    visited = [[False] * N for _ in range(N)]
    moves = {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0, -1)}

    def _dfs(x, y, step, move):
        if x == (N - 1) and y == 0:
            if step == (N**2 - 1):
                return 1
            return 0


        # WTF is this....anyway runtime error with python
        if ((move == 'L' and (y == 0 or visited[x][y-1]) and 0 < x < 6 and not visited[x-1][y] and not visited[x+1][y]) or
            (move == 'R' and (y == 6 or visited[x][y+1]) and 0 < x < 6 and not visited[x-1][y] and not visited[x+1][y]) or
            (move == 'U' and (x == 0 or visited[x-1][y]) and 0 < y < 6 and not visited[x][y-1] and not visited[x][y+1]) or
            (move == 'D' and (x == 6 or visited[x+1][y]) and 0 < y < 6 and not visited[x][y-1] and not visited[x][y+1])): 
            return 0

        pattern_move, path_count = pattern[step], 0
        
        if pattern_move != '?':
            x_move, y_move = moves[pattern_move]
            x_p, y_p = x + x_move, y + y_move
            
            if (x_p < 0 or x_p >= N) or (y_p < 0 or y_p >= N) or visited[x_p][y_p]:
                return 0

            visited[x_p][y_p] = True
            path_count += _dfs(x_p, y_p, step + 1, pattern_move)
            visited[x_p][y_p] = False
        else:
            for move in moves:
                x_move, y_move = moves[move]
                x_p, y_p = x + x_move, y + y_move

                if (x_p < 0 or x_p >= N) or (y_p < 0 or y_p >= N) or visited[x_p][y_p]:
                    continue

                visited[x_p][y_p] = True
                path_count += _dfs(x_p, y_p, step + 1, move) 
                visited[x_p][y_p] = False 
        
        return path_count

    visited[0][0] = True
    return _dfs(0, 0, 0, 0)


def main():
    pattern = input()
    paths = count_paths(pattern) # "?"* (N**2 - 1)
    # print(f"N: {N}, Paths: {paths}")
    print(paths)


if __name__ == "__main__":
    main()