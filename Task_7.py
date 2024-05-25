import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(n_rolls):
    sums_count = {i: 0 for i in range(2, 13)}
    
    for _ in range(n_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice_sum = dice1 + dice2
        sums_count[dice_sum] += 1
    
    probabilities = {sum_val: count / n_rolls for sum_val, count in sums_count.items()}
    return probabilities

def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())
    
    plt.bar(sums, probs, tick_label=sums)
    plt.xlabel('Сума')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірності сум при киданні двох кубиків (Метод Монте-Карло)')
    plt.show()

def main():
    n_rolls = 1000000 
    probabilities = simulate_dice_rolls(n_rolls)
    
    analytical_probabilities = {
        2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 
        7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
    }
    
    print("| Сума | Ймовірність (Монте-Карло) | Ймовірність (Аналітична)  |")
    print("|------|---------------------------|---------------------------|")
    for sum_val in range(2, 13):
        print(f"| {sum_val:<4} | {probabilities[sum_val]:<25.2%} | {analytical_probabilities[sum_val]:<25.2%} |")
    
    plot_probabilities(probabilities)

if __name__ == "__main__":
    main()