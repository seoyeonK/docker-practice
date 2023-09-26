FROM    ubuntu
RUN     apt-get update && apt-get install -y git
RUN     mkdir /app
WORKDIR app
COPY    ./cloner /app/
RUN     chmod a+x /app/cloner
CMD     ["/app/cloner"]