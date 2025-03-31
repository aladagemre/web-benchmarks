django:
	wrk -t4 -c100 -d10s http://localhost:8000/users
fastapi:
	wrk -t4 -c100 -d10s http://localhost:8001/users
robyn:
	wrk -t4 -c100 -d10s http://localhost:8002/users
robyn_tortoise:
	wrk -t4 -c100 -d10s http://localhost:8003/users
gogini:
	wrk -t4 -c100 -d10s http://localhost:8004/users
	
rebuild_django:
	docker-compose build django_app
	docker-compose up -d django_app
	docker compose exec django_app python manage.py makemigrations
	docker compose exec django_app python manage.py makemigrations django_app
	docker compose exec django_app python manage.py migrate
	docker compose exec django_app python manage.py migrate django_app
	# docker compose exec django_app python manage.py shell -c "from django_app.models import User; for i in range(1000): User.objects.create(name=f'User{i}', email=f'u{i}@test.com')"

rebuild_fastapi:
	docker-compose build fastapi_app
	docker-compose up -d fastapi_app
	docker compose exec fastapi_app python init_db.py
	
rebuild_robyn:
	docker-compose build robyn_app
	docker-compose up -d robyn_app
	docker compose exec robyn_app python init_db.py

rebuild_robyn_tortoise:
	docker-compose build robyn_tortoise_app
	docker-compose up -d robyn_tortoise_app
	docker compose exec robyn_tortoise_app python init_db.py
	
	

rebuild_go_gin:
	docker-compose build go_gin_app
	docker-compose up -d go_gin_app
