from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.functions import MapFunction, FilterFunction

class Transaction:
    def __init__(self, transaction_id, user_id, amount, timestamp):
        self.transaction_id = transaction_id
        self.user_id = user_id
        self.amount = amount
        self.timestamp = timestamp

    @staticmethod
    def from_csv_line(line):
        fields = line.split(",")
        return Transaction(fields[0], fields[1], float(fields[2]), int(fields[3]))

    def __str__(self):
        return f"Transaction(transaction_id={self.transaction_id}, user_id={self.user_id}, amount={self.amount}, timestamp={self.timestamp})"

class FraudFilter(FilterFunction):
    def filter(self, transaction: Transaction):
        return transaction.amount > 5000  # Flag as fraud if amount > $5000

class ParseTransaction(MapFunction):
    def map(self, value):
        # Skip the header row
        if "transaction_id" in value:
            return None
        return Transaction.from_csv_line(value)

def main():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)

    # Read from the CSV file as a text stream
    transaction_stream = env.read_text_file("transactions.csv")

    # Parse the text lines into Transaction objects
    transactions = transaction_stream.map(ParseTransaction()).filter(lambda x: x is not None)

    # Filter fraudulent transactions
    fraudulent_transactions = transactions.filter(FraudFilter())

    # Print the fraudulent transactions
    fraudulent_transactions.print()

    # Execute the Flink job
    env.execute("Fraud Detection Job")

if __name__ == "__main__":
    main()
