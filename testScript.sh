rm -r htmlcov/
coverage run --branch writeMusic.py
coverage html --omit=/usr/lib/*
