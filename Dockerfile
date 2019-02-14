FROM python:2.7.14

ARG project_dir=/app/

ADD requirements.txt $project_dir

WORKDIR $project_dir
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
