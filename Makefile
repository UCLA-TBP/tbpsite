default: build

build: 
				docker build -t tbpsite/backend backend
				docker build -t tbpsite/frontend frontend
				docker build -t tbpsite/websockets frontend
				docker-compose build

run: 
				-pkill docker-compose
				docker-compose up

restart:
				docker-compose restart backend frontend

shell:
				docker-compose exec backend /app/manage.py shell_plus

test:
				docker-compose exec backend /app/manage.py test --no-input --parallel $(args)

clean_db:
				-docker-compose exec db mysql -uroot -pCAEpsilon -e "DROP DATABASE tbpsite;"

init_db: clean_db 
				docker cp init_db.sql "$(shell docker-compose ps -q db)":/init_db.sql
				docker-compose exec db mysql -uroot -pCAEpsilon -e "CREATE DATABASE tbpsite;"
				docker-compose exec db /bin/sh -c "mysql -uroot -pCAEpsilon tbpsite < /init_db.sql" 
				docker-compose exec backend /app/manage.py migrate --noinput --merge

backup_db:
				docker-compose exec db mysqldump -uroot -pCAEpsilon > tbpsite_dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql

install_package:
				docker-compose exec backend pip install $(pkg)
				docker-compose exec backend pip freeze | tail -n +1 > src/requirements.txt

