from confluent_kafka import Producer
from config import KAFKA_BOOTSTRAP_SERVERS

producer = Producer({'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS})


def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed: {err}")
    else:
        print(f"Event produced to {msg.topic()} [{msg.partition()}]")


def produce_event(event_dict: dict, topic: str):
    producer.produce(topic, value=str(event_dict), callback=delivery_report)
    producer.flush()
