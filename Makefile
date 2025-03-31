django:
	wrk -t4 -c100 -d10s http://localhost:8000/users
fastapi:
	wrk -t4 -c100 -d10s http://localhost:8001/users
robyn:
	wrk -t4 -c100 -d10s http://localhost:8002/users


rebuild_django:
	docker-compose build django
	docker-compose up -d django
	docker compose exec django python manage.py makemigrations
	docker compose exec django python manage.py migrate
	docker compose exec django python manage.py shell -c "from django_app.models import User; for i in range(1000): User.objects.create(name=f'User{i}', email=f'u{i}@test.com')"

rebuild_fastapi:
	docker-compose build fastapi
	docker-compose up -d fastapi
	docker compose exec fastapi python init_db.py
	
rebuild_robyn:
	docker-compose build robyn_app
	docker-compose up -d robyn_app
	docker compose exec robyn_app python init_db.py


