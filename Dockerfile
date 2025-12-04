
FROM python:3.11-slim AS builder


WORKDIR /app


COPY requirements.txt .


RUN pip install --upgrade pip \
    && pip install --prefix=/install -r requirements.txt

FROM python:3.11-slim


ENV TZ=UTC


WORKDIR /app


RUN apt-get update && apt-get install -y --no-install-recommends \
        cron \
        tzdata \
    && ln -snf /usr/share/zoneinfo/UTC /etc/localtime \
    && echo "UTC" > /etc/timezone \
    && apt-get clean && rm -rf /var/lib/apt/lists/*


COPY --from=builder /install /usr/local


COPY . /app

RUN chmod 0644 /app/cron/2fa-cron \
    && crontab /app/cron/2fa-cron


RUN mkdir -p /data /cron \
    && chmod 755 /data /cron


EXPOSE 8080


CMD cron && uvicorn main:app --host 0.0.0.0 --port 8080
