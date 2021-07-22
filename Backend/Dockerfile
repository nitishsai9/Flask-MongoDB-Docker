FROM python:3

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .

ENV PORT=3000


EXPOSE 3000

CMD [ "python3","server.py" ]