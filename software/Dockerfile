FROM lydbydissing/euphonium-builder:latest AS build

WORKDIR /workspace

## Install Python dependencies
COPY ./euphonium/requirements.txt /workspace/euphonium/requirements.txt
RUN pip install -r euphonium/requirements.txt

COPY . .
RUN mkdir -p euphonium/targets/cli/build \
    && make -j$(nproc) cli
RUN . /opt/esp/idf/export.sh \
    && pip install -r euphonium/requirements.txt \
    && make esp32
