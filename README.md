🚀 Real-Time Order Processing Pipeline using Apache Kafka & PySpark

📌 Overview
This project demonstrates a real-time data pipeline using Apache Kafka and PySpark.

🏗️ Architecture
Producer → Kafka → Spark Streaming → Output

⚙️ Tech Stack
- Apache Kafka
- PySpark
- Docker

How to Run

Start Kafka
docker-compose up -d

Run Producer
python producer/producer.py

Run Consumer
python consumer/spark_streaming.py

Features
- Real-time streaming
- Fault-tolerant pipeline
- Scalable architecture
