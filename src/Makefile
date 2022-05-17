############################################################################
# Project: IVS 2022 - Calculator
# File: Makefile
# Date: 25.4.2022
# Last modify: 25.4.2022
# Author: Tomáš Hak xhakto01@stud.fit.vutbr.cz
#
# Description: Build script
############################################################################

INT           = python3
BIN           = main.py
ARCHIVE_NAME  = xdzuri00_xlizic00_xhakto01_xvilce00
REPO_NAME_NEW = repo
SOURCE_DIR    = $(shell basename `pwd`)
REPO_NAME_OLD = $(shell basename `cd ../ && pwd`)
TOP_LEVEL_DIR = $(shell basename `cd ../../ && pwd`)

.PHONY: all pack clean test doc run profile

all:

pack: clean
	cd ../../                                   && \
	mv $(REPO_NAME_OLD) $(REPO_NAME_NEW)        && \
	cd ../                                      && \
	mv $(TOP_LEVEL_DIR) $(ARCHIVE_NAME)         && \
	zip -r $(ARCHIVE_NAME).zip $(ARCHIVE_NAME)  && \
	mv $(ARCHIVE_NAME) $(TOP_LEVEL_DIR)         && \
	cd $(TOP_LEVEL_DIR)                         && \
	mv $(REPO_NAME_NEW) $(REPO_NAME_OLD)        && \
	cd $(REPO_NAME_OLD)/$(SOURCE_DIR)           && \
	mv ../../../$(ARCHIVE_NAME).zip ./

clean:
	rm -rf __pycache__ $(ARCHIVE_NAME).zip

test: test-op test-cal

test-op: test_operations.py
	$(INT) test_operations.py

test-cal: test_calculation.py
	$(INT) test_calculation.py

doc:
	doxygen Doxyfile

run:
	$(INT) $(BIN)

profile:
	pass

