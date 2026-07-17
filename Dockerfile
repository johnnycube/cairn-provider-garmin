FROM python:3.14-slim

WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Worker package + the committed generated proto stubs it imports.
COPY cairn_garmin ./cairn_garmin
COPY proto /opt/cairn-proto

ENV PYTHONPATH=/app \
    CAIRN_PROTO_PATH=/opt/cairn-proto \
    CAIRN_GARTH_HOME=/data/garth

VOLUME ["/data"]
ENTRYPOINT ["python", "-m", "cairn_garmin.main"]
