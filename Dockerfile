FROM alpine:3.7
MAINTAINER yerikyu "yerik_shu@139.com"
ADD apps /code/
WORKDIR /code
RUN apk update && apk upgrade --update-cache --available\
    apk add --no-cache python3 &&\
    apk add --no-cache python3-dev &&\
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi &&\
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi &&\
    rm -rf /var/lib/apk/* &&\
    pip install -U pip &&\
    python install_requirement.py &&\
    rm -rf ~/.cache/pip && python -m pip uninstall pip -y