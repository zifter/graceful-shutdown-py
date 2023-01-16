.PHONY: setup
setup:
	pip install tox

.PHONY: test
test:
	tox

.PHONY: fix
fix:
	tox -e isort
	tox -e black

.PHONY: build
build:
	tox -e build_wheel

.PHONY: publish
publish:
	tox -e pypi_upload
