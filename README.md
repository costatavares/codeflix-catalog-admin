# codeflix-catalog-admin

## criara ambiente virtual 
python3 -m venv venv 

## para acessar ambiente
 source venv/bin/activate

crtl +k - limpa o terminal 

C:\Users\ANDERSON\AppData\Local\Programs\cursor


pytest  /home/anderson/python/codeflix-catalog-admin/test_category.py

src
└── core
    └── category
        ├── application
        ├── domain
        │   └── category.py
        ├── infra
        └── test
            ├── application
            │   └── test_category.py
            ├── domain
            └── infra


# Command start
python manage.py runserver

# commad test 
python manage.py test django_project

para rodar com pytest deve se instalar o pytest-django 

pip install pytest-django
e configurar o arquivo codeflix-catalog-admin/pytest.ini
 

# Dê permissão de execução:

bash
Copiar
Editar
chmod +x create_app.sh

# djangorestframework
pip install djangorestframewor


# Migrations 
Deve se criar os modelos "/codeflix-catalog-admin/src/django_project/category_app/models.py"
python manage.py makemigrations

python manage.py migrate

#DOCKER 

docker-compose build
docker-compose up -d

docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py dbshell
