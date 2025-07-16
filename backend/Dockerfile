FROM python:3.12-slim

WORKDIR /api

COPY . backend/
COPY requirements_backend.txt .

# Instala locale pt_BR.UTF-8
RUN apt-get update && apt-get install -y locales && \
    sed -i '/pt_BR.UTF-8/s/^# //g' /etc/locale.gen && \
    locale-gen pt_BR.UTF-8 && \
    update-locale LANG=pt_BR.UTF-8

ENV LANG=pt_BR.UTF-8
ENV LANGUAGE=pt_BR:pt
ENV LC_ALL=pt_BR.UTF-8
ENV PYTHONPATH="/"

RUN pip install --upgrade pip
RUN pip install -r requirements_backend.txt

EXPOSE 5000

CMD ["python", "-m", "backend.app"]