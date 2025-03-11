 sudo apt install python3-venv -y
 python3 -m venv hospatial_website
 source hospatial_website/bin/activate
 git clone git@github.com:harikrishna0944/hospital_website.git
 cd hospatial_website/
 pip install -r requirements.txt
 python manage.py makemigrations
 python manage.py migrate
 python manage.py runserver 0.0.0.0:8000
