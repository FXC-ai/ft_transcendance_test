FROM nginx:1.25

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

RUN mkdir -p /var/www/
COPY src/index.html /var/www/index.html
COPY src/pong /var/www/pong/

CMD ["nginx", "-g", "daemon off;"]