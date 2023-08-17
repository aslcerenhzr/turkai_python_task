#!/bin/bash
sleep 10

# PostgreSQL servisini başlat
service postgresql start

# PostgreSQL kullanıcısına geç
su postgres -c "psql -U postgres -c \"create database mydb;\""
su postgres -c "psql -U postgres -c \"alter user postgres password 'postgres';\""

python /app/connect_db.py
wait

python /app/myflaskapp/app.py 

