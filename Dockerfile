# Image
FROM ubuntu:20.04

# Download dependencies
RUN apt-get update
RUN apt-get install python3.7
RUN apt-get install python3-pip -y
RUN apt-get install openssh-client -y
RUN apt-get install telnet -y

# Copy repository to container
COPY . /app

# Install requirements
RUN pip3 install --upgrade pip
RUN pip3 install flask
RUN pip3 install genie
RUN pip3 install pyats

# CD to folder healthcheck
WORKDIR /app/healthcheck

ENTRYPOINT ["python3"]
CMD ["startapp.py"]

# Info
MAINTAINER Johan Lahti