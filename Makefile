VENV_NAME?=$$HOME/.venv/python3_test_env
run:
	@echo "run"; \
	
	@scrapy crawl test -O data.json; \

	@python RewriteData.py; \

	@json-server --watch data.json; \
	
	@echo "finish"
