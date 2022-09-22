# syntax=docker/dockerfile:1

# Use official node image as the base image
FROM node:latest as build

ENV NODE_ENV=production

# Set the working directory
WORKDIR /app

# Install all the dependencies
COPY ["package.json", "package-lock.json*", "./"]
RUN npm install --production

# Add the source code to app
COPY . . 

# Generate the build of the application
RUN npm run build

# Stage 2: Serve app with nginx server
# Use official nginx image as the base image
FROM nginx:latest

# Copy the build output to replace the default nginx contents.
COPY --from=build /app/build /usr/share/nginx/html
