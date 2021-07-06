# Base Image 
FROM ubuntu:16.04

# Mainatiner of this image
MAINTAINER Amit Vashist <amitvashist7@outlook.com>

# Update Apt Repo. 
RUN apt-get update

# Install Apache Packages 
RUN apt-get install apache2 -y 

# Insert Custom Web Page 
COPY index.html /var/www/html/index.html

# Bring up the Service
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
