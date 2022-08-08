.DEFAULT_GOAL := esp32
JTAG_PORT ?= "/dev/ttyUSB0"
COPY_FLAGS := -v -R
CMAKE_BUILD_ARGS := -DHTTP_SERVER_PORT=8080

ifeq ($(OS),Windows_NT)
    #??
else
    UNAME_S := $(shell uname -s)
    ifeq ($(UNAME_S),Linux)
        COPY_FLAGS += -u
				CMAKE_BUILD_ARGS += -DCMAKE_CXX_STANDARD_LIBRARIES="-lX11 -ldl"
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

cli: copy-config
	cd euphonium/targets/cli/build; cmake ${CMAKE_BUILD_ARGS} ..;
	@$(MAKE) -C euphonium/targets/cli/build

flash-all: esp32
	@echo "flashing using this port '${JTAG_PORT}'"
	cd euphonium/targets/esp32; sh flash_all.sh ${JTAG_PORT};

clean: clean-cli clean-esp32

clean-cli:
	@$(MAKE) -C euphonium/targets/cli/build clean

clean-esp32:
	cd euphonium/targets/esp32; idf.py fullclean;
