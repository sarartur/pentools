cd ..
rm -rf build
rm -rf dist
rm -rf pentools.com.egg-info
python setup.py sdist bdist_wheel
twine upload dist/*
