# 1) choose base container
# generally use the most recent tag

# data science notebook
# https://hub.docker.com/repository/docker/ucsdets/datascience-notebook/tags
ARG BASE_CONTAINER=ucsdets/datascience-notebook:2020.2-stable

# scipy/machine learning (tensorflow)
# https://hub.docker.com/repository/docker/ucsdets/scipy-ml-notebook/tags
# ARG BASE_CONTAINER=ucsdets/scipy-ml-notebook:2020.2-stable

FROM $BASE_CONTAINER

LABEL maintainer="UC San Diego ITS/ETS <ets-consult@ucsd.edu>"

# 2) change to root to install packages
USER root

# 3) install packages
RUN	apt-get install -y htop && \
    apt-get install -y aria2 && \
    apt-get install -y nmap && \
    apt-get install -y traceroute 

RUN conda install --yes geopandas 
RUN conda install --yes bokeh
RUN pip install --no-cache-dir babypandas
RUN pip install --no-cache-dir geopy
RUN pip install --no-cache-dir scikit-learn
RUN pip install --no-cache-dir networkx scipy python-louvain
RUN pip install --no-cache-dir pymavlink
RUN pip install --no-cache-dir dronekit-sitl
RUN pip install --no-cache-dir mavproxy

# 4) change back to notebook user
COPY /run_jupyter.sh /
USER $NB_UID

# Override command to disable running jupyter notebook at launch
# CMD ["/bin/bash"]
