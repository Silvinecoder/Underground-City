From python:3.10

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /app

COPY ./ /app

EXPOSE 80
CMD ["flask", "run", "--host=1.2.7.0"]
