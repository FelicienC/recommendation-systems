UV := uv

.PHONY: init notebooks docs-build docs-serve prek clean

init:
	$(UV) sync
	$(UV) run prek install
	$(UV) run prek install --hook-type commit-msg

prek:
	$(UV) run prek run --all-files

notebooks:
	$(UV) run jupyter nbconvert --to notebook --execute --stdout src/recommendationsystems/*/*.ipynb > /dev/null

docs-build:
	$(UV) run mkdocs build --strict

docs-serve:
	$(UV) run mkdocs serve

clean:
	rm -rf .venv .pytest_cache .ruff_cache .ty_cache build dist *.egg-info
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
