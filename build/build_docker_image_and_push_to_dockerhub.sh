#!/bin/bash

cd ..
docker build -t gtdreams/wog4:v1.0 .
docker-compose build
docker push gtdreams/wog4:v1.0
