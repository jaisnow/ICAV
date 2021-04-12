# ICAV

This project you used for displaying rows and filter data from books.csv file

## Installation

- First you need to create python3+ version environemt 
- Then you need to clone the project from https://github.com/jaisnow/ICAV.git repo 
- Then after cloning instal all the dependencies from requirement.txt file
- and start project by running command python manage.py runserver


## API URL's

1) Getting number of rows from books.csv file with the use of below given API

```http://localhost:8000/tests/books/?rows=2```

2) For getting listing of filtered data on the bases of each column present in books,csv file

```http://localhost:8000/tests/books/filter?audthor=Sapphire```


## Test CASES

For runnin test cases you need to run
	- python manage.py test