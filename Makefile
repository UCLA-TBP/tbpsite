default: build

build: 
				docker-compose build

run: 
				-pkill docker-compose
				docker-compose up

restart:
				docker-compose restart backend

shell:
				docker-compose exec backend /app/manage.py shell_plus

test:
				docker-compose exec backend /app/manage.py test --no-input --parallel $(args)

clean_db:
				-docker-compose exec db mysql -uroot -pCAEpsilon -e "DROP DATABASE tbpsite;"

collect_static:
				docker-compose exec backend /app/manage.py collectstatic --noinput

init_db: clean_db 
				docker cp init_db.sql "$(shell docker-compose ps -q db)":/init_db.sql
				docker-compose exec db mysql -uroot -pCAEpsilon -e "CREATE DATABASE tbpsite;"
				docker-compose exec db /bin/sh -c "mysql -uroot -pCAEpsilon tbpsite < /init_db.sql" 
				-docker-compose exec backend /app/manage.py migrate --noinput --merge

untar_setup:
				tar -xzf setup.tar.gz

init: untar_setup init_db collect_static

backup_db:
				docker-compose exec db mysqldump -uroot -pCAEpsilon > tbpsite_dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql

install_package:
				docker-compose exec backend pip install $(pkg)
				docker-compose exec backend pip freeze | tail -n +1 > src/requirements.txt

