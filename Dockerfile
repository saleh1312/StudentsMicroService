FROM python:3.10

WORKDIR /home/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD [ "python", "main.py" ]