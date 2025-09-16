FROM postgres:14

ENV POSTGRES_DB=sap
ENV POSTGRES_USER=meli
ENV POSTGRES_PASSWORD=metralleta

COPY ../source/tables/init.sql /docker-entrypoint-initdb.d/