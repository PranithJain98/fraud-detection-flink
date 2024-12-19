import random
import time
import csv

def generate_transactions(output_file, num_transactions=1000):
    users = ["user1", "user2", "user3", "user4"]
    with open(output_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["transaction_id", "user_id", "amount", "timestamp"])
        for i in range(num_transactions):
            writer.writerow([
                f"txn{i}",
                random.choice(users),
                round(random.uniform(10, 10000), 2),
                int(time.time() * 1000)
            ])
            time.sleep(0.01)  # Simulate a real-time stream

if __name__ == "__main__":
    generate_transactions("transactions.csv")
