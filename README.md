# merchagency
digital marketing
## objectives 
-create central reposiroty for independent merch retailers
-allow users to share socials
-allow users to follow each other
-allow users to post their work

### installation
- clone or download the repository
- download and install teseract ocr engine 
- to install all dependencies run
  ```shell
   pip install requirments.txt
  ```
 to run the server run the following commands
 ```shell
 python manage.py makemigrations
 python manage.py migrate
 python manage.py runserver
 ```
 on browser go to http://127.0.0.1:8000/
 
 if user wants to create a superuser account(admin)
 run the following command

 ```shell
 python manage.py createsuperuser
 ```
 
 link : https://merchagency.herokuapp.com/

