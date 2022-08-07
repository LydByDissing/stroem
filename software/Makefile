.DEFAULT_GOAL := esp32
JTAG_PORT ?= "/dev/ttyUSB0"
COPY_FLAGS := -v -R
ifeq ($(OS),Windows_NT)
    #??
else
    UNAME_S := $(shell uname -s)
    ifeq ($(UNAME_S),Linux)
        COPY_FLAGS += -u
    endif
    ifeq ($(UNAME_S),Darwin)
        #COPY_FLAGS += -u
    endif
endif

copy-config:
	@echo "Copying local cofig"
	cp ${COPY_FLAGS} config/* euphonium/

esp32: copy-config
	cd euphonium/targets/esp32; sh generate_full_build.sh;


flash-all: esp32
	@echo "flashing using this port '${JTAG_PORT}'"
	cd euphonium/targets/esp32; sh flash_all.sh ${JTAG_PORT};
