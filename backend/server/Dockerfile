# syntax=docker/dockerfile:1

# Use official node image as the base image
FROM node:latest


# Set the working directory
WORKDIR /usr/src/app
COPY package*.json ./
# Install all the dependencies
RUN npm install 

# Add the source code to app
COPY . .

CMD [ "node", "app.js" ]