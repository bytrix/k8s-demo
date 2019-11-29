#! /bin/bash
docker stop demo
docker rm demo
docker run -it -p 5000:5000 -v /Users/wengzhijie/Desktop/git/k8s-demo:/root --name=demo demo python /root/app.py
