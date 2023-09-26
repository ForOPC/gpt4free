FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN chmod +x /app/entrypoint.
RUN apt-get update && apt-get install -y git
RUN pip3 install --upgrade pip
RUN pip3 install g4f==0.0.3.4 \
                 PyExecJS==1.5.1 \
                 httpx
CMD ["/app/entrypoint.sh"]
