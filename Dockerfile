FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY hello_flask ./hello_flask
EXPOSE 5000
ENV FLASK_APP=hello_flask
CMD ["flask","run","--host=0.0.0.0"]
