FROM node:20 as build

# RUN apt-get update &&   \
#   apt-get install -y    \
#     python3-pip         \
#     wget                \
#   && rm -rf /var/lib/apt/lists/*

# Basic python reqs
# RUN pip3 install --no-cache-dir jira
# RUN pip3 install --no-cache-dir netaddr
# RUN pip3 install --no-cache-dir bcrypt
# RUN pip3 install --no-cache-dir pyyaml
# RUN pip3 install --no-cache-dir tornado==5.0.1
# RUN pip install --no-cache-dir jsmin

# WORKDIR /tmp
# ADD https://nodejs.org/dist/v12.14.1/node-v12.14.1-linux-x64.tar.xz 
# RUN tar -C /usr/local --strip-components 1 -xf /tmp/node-v12.14.1-linux-x64.tar.xz
RUN npm install -g vulcanize@1.16.0

# RUN useradd --create-home --shell /bin/bash des --uid 1001
# USER des
WORKDIR /opt
COPY --chown=des:des ./ ./

RUN vulcanize static/des_components/elements.html \
    --exclude static/bower_components/polymer/lib/legacy/ \
    --out-html static/des_components/elements-built.html

FROM jekyll/jekyll:3.8
## Currently jekyll/jekyll:4 fails with the error below so tag 3.8 is used instead.

ENV JEKYLL_UID=1000
ENV JEKYLL_GID=1000

USER ${JEKYLL_UID}

## Install required gems
COPY ./Gemfile ./Gemfile
RUN bundle install

## Copy source files
COPY --from=build --chown=${JEKYLL_UID}:${JEKYLL_GID} /opt/ ./

CMD ["bundle", "exec", "jekyll", "serve", "--host=0.0.0.0", "--watch", "--drafts"]
