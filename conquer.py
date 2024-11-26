import random

def classify_numbers(numbers):
    if len(numbers) == 1:
        return ["low" if numbers[0] < 50 else "high"]
    
    mid = len(numbers) // 2
    left_part = numbers[:mid]
    right_part = numbers[mid:]
    
    left_classification = classify_numbers(left_part)
    right_classification = classify_numbers(right_part)
    
    return left_classification + right_classification

random.seed(40)

random_numbers = sorted([random.randint(0, 100) for _ in range(50)])

categories = classify_numbers(random_numbers)

print("Bilangan acak (sorting):", random_numbers)
print("Kategori:", categories)

low_count = categories.count("low")
high_count = categories.count("high")
print(f"\nJumlah 'low': {low_count}")
print(f"Jumlah 'high': {high_count}")
