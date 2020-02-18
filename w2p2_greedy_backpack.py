from utils import to_int

# набиваем рюкзак предметами с максимальной стоимостью за обьем (c/w)
def get_max_backpack_value(max_space: int, costs: list) -> float:
    sorted_costs = sorted(costs, key=lambda cost: (cost[0] / cost[1]))  # O(nlogn)

    total_cost = 0.0
    while max_space > 0:  # O(n)
        if len(sorted_costs) == 0:
            break
        
        cost, volume = sorted_costs.pop()  # O(1)
        if volume <= max_space:
            max_space -= volume
            total_cost += cost
        else:
            total_cost += (max_space / volume) * cost
            max_space = 0

    return total_cost  # O(nlogn) + O(n) = O(nlogn)


if __name__ == "__main__":
    n, W = map(int, input().split())
    costs = [to_int(input().split()) for _ in range(n)]
    
    max_value = round(get_max_backpack_value(W, costs), 3)
    print(max_value)
