# Fraud Detection in Transactions

This project implements a **fraud detection system** using **Apache Flink**. Transactions exceeding a certain threshold amount are flagged as fraudulent. The system processes transaction data in real time and outputs fraudulent transactions for further investigation.

## Features
- Generates synthetic transaction data for testing.
- Processes transaction data using Apache Flink's **DataStream API**.
- Flags transactions with an amount greater than `$5000` as fraudulent.
- Designed to handle batch and real-time data streams.

## Technologies Used
- **Python**: For implementing the fraud detection logic.
- **Apache Flink**: For distributed stream processing.
- **VS Code**: Development environment.

## How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/PranithJain98/fraud-detection-flink.git
cd fraud-detection-flink
2. Set Up the Environment
Ensure you have Python 3.8+ installed.
Install the required dependencies:
bash
Copy code
pip install apache-flink
3. Generate Synthetic Data
Run the data generator to create a transactions.csv file:

bash
Copy code
python3 transactions_generator.py
4. Run the Fraud Detection Job
Execute the fraud detection script to process the transactions:

bash
Copy code
python3 fraud_detection_job.py
5. View Output
Fraudulent transactions (amount > $5000) will be printed in the console.

Example output:

scss
Copy code
Transaction(transaction_id=txn23, user_id=user3, amount=7500.50, timestamp=1671408891000)
Transaction(transaction_id=txn78, user_id=user1, amount=6200.10, timestamp=1671408894000)
File Structure
bash
Copy code
fraud-detection-flink/
├── transactions_generator.py  # Generates synthetic transaction data.
├── fraud_detection_job.py     # Apache Flink job to detect fraud.
├── transactions.csv           # Generated synthetic transaction data (after running generator).
└── README.md                  # Project description and setup instructions.
Future Enhancements
Real-Time Integration: Replace the CSV file with a Kafka-based real-time data stream.
Database Integration: Save flagged transactions in a database (e.g., MySQL, PostgreSQL).
Visualization: Build a dashboard to monitor fraud trends using tools like Grafana or Power BI.
Author
Pranith Jain

License
This project is open source and available under the MIT License.
