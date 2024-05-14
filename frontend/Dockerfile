# frontend/Dockerfile
FROM nginx:latest

# Copia i file HTML e CSS nella directory di default di Nginx
COPY templates /usr/share/nginx/html

# Esponi la porta 80 per il traffico HTTP
EXPOSE 80

# Avvia Nginx all'interno del container
CMD ["nginx", "-g", "daemon off;"]
