FROM node:20 as build

RUN npm install -g vulcanize@1.16.0
WORKDIR /opt
COPY --chown=des:des ./ ./


RUN vulcanize static/des_components/elements.html \
    --exclude static/bower_components/polymer/lib/legacy/ \
    --out-html static/des_components/elements-built.html

FROM python:3.9

RUN pip install --no-cache-dir jira
RUN pip install --no-cache-dir netaddr
RUN pip install --no-cache-dir bcrypt
RUN pip install --no-cache-dir pyyaml
RUN pip install --no-cache-dir tornado==5.0.1
RUN pip install --no-cache-dir jsmin

## Copy source files
COPY --from=build /opt/ ./

CMD [ "bash", "start.sh" ]
