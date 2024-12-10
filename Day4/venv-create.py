'''

Create venv:

python -m venv venv_name
Activate venv:

Windows:
1.venv_name\Scripts\activate
2. venv_name\Scripts\activate.bat

Linux/Mac:
source venv_name/bin/activate
Deactivate venv:

deactivate

ex :-
➜  Django-Class-3 git:(main) ✗ python3 -m venv venv_name
➜  Django-Class-3 git:(main) ✗ source venv_name/bin/activate
(venv_name) ➜  Django-Class-3 git:(main) ✗ 
(venv_name) ➜  Django-Class-3 git:(main) ✗ deactivate
➜  Django-Class-3 git:(main) ✗ 

how to check python version
python3 --version

(venv_name) ➜  Django-Class-3 git:(main) python3 --version

Python 3.10.12


install django:-
(venv_name) ➜  Django-Class-3 git:(main) ✗ pip install django 
Collecting django
  Downloading Django-5.1.4-py3-none-any.whl (8.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.3/8.3 MB 13.3 MB/s eta 0:00:00
Collecting sqlparse>=0.3.1
  Downloading sqlparse-0.5.2-py3-none-any.whl (44 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 44.4/44.4 KB 3.9 MB/s eta 0:00:00
Collecting asgiref<4,>=3.8.1
  Using cached asgiref-3.8.1-py3-none-any.whl (23 kB)
Collecting typing-extensions>=4
  Using cached typing_extensions-4.12.2-py3-none-any.whl (37 kB)
Installing collected packages: typing-extensions, sqlparse, asgiref, django
Successfully installed asgiref-3.8.1 django-5.1.4 sqlparse-0.5.2 typing-extensions-4.12.2


'''
