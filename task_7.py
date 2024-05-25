import random
import matplotlib.pyplot as plt

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def simulate_dice_rolls(num_rolls):
    sums = {i: 0 for i in range(2, 13)}
    for _ in range(num_rolls):
        die1, die2 = roll_dice()
        dice_sum = die1 + die2
        sums[dice_sum] += 1
    return sums

def calculate_probabilities(sums, num_rolls):
    probabilities = {sum_: count / num_rolls for sum_, count in sums.items()}
    return probabilities

def main():
    num_rolls = 1000000
    sums = simulate_dice_rolls(num_rolls)
    probabilities = calculate_probabilities(sums, num_rolls)
    
    analytical_probabilities = {
        2: 1/36,
        3: 2/36,
        4: 3/36,
        5: 4/36,
        6: 5/36,
        7: 6/36,
        8: 5/36,
        9: 4/36,
        10: 3/36,
        11: 2/36,
        12: 1/36
    }

    # Відображення результатів
    print("Сума\tІмовірність (симуляція)\tІмовірність (аналітична)")
    for sum_ in range(2, 13):
        sim_prob = probabilities[sum_] * 100
        anal_prob = analytical_probabilities[sum_] * 100
        print(f"{sum_}\t{sim_prob:.2f}%\t\t\t{anal_prob:.2f}%")
    
    # Графік ймовірностей
    sums_list = list(range(2, 13))
    sim_probs = [probabilities[sum_] * 100 for sum_ in sums_list]
    anal_probs = [analytical_probabilities[sum_] * 100 for sum_ in sums_list]

    plt.figure(figsize=(10, 6))
    plt.bar(sums_list, sim_probs, alpha=0.7, label='Симуляція', color='blue')
    plt.plot(sums_list, anal_probs, marker='o', linestyle='-', color='red', label='Аналітична')
    plt.xlabel('Сума')
    plt.ylabel('Імовірність (%)')
    plt.title('Ймовірності сум при киданні двох кубиків')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
