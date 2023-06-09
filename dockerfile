# Import basic image
FROM python:3.10 
# Where to use
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cahe-dir --upgrade -r requirements.txt
# Copy source to destination
COPY . .
CMD [ "gunicorn","--bind","0.0.0.0:80","app:create_app()" ] 