#!/bin/bash

# Başlangıç mesajı
echo "Başliyor..."

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
