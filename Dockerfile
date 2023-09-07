FROM mcr.microsoft.com/playwright:v1.36.0-focal
WORKDIR /usr/local/bin
COPY requirements.txt .
RUN  apt update
RUN apt install python3-pip -y
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN apt update -y
RUN apt -f install -y
RUN apt-get install -y wget python3-venv
ADD . .
