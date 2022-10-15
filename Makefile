test:
	PYTHONPATH=$(PWD) poetry run st run --checks all --app=main:app /openapi.json
