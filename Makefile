###################################################
#
# Makefile
#
###################################################

CC = gcc

CFLAGS = -Wall
CFLAGS += -O2

BINS = test_exec

all: $(BINS)

test_exec: test_exec.c
	$(CC) $(CFLAGS) -o $@ $<

clean:
	rm -f *.o *~ $(BINS)
