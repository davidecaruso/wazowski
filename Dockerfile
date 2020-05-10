FROM python:3

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

CMD [ "python3", "main.py" ]
