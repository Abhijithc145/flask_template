SHELL := /bin/bash

env-local-setup:
	rm -rf venv
	python3.8 -m venv venv; \
	source venv/bin/activate; \
	pip install -r requirements.txt

# run-dev:
# 	conda deactivate; \
# 	conda activate bot; \
# 	pip install -r requirements.txt; \
# 	export CONFIG_PATH=configs/dev.cfg; \
# 	python manage.py makemigrations; \
# 	python manage.py migrate; \
# 	rm -rf bot_service/static; \
# 	python manage.py collectstatic; \
# 	sudo systemctl restart bot

run-local:
	source venv/bin/activate; \
	black .; \
	python3 blog.py 
	