dev:
	pip install -r requirements/development.txt

djadmin-chromium:
	@echo 'will create a new tab on the browser and go to the django admin url'
	chromium http://127.0.0.1:8000/admin/login/?next=/admin/

djadmin-chrome:
	@echo 'will create a new tab on the browser and go to the django admin url'
	chrome http://127.0.0.1:8000/admin/login/?next=/admin/

djadmin-firefox:
	@echo 'will create a new tab on the browser and go to the django admin url'
	firefox http://127.0.0.1:8000/admin/login/?next=/admin/
