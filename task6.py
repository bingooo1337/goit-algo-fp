budget = 100
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(),
        key=lambda a: a[1]["calories"] / a[1]["cost"],
        reverse=True
    )

    total_calories = 0
    total_cost = 0
    selected_items = []

    for item, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            total_cost += info["cost"]
            total_calories += info["calories"]
            selected_items.append(item)

    return selected_items, total_calories


selected_items, total_calories = greedy_algorithm(items, budget)
print(f"Greedy:")
print(f"Selected items - {selected_items}")
print(f"Total calories - {total_calories}")
print()


def dynamic_programming(items, budget):
    n = len(items)
    item_list = list(items.items())
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        item, info = item_list[i - 1]
        cost = info["cost"]
        calories = info["calories"]

        for w in range(budget + 1):
            if w >= cost:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item, _ = item_list[i - 1]
            selected_items.append(item)
            w -= items[item]["cost"]

    total_calories = dp[n][budget]

    return selected_items, total_calories


selected_items, total_calories = dynamic_programming(items, budget)
print(f"Dynamic:")
print(f"Selected items - {selected_items}")
print(f"Total calories - {total_calories}")
