#parent image
FROM python:3.12

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
# Expose the port that the API runs on
EXPOSE 5000
ENV FLASK_APP=app.py
CMD ["python", "app.py"]
