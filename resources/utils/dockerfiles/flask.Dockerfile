# Dockerfile-flask

# We simply inherit the Python 3 image. This image does not particularly care what OS runs underneath
FROM python:3.6

# Set an environment variable with the directory where we'll be running the app
ENV APP /app

# Create the directory and instruct Docker to operate from there from now on
RUN mkdir $APP
WORKDIR $APP

# Create folder for uWSGI logging`
RUN mkdir /tmp/uwsgi

# Expose the port uWSGI will listen on
EXPOSE 5000

# Copy the requirements file in order to install Python dependencies
COPY app/requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Finally, we run uWSGI with the ini file we created earlier
CMD [ "uwsgi", "--ini", "app.ini" ]