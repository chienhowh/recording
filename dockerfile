# Import basic image
FROM python:3.10 
# Where to use
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
# Copy source to destination
COPY . .
CMD [ "/bin/bash","docker-entrypoint.sh" ] 