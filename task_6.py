items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items: dict, budget: int):
    # Створюємо список з предметів з додатковими полями для "калорії/вартість" відношення
    item_list = []
    for name, info in items.items():
        cost = info["cost"]
        calories = info["calories"]
        ratio = calories / cost
        item_list.append((name, cost, calories, ratio))
    
    # Сортуємо список предметів за "калорії/вартість" відношенням у порядку спадання
    item_list.sort(key=lambda x: x[3], reverse=True)
    
    total_cost = 0
    total_calories = 0
    selected_items = []
    
    for item in item_list:
        name, cost, calories, ratio = item
        if total_cost + cost <= budget:
            total_cost += cost
            total_calories += calories
            selected_items.append(name)
        else:
            break
    
    return selected_items, total_cost, total_calories

# Приклад використання
budget = 100
selected_items, total_cost, total_calories = greedy_algorithm(items, budget)
print(f"Вибрані предмети: {selected_items}")
print(f"Загальна вартість: {total_cost}")
print(f"Загальна кількість калорій: {total_calories}")

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def dynamic_programming(items: dict, budget: int):
    # Перетворюємо словник в список для зручності роботи з індексами
    item_list = list(items.items())
    n = len(item_list)
    
    # Створюємо DP таблицю
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    # Заповнюємо DP таблицю
    for i in range(1, n + 1):
        item_name, info = item_list[i - 1]
        cost = info["cost"]
        calories = info["calories"]
        for j in range(budget + 1):
            if cost <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + calories)
            else:
                dp[i][j] = dp[i - 1][j]
    
    # Відновлюємо вибрані предмети
    selected_items = []
    total_cost = 0
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item_name, info = item_list[i - 1]
            selected_items.append(item_name)
            total_cost += info["cost"]
            w -= info["cost"]
    
    selected_items.reverse()
    total_calories = dp[n][budget]
    
    return selected_items, total_cost, total_calories

# Приклад використання
budget = 100
selected_items, total_cost, total_calories = dynamic_programming(items, budget)
print(f"Вибрані предмети: {selected_items}")
print(f"Загальна вартість: {total_cost}")
print(f"Загальна кількість калорій: {total_calories}")
