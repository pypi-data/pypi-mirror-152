# Build and update package
1. `rm ./dist`
2. `python setup.py sdist bdist_wheel`
3. `twine upload dist/*`