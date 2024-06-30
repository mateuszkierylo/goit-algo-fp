def greedy_algorithm(items, budget):
    # Calculate the ratio of calories to cost
    item_ratios = [(name, info['calories'] / info['cost']) for name, info in items.items()]
    # Sort items by their calorie to cost ratio in descending order
    item_ratios.sort(key=lambda x: x[1], reverse=True)
    
    total_cost = 0
    selected_items = []
    
    for name, ratio in item_ratios:
        cost = items[name]['cost']
        if total_cost + cost <= budget:
            selected_items.append(name)
            total_cost += cost
    
    return selected_items

def dynamic_programming(items, budget):
    item_names = list(items.keys())
    num_items = len(item_names)
    
    # Create a table to store the maximum calories for each budget
    dp = [[0] * (budget + 1) for _ in range(num_items + 1)]
    
    # Fill the table
    for i in range(1, num_items + 1):
        for b in range(budget + 1):
            item_name = item_names[i - 1]
            item_cost = items[item_name]['cost']
            item_calories = items[item_name]['calories']
            
            if item_cost <= b:
                dp[i][b] = max(dp[i-1][b], dp[i-1][b - item_cost] + item_calories)
            else:
                dp[i][b] = dp[i-1][b]
    
    # Trace back to find the items included
    selected_items = []
    b = budget
    for i in range(num_items, 0, -1):
        if dp[i][b] != dp[i-1][b]:
            item_name = item_names[i - 1]
            selected_items.append(item_name)
            b -= items[item_name]['cost']
    
    return selected_items

# Example usage
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

greedy_selection = greedy_algorithm(items, budget)
dp_selection = dynamic_programming(items, budget)

print("Greedy Algorithm Selection:", greedy_selection)
print("Dynamic Programming Selection:", dp_selection)
