# proxy/default.conf.tpl

server {
    listen ${LISTEN_PORT};

    location /static {
        alias /vol/static;
    }


    location / {
        proxy_pass      http://${APP_HOST}:${APP_PORT};
        include         /etc/nginx/proxy_params;
    }
}