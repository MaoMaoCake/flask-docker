# we use a debian base because its better than alpine for image size
# Buster is able to use the prebuild wheels saving us compile time
FROM python:3.8-slim-buster

# this is specifying the directory that the rest of the code will be run in
WORKDIR /flask

COPY . ./

RUN pip install -r requirements.txt

#RUN python initdb.py

EXPOSE 3000
CMD ["gunicorn"  , "-b", "0.0.0.0:3000", "app:app"]