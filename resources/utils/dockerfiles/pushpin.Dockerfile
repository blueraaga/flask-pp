# Dockerfile-pushpin

FROM fanout/pushpin:1.24.0

# Expose ports from the original dockerfile.
# - 7999: HTTP port to forward on to the app
# - 5560: ZMQ PULL for receiving messages
# - 5561: HTTP port for receiving messages and commands
# - 5562: ZMQ SUB for receiving messages
# - 5563: ZMQ REP for receiving commands

# Remove the default config file that /etc/nginx/nginx.conf includes
RUN rm /etc/pushpin/routes

# We copy the app.conf file to setup app with NGINX
COPY ./resources/utils/pushpin/routes /etc/pushpin