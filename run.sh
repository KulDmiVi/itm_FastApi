celery -A app.celery_worker.app worker -l info &
uvicorn app.main:app --host 0.0.0.0 --reload