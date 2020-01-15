/*
 * Just a simple program to test the IoT_Network
 * It receives an input from a client and returns a hello world response.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (int argc, char **argv)
{
    fprintf(stdout, "This is the C program, number is %d\n", atoi(argv[1]));
    return 0;
}
