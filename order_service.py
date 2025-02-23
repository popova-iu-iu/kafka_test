from confluent_kafka import Producer
import json

# Конфигурация Kafka
KAFKA_BROKER = 'localhost:9092'
TOPIC_ORDER_CREATED = 'order_created'

# Producer для отправки событий
producer = Producer({'bootstrap.servers': KAFKA_BROKER})

def send_order_created_event(order_id, user_email, items):
    """
    Отправляет событие о создании заказа в Kafka.
    """
    event = {
        'order_id': order_id,
        'user_email': user_email,
        'items': items,
        'status': 'created'
    }
    producer.produce(TOPIC_ORDER_CREATED, json.dumps(event).encode('utf-8'))
    producer.flush()
    print(f"Order created event sent: {event}")

if __name__ == "__main__":
    # Пример создания заказа
    order_id = 12345
    user_email = 'user@example.com'
    items = [
        {'product_id': 3, 'name': 'Тонер для принтера', 'quantity': 2},
        {'product_id': 5, 'name': 'Бумага A4', 'quantity': 5}
    ]
    send_order_created_event(order_id, user_email, items)