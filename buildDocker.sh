#!/bin/bash
pip freeze > requirement
docker build -t novacollection:latest .
docker tag novacollection:latest registry.pinginglab.com:5000/beckend/novacollection:1.0
docker push registry.pinginglab.com:5000/beckend/novacollection:1.0