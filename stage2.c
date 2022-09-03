#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>

// triggered manually
void debug_terminal()
{
	puts("recovery console active\n");
	system("/bin/sh");
}

int read_input()
{
	char result[100];

	//fscanf(stdin, "%n", result);
	gets(result);
	return strlen(result);
}

int main(int argc, char** argv)
{
	int num_bytes = -1;

	signal(SIGHUP, debug_terminal);
	puts("reading ...");
	num_bytes = read_input();
	printf("\nread %d bytes", num_bytes);
}
