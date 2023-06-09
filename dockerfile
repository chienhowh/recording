# Import basic image
FROM python:3.10 
# Expose port
EXPOSE 5000
# Where to use
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
# Copy source to destination
COPY . .
CMD [ "flask","run","--host","0.0.0.0" ] 