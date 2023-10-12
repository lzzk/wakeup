FROM python

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
RUN ls -la
RUN pwd

CMD ["python", "wakeup.py"]
