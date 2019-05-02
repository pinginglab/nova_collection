#!/bin/bash
pip freeze > requirement
docker build -t nova:latest .
docker tag nova:latest registry.pinginglab.com:5000/beckend/nova:1.0
docker push registry.pinginglab.com:5000/beckend/nova:1.0