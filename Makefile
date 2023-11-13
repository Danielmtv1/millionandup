.PHONY: test
api:
	uvicorn main:app --reload
test:
	python -m unittest discover -s tests -p 'test_routes.py'
