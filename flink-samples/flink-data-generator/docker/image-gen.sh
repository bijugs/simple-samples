#!/bin/sh
cp ../target/flink-data-generator-1.0-SNAPSHOT.jar .
docker image rm dockerhub/datagen-client:1.0
docker image rm dockerhub/datagen:1.0
docker build -t dockerhub/datagen:1.0 -f Dockerfile .
docker build -t dockerhub/datagen-client:1.0 -f Dockerfile.client .
