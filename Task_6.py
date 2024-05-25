def greedy_algorithm(items, budget):
    items_sorted = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_cost = 0
    total_calories = 0
    selected_items = []

    for item, info in items_sorted:
        if total_cost + info['cost'] <= budget:
            selected_items.append(item)
            total_cost += info['cost']
            total_calories += info['calories']

    return selected_items, total_calories, total_cost


def dynamic_programming(items, budget):
    item_list = list(items.items())
    n = len(item_list)
    
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, info = item_list[i - 1]
        for w in range(1, budget + 1):
            if info['cost'] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - info['cost']] + info['calories'])
            else:
                dp[i][w] = dp[i - 1][w]

    w = budget
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name, info = item_list[i - 1]
            selected_items.append(name)
            w -= info['cost']

    return selected_items, dp[n][budget], budget - w


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 90
greedy_result = greedy_algorithm(items, budget)

print("Greedy Algorithm Result:")
print(f"Selected items: {greedy_result[0]}")
print(f"Total calories: {greedy_result[1]}")
print(f"Total cost: {greedy_result[2]}")

dp_result = dynamic_programming(items, budget)
print("\nDynamic Programming Algorithm Result:")
print(f"Selected items: {dp_result[0]}")
print(f"Total calories: {dp_result[1]}")
print(f"Total cost: {dp_result[2]}")