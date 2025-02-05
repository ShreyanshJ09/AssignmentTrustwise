#parent image
FROM python:3.12

# Set an environment variable for Hugging Face token
ARG HF_TOKEN
ENV HF_TOKEN=${HF_TOKEN}


WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
# Expose the port that the API runs on
EXPOSE 10000
ENV FLASK_APP=app.py
CMD ["python", "app.py"]
