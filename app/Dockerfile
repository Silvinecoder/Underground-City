From python:3.10

RUN mkdir /app
COPY ./ /app

# Install dependencies
RUN cd /app/ && pip install -r requirements.txt -r requirements-dev.txt

WORKDIR /app

EXPOSE 80

CMD ["flask", "run", "--host=1.2.7.0"]
