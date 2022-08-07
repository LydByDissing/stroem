.DEFAULT_GOAL := esp32
JTAG_PORT ?= "/dev/ttyUSB0"

copy-config:
	@echo "Copying local cofig"
	cp -vuR config/* euphonium/

esp32: copy-config
	cd euphonium/targets/esp32; sh generate_full_build.sh;


flash-all: esp32
	@echo "flashing using this port '${JTAG_PORT}'"
	cd euphonium/targets/esp32; sh flash_all.sh ${JTAG_PORT};
