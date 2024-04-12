
FROM python:3.11-slim

RUN mkdir todo_project

WORKDIR todo_project

COPY req.txt ./

RUN pip install -r ./req.txt

COPY . ./

CMD ["python","manage.py","runserver"]