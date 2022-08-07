all:
	@$(MAKE) -C docs html
	@$(MAKE) -C software esp32

clean:
	@$(MAKE) -C docs clean
	@$(MAKE) -C software clean
