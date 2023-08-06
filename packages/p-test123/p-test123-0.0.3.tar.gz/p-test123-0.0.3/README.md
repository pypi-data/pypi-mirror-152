```
pip install --user --upgrade setuptools
pip install twine
```
```
python3 -m build
python setup.py sdist
twine upload dist/*
```
