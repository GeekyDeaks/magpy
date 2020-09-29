# Jupyter Notebook Magpylib Python Stack

Builds a docker image with Magpylib based on the Jupyter Notebook Scientific Python Stack `jupyter/scipy-notebook`

- https://github.com/jupyter/docker-stacks/tree/master/scipy-notebook
- https://magpylib.readthedocs.io/en/latest/

# Build

    docker build -t geekydeaks/magpylib .

# Running

    docker run -d --name magpylib -p 8888:8888 \
    --mount type=bind,source=$(pwd),target=/home/jovyan/nb \
    geekydeaks/magpylib:latest 

Get the URL + Token for notebook from the logs

    docker logs magpylib

Moseying around the container

    docker exec -it magpylib /bin/bash