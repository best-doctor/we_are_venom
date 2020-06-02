check:
	flake8 we_are_venom
	mypy we_are_venom
	mdl README.md
	python -m pytest --cov=we_are_venom --cov-report=xml --disable-network
