from confluent_kafka import Consumer, KafkaError
import json

# Конфигурация Kafka
KAFKA_BROKER = 'localhost:9092'
TOPIC_ORDER_CREATED = 'order_created'

# Consumer для получения событий
consumer = Consumer({
    'bootstrap.servers': KAFKA_BROKER,
    'group.id': 'notification_service',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe([TOPIC_ORDER_CREATED])

def send_notification(user_email, message):
    """
    Отправляет уведомление пользователю (заглушка).
    """
    print(f"Sending notification to {user_email}: {message}")

def handle_order_created_event(event):
    """
    Обрабатывает событие о создании заказа.
    """
    order_id = event['order_id']
    user_email = event['user_email']
    items = event['items']
    message = f"Ваш заказ #{order_id} успешно создан. Товары: {items}"
    send_notification(user_email, message)

def consume_events():
    """
    Получает события из Kafka.
    """
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(f"Error: {msg.error()}")
                break
        event = json.loads(msg.value().decode('utf-8'))
        print(f"Received event: {event}")
        handle_order_created_event(event)

if __name__ == "__main__":
    print("Notification Service is running...")
    consume_events()