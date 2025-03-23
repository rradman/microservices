FROM python:3.13-slim
WORKDIR /app
COPY app pyproject.toml .
RUN pip install .
COPY . .
EXPOSE "8080"
CMD ["python", "app/main.py"]
