FROM python:latest

# Create the group and user to be used in this container
RUN groupadd flaskgroup && useradd -m -g flaskgroup -s /bin/bash flask

# Create the working directory (and set it as the working directory)
RUN mkdir -p /home/flask/app/web
WORKDIR /home/flask/app/web

# Install the package dependencies
COPY requirements.txt /home/flask/app/web
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container
COPY . /home/flask/app/web

RUN chown -R flask:flaskgroup /home/flask

USER flask

CMD ["/usr/local/bin/gunicorn", "-w", "2", "-b", "0.0.0.0:8000", "project:app"]