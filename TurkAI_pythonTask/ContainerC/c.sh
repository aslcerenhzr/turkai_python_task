#!/bin/bash

DOCKER_CMD=$(which docker)  # Docker'ın tam yolunu bulma

if [ -z "$DOCKER_CMD" ]; then
    echo "Docker komutu bulunamadı."
    exit 1
fi

# RabbitMQ sunucusunu başlatma komutu
$DOCKER_CMD run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management

echo "RabbitMQ sunucusu başlatıldı. Yönetim arayüzüne http://localhost:15672 adresinden erişebilirsiniz."
