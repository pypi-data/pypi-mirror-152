# syntax=docker/dockerfile:experimental
FROM swernst/cauldron:current-ui-standard

COPY requirements.txt /build_data/requirements.txt

RUN pip install --upgrade pip \
 && pip install -r /build_data/requirements.txt

COPY graph_polisher /project/graph_polisher
COPY notebooks /project/notebooks

WORKDIR /project
