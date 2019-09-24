# Dockerfile-nginx

FROM nginx:1.17.3

# Nginx will listen on this port
EXPOSE 80

# Remove the default config file that /etc/nginx/nginx.conf includes
RUN rm /etc/nginx/conf.d/default.conf

# We copy the app.conf file to setup app with NGINX
COPY ./resources/utils/nginx/app.conf /etc/nginx/conf.d