FROM python:3.10

WORKDIR /automation-api-python
COPY requirements.txt /automation-api-python/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /automation-api-python/requirements.txt

COPY . /automation-api-python/

CMD pytest

