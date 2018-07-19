python3 -m venv myvenv
sudo apt install python-virtualenv
virtualenv --python=python3.6 myvenv
source myvenv/bin/activate

django-admin startproject mysite .
