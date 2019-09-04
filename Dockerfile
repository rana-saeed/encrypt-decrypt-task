FROM python:3

ADD interface.py /
ADD task.py /
ADD unitTests.py /

RUN pip install click
RUN pip install requests

ENTRYPOINT ["python", "./interface.py"]