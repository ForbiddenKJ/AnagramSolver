@echo off

python setup.py bdist_wheel --universal
python -m twine upload --repository pypi --skip-existing dist/*
