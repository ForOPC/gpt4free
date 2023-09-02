FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN chmod +x /app/entrypoint.sh
RUN pip3 install --upgrade pip
RUN pip3 install g4f==0.0.2.6 \
                 httpx
CMD ["/app/entrypoint.sh"]
