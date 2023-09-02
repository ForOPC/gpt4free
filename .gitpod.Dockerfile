FROM gitpod/workspace-full
WORKDIR /app
COPY . /app
RUN chmod +x entrypoint.sh
RUN pip3 install --upgrade pip
RUN pip3 install g4f==3.8.4 \
                 httpx
RUN pip install --no-cache-dir -r requirements.txt
CMD ["./entrypoint.sh"]
