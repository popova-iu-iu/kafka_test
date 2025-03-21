# Kafka Test App

Это приложение демонстрирует использование Kafka для отправки и получения сообщений о создании заказов. Оно состоит из Flask-приложения, которое отправляет события в Kafka, и Consumer, который получает эти события и отправляет уведомления пользователям.

## 1. Установка
Перед началом убедитесь, что у вас установлен Docker и Docker Compose.

### 1.1 Клонируйте репозиторий

```bash
git clone https://github.com/popova-iu-iu/kafka_test.git
cd kafka_test
```

### 1.2 Установите зависимости
```
pip install -r requirements.txt
```

## 2. Запуск приложения

### 2.1 Запустите Kafka и Zookeeper
Используйте Docker Compose для запуска Kafka и Zookeeper:
```
docker-compose up -d
```

### 2.2 Запустите приложение Flask
В отдельном терминале запустите Flask приложение:
```commandline
python app.py
```

### 2.3 Запустите Consumer
В другом терминале запустите Consumer для получения уведомлений:
```commandline
python notification_service.py
```

## 3. Использование
Откройте браузер и перейдите по адресу http://localhost:5000.
Введите ID заказа, email пользователя, выберите товар и укажите количество.
Нажмите кнопку "Купить", чтобы отправить уведомление о создании заказа.
Проверяйте консоль Consumer для получения уведомлений о создании заказа.

### Примечания
Убедитесь, что ваши зависимости в requirements.txt соответствуют установленным версиям библиотек.
Вы можете изменить настройки Kafka и Zookeeper в docker-compose.yml по мере необходимости.

