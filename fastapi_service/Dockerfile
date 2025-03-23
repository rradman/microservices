FROM python:3.13-slim
WORKDIR /app
COPY app pyproject.toml .
RUN pip install .
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]