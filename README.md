DES Data Management (DESDM) public data release website
========================================================

This repository is the source code for the DESDM public data release website at https://des.ncsa.illinois.edu/.

Workflow for contributing content updates
----------------------------------------------

0. [Install `docker`](https://docs.docker.com/engine/install/) and `git`.
1. Fork the repo `https://github.com/des-labs/des_ncsa` to `https://github.com/$GITHUB_USER/des_ncsa` where `$GITHUB_USER` is your GitHub account username.
2. Clone your fork locally and create a `dev-$RELEASE_NAME` branch, where `$RELEASE_NAME` is some short meaningful name like `dr2` or `y6bao`.
    ```shell
    CLONE_DIR="$HOME/src/$GITHUB_USER/des_ncsa"
    git clone https://github.com/$GITHUB_USER/des_ncsa $CLONE_DIR
    cd $CLONE_DIR
    git checkout -b dev-$RELEASE_NAME
    ```
    
3. Build the Docker image.
    ```shell
    docker build . -t desdm-public --platform linux/x86_64
    ```
4. Configure the webserver to run in "development mode".
    ```shell
    docker run --rm -d --name desdm-public --platform linux/x86_64 \
        -p 8888:8080 \
        -v $(pwd):/home/des \
        -u $(id -u) \
        -e DEBUG_ENABLED="true" \
         desdm-public
    ```
5. Open your browser to http://127.0.0.1:8888 to view the website.
6. Edit and save the relevant HTML files. Reload the page and see the results. Repeat this step until satisfied.
7. Commit only the substantive changes to the Git repo and push the updates to your GitHub fork.
    ```shell
    git add [path/to/file_1] [path/to/file_2] [...]
    git commit -m 'Updated release page blah'
    git push origin dev-$RELEASE_NAME
    ```
8. Create a pull request to merge and publish your changes. You must [inform the DES Science Release community via the #sci-release Slack channel](https://darkenergysurvey.slack.com/archives/C0PMTCWRL) to allow for a peer review of the submission before it can be accepted. 
