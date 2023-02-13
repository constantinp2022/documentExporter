# document Exporter
## How to install 
1. Install python (version 3 was tested)
2. Install django and all the requirements
```bash
cd web_interface
python3 -m pip install -r requirements.txt
```
3. Install libreoffice

```bash
sudo apt install libreoffice -y
```

4. Make the migrations
```bash
python3 manage.py makemigrations
```
5. Migrate 
```bash
python3 manage.py migrate
```

6. Start the app
```bash
python3 manage.py runserver
```

### Point 4.and 5. are for DB 
<br>
<br>
<br>

## Few tips
1. Start the app at certain port:
```bash
python3 manage.py runserver 127.0.0.1:8000
```
2. Start the app and run it in backgroud even after closing ssh session

```bash
nohup python3 manage.py runserver 127.0.0.1:8000 &
```
3. Close the background task by

```bash
kill -9 $pid
```
4. $pid variable is just the process id you could find it by running:

```bash
ps -ef | grep manage.py
```
<br>

## How a template looks like 
A template is any docx file. For example teamplate.docx that contain: 
```
Hi {{ employee.first_name }}
```
It will generate a generated_document.docx/pdf
```
Hi John
```
 If the Employee first name is <i>John</i> in DB

<br>


## What it is?
It is a web interface to generate docx/pdf for employees starting from a base template and filling automatically data from a database
<br>
<br>

## What database it uses
At the moment in settings is set up to save in SQLite which is just a local 