# my simple python framework is in development

Before run the framework install all packages:
```pip install -r requirements.txt```

## Starting simple framework
run command 
```gunicorn app:app --bind 127.0.0.1:8010``` 
"--bind" helps to start localhost with port 8010, 
you can change port, if it already is used

Here are the links, that are implemented:<br/>
[http://127.0.0.1:8010/home]()<br/>
[http://127.0.0.1:8010/about]()<br/>
[http://127.0.0.1:8010/hello/yourname]()<br/>
[http://127.0.0.1:8010/tell/100]()<br/>
[http://127.0.0.1:8010/books]()<br/>
[http://127.0.0.1:8010/sample]()<br/>
[http://127.0.0.1:8010/template]()<br/>
[http://127.0.0.1:8010/json]()<br/>
[http://127.0.0.1:8010/text]()<br/>

## Unit tests
run command
```pytest test_framework.py``` 

for coverage percentage:
```pytest --cov=. test_framework.py``` 


## Just testing WSGI files
run command 
```python WSGI.py``` 
in framework dir and open 
```http://localhost:8005/```

for reversed response:
run command 
```python WSGI_reverse.py``` 
in framework dir and open 
```http://localhost:8006/```