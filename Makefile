test-local:
	PYTHONPATH=$(PWD) poetry run st --pre-run setup_test run -vv --checks all --app=main:app /openapi.json

test:
	PYTHONPATH=$(PWD) poetry run st --pre-run setup_test run -vv --checks all http://localhost:8000/openapi.json
