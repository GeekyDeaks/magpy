# Jupyter Notebook MagPy Python Stack

Builds a docker image with MagPy based on the Jupyter Notebook Scientific Python Stack `jupyter/scipy-notebook`

https://github.com/jupyter/docker-stacks/tree/master/scipy-notebook

# Build

    docker build -t geekydeaks/magpylib .

# Running

    docker run -d --name magpylib -p 8888:8888 geekydeaks/magpylib:latest

    docker logs magpylib

    docker exec -it magpylib /bin/bash