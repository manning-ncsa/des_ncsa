FROM node:20 AS build

RUN npm install -g vulcanize@1.16.0
WORKDIR /opt
COPY --chown=des:des ./ ./


RUN vulcanize static/des_components/elements.html \
    --exclude static/bower_components/polymer/lib/legacy/ \
    --out-html static/des_components/elements-built.html

FROM python:3.9

COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

## Copy source files
COPY --from=build /opt/ ./

CMD [ "bash", "start.sh" ]
