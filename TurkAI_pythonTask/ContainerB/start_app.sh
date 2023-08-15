#!/bin/bash
sleep 20
# PostgreSQL servisini başlat
service postgresql start

# PostgreSQL kullanıcısına geç
su postgres <<EOF
psql -U postgres -c "create database mydb;"
psql -U postgres -c "alter user postgres password 'postgres';"
EOF

# Veritabanı bağlantısını başlatmak için Python komutu (ve port numarası parametresi)
python connect_db.py  --database_host localhost --database_port 5432
wait

# Uygulamayı başlatmak için Python komutu 
python app.py 

# Bash betiği burada sona erer
