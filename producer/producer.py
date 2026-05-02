from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

orders = [
    {"order_id": 1, "amount": 200, "status": "SUCCESS"},
    {"order_id": 2, "amount": 500, "status": "FAILED"},
    {"order_id": 3, "amount": 700, "status": "SUCCESS"}
]

for order in orders:
    producer.send('orders_topic', value=order)
    print(f"Sent: {order}")
    time.sleep(2)
