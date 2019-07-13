### 1. 가상환경 생성
virtualenv rookie_project_server --no-site-packages

### 2. 가상환경 실행
source virtual_rookie_project/bin/activate

### 3. 설치
pip3 install django==2.1.0
pip3 install djangorestframework
pip3 install django-rest-swagger
pip3 install Pillow

### 4. 장고 설치 확인
python3 -c "import django; print(django.get_version())"

### 5. 프로젝트 생성
django-admin.py startproject rookie_server

### 6. 앱 생성
python3 manage.py startapp diary_server

### 7. 모델 변경시
python3 manage.py makemigrations
python3 manage.py migrate

### 8. 서버 실행
python3 manage.py runserver {my IP address}:8000
