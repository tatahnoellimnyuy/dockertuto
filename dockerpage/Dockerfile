# set the base Image
FROM python:3 

# set the working directory
WORKDIR  /usr/src/app

#copy all files into the container

COPY . .

#install the dependancies from requirements.txt

RUN pip install  --no-cache-dir -r requirements.txt

#expose the django default port

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

# run the command
CMD ["python3", "./manage.py","runserver","0.0.0.0:8000"] 




