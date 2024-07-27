# build stage
ARG PYTHON_VERSION=3.10
FROM python:${PYTHON_VERSION}

WORKDIR /query-genie

COPY ./pyproject.toml ./pdm.lock 

# update system
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# install PDM
RUN pip install --no-cache-dir -U pip setuptools wheel pdm

ENV VENV_DIR /opt/venv/query-genie
ENV PATH ${VENV_DIR}/bin:${PATH}

ENV PYTHONPATH query-genie/.

RUN python -m venv ${VENV_DIR}

RUN pdm use -f ${VENV_DIR}

RUN pdm sync --prod --no-isolation --no-self
