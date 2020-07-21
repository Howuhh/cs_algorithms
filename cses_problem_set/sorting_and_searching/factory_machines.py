
# Idea: solve an inverse problem: given time x is it possible to produce at least t products?
# solution: time = 8, then total_products = (8 // 4) + (8 // 3) + (8 // 5) (for times 2 3 5)
def min_prod_time(machines, goal_products):
    left, right = 0, 1e18

    while left <= right:
        mid_time = (left + right) // 2

        max_products = 0
        for machine in machines:
            max_products += (mid_time // machine)

        if max_products < goal_products:
            left = int(mid_time) + 1
        else:
            right = int(mid_time) - 1 
            
    return int(left)


def main():
    n, t = map(int, input().split())
    machines = [int(i) for i in input().split()]

    print(min_prod_time(machines, t))


if __name__ == "__main__":
    main()