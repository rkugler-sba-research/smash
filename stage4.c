#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int choose()
{
	char name[255];
	fgets(name, 255, stdin);
	printf("name=%s", name);
	printf(name);
}

int main(int argc, char** argv)
{
	while(1)
	{
		choose();
	}
}
