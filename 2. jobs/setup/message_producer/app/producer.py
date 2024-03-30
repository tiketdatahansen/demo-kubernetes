from kafka import KafkaProducer
import uuid
import argparse


def produce_messages(n, bootstrap_servers: str, topic: str):
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers.split(","))
    count = 0

    for _ in range(n):
        try:
            message = str(uuid.uuid4()).encode("utf-8")
            producer.send(topic, value=message)
            count += 1
        except Exception as e:
            print(f"Error producing message: {e}")

    producer.flush()
    return count


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Produce UUIDs to a Kafka topic.")
    parser.add_argument("-n", type=int, default=1, help="Number of UUIDs to generate")
    parser.add_argument(
        "-b",
        "--bootstrap-servers",
        type=str,
        default="localhost:9092",
        help="Kafka bootstrap servers",
    )
    parser.add_argument(
        "-t",
        "--topic",
        type=str,
        default="default",
        help="Kafka topic to produce to",
    )

    args = parser.parse_args()
    print(vars(args))
    count = produce_messages(args.n, args.bootstrap_servers, args.topic)
    print(f"Produced {count} messages to {args.topic}")
