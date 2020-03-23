# Usage:
# make        # run the makefile
# make clean  # remove ALL textfiles on the server

.PHONY = all run-all run-server run-client test-all test-server clean

LANGUAGE = python   # program language to use
SERVER_PATH = server/src/
SERVER_FILE = server.py
CLIENT_PATH = client/src/
CLIENT_FILE = menu.py
TEST_PATH = server/tests/
TEST_FILE = test.py

all: detected_OS run-all test-all

# Detect operating system in Makefile
detected_OS:
    ifeq ($(OS), Windows_NT) # XP, 2000, 7, Vista, 10
        detected_OS := Windows
    else
        detected_OS := $(shell uname)
    endif
    
#    ifeq ($(detected_OS), Windows)
#        OS_FLAG += -D WIN32
#    endif
#    ifeq ($(detected_OS), Darwin)   # Mac OS X
#        OSFLAG += -D OSX
#    endif
#    ifeq ($(detected_OS), Linux)
#        OS_FLAG += -D LINUX
#    endif

run-all:
    ifeq ($(detected_OS), Windows)
        set FLASK_APP = $(SERVER_PATH)$(SERVER_FILE) flask run
    else
        export FLASK_APP = $(SERVER_PATH)$(SERVER_FILE) flask run
    endif
    $(LANGUAGE) $(CLIENT_PATH)$(CLIENT_FILE)
  
run-server:
    env FLASK_APP = $(SERVER_PATH)$(SERVER_FILE) flask run
  
run-client:
    $(LANGUAGE) $(CLIENT_PATH)$(CLIENT_FILE)
  
test-all:
    @touch "bla bla bla..." > file_on_server.txt
    @echo "file_on_server.txt has been created"
    $(LANGUAGE) $(TEST_PATH)$(TEST_FILE)
    @rm file_on_server.txt
    @echo "file_on_server.txt has been deleted"

test-server:
    $(LANGUAGE) $(TEST_PATH)$(TEST_FILE)

clean:
    @echo "Cleaning up on the server..."
    rm $(SERVER_PATH)*.txt
