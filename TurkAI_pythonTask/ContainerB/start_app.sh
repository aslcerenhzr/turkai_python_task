#!/bin/bash

# Başlangıç mesajı
echo "Başliyor..."

# Start PostgreSQL service
service postgresql start
su postgres 
psql -U postgres -c "create database mydb;"
psql -U postgres -c "alter user guest password 'guest';"

# Veritabanı bağlantısını başlat
python connect_db.py
# Veritabanı bağlantısının tamamlanmasını beklemek
wait

# Uygulamayı başlat
python app.py
# Uygulamanın tamamlanmasını beklemek
wait

# Tamamlandı mesajı
echo "Tamamlandi."
