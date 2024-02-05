FROM 307943323221.dkr.ecr.us-east-1.amazonaws.com/tiangolo/uvicorn-gunicorn-fastapi:python3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN python -m spacy download en_core_web_sm

COPY ./app /code/app
COPY ./etc /code/etc

CMD ["opentelemetry-instrument","uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--workers", "4"]

