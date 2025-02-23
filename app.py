from flask import Flask, render_template, request
from confluent_kafka import Producer, Consumer, KafkaError
import threading
import json

app = Flask(__name__)

# Producer configuration
producer = Producer({'bootstrap.servers': 'localhost:9092'})

# Consumer configuration
consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['order_created'])

# Global variable to store messages
messages = []


def consume_messages():
    global messages
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break
        messages.append(msg.value().decode('utf-8'))


@app.route('/', methods=['GET', 'POST'])
def index():
    global producer
    if request.method == 'POST':
        order_id = request.form['order_id']
        user_email = request.form['user_email']
        selected_product = json.loads(request.form['product'])
        quantity = int(request.form['quantity'])

        event = {
            'order_id': order_id,
            'user_email': user_email,
            'items': [
                {
                    'product_id': selected_product['product_id'],
                    'name': selected_product['name'],
                    'quantity': quantity,
                    'price': selected_product['price']
                }
            ],
            'status': 'created'
        }

        producer.produce('order_created', json.dumps(event).encode('utf-8'))  # Отправка в нужный топик
        producer.flush()

    return render_template('index.html', messages=messages)


if __name__ == "__main__":
    # Start the consumer in a separate thread
    threading.Thread(target=consume_messages, daemon=True).start()
    app.run(debug=True)
