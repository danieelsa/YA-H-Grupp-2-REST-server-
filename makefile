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

all: run-all test-all

run-all:
    env FLASK_APP = $(SERVER_PATH)$(SERVER_FILE) flask run
    $(LANGUAGE) $(CLIENT_PATH)$(CLIENT_FILE)
  
run-server:
    env FLASK_APP = $(SERVER_PATH)$(SERVER_FILE) flask run
  
run-client:
    $(LANGUAGE) $(CLIENT_PATH)$(CLIENT_FILE)
  
test-all:
    $(LANGUAGE) $(TEST_PATH)$(TEST_FILE)

test-server:
    $(LANGUAGE) $(TEST_PATH)$(TEST_FILE)

clean:
    @echo "Cleaning up on the server..."
    rm $(SERVER_PATH)*.txt
