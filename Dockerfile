from python:3.10-slim AS base

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


COPY /graph_app /graph_app

EXPOSE 8000

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "graph_app.main:app", "--reload"]


