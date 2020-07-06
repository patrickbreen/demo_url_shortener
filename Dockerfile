FROM python:3.8.0b3-buster


# install the AWS CLI version 2
WORKDIR /aws_install
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install


# I'm going to only copy the requirements at first, for faster docker builds.
# Docker builds incrementally...
WORKDIR /app
COPY requirements.txt /app


RUN apt update
RUN apt install python3-pip -y
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt --upgrade
EXPOSE 80

# The install is good now, so copy in the rest of the application
COPY . /app
CMD ["python3", "app.py"]