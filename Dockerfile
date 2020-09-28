FROM jupyter/scipy-notebook

USER $NB_UID

RUN conda install magpylib
