#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int read_input()
{
	char result[100];

	fgets(result, 200, stdin);
	return strlen(result);
}

int main(int argc, char** argv)
{
	int num_bytes = -1;
	puts("reading ...");
	num_bytes = read_input();
	printf("\nread %d bytes", num_bytes);
}
