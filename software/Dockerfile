FROM espressif/idf:release-v4.4 AS base

ADD https://github.com/Kitware/CMake/releases/download/v3.20.0/cmake-3.20.0.tar.gz /tmp
WORKDIR /tmp
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update \
    && apt-get install -y build-essential libssl-dev \
       libasound-dev libavahi-compat-libdnssd-dev
RUN tar -zxvf cmake-3.20.0.tar.gz \
    && cd cmake-3.20.0 \
    && ./bootstrap \
    && make -j$(nproc) \
    && make install \
    && rm -fr /tmp/cmake-3.20.0 /tmp/cmake-3.20.0.tar.gz

## Install PortAudio
ADD http://files.portaudio.com/archives/pa_stable_v190700_20210406.tgz /tmp
RUN tar -zxvf /tmp/pa_stable_v190700_20210406.tgz \
    && cd /tmp/portaudio/build \
    && cmake .. \
    && make -j$(nproc) \
    && make install \
    && rm -fr /tmp/portaudio /tmp/pa_stable_v190700_20210406.tgz

FROM base AS build

WORKDIR /workspace

## Install Python dependencies
COPY euphonium/requirements.txt euphonium/requirements.txt
RUN pip install -r euphonium/requirements.txt

COPY . .
RUN mkdir -p euphonium/targets/cli/build \
    && make -j$(nproc) cli
RUN . /opt/esp/idf/export.sh \
    && pip install -r euphonium/requirements.txt \
    && make esp32
