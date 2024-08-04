FROM python:3.11

WORKDIR  /docker_dir

COPY ./requirements.txt /docker_dir/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /docker_dir/requirements.txt

COPY . /docker_dir/

EXPOSE 8000

CMD uvicorn main:app --host 0.0.0.0 --port 8000