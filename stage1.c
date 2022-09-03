#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <curses.h>
#include <termios.h>

#define USERNAME_LENGTH 255

struct user
{
	char username[30];
	int id;
};

int
check_password(char* username, char* password)
{
	struct user current_user;
	int password_correct = -1;
	char recovery [] = { 's', '3', 'c', 'r', 'e', 't' };

	strcpy(current_user.username, username);
	current_user.id = 1000;
	if(strncmp(password, recovery, 6) == 0)
	{
		password_correct = 1;
	}
	// do stuff
	//
	//
	return password_correct;
}

int
main(int argc, char** argv)
{
	char input_username[USERNAME_LENGTH];
	char* input_password;

	fputs("Welcome!\n", stdout);
	fputs("username: ", stdout); fflush(stdout);
	fgets(input_username, USERNAME_LENGTH, stdin);
	input_password = getpass("Password: "); fflush(stdout);

	if(check_password(input_username, input_password) != -1)
	{
		fprintf(stdout, "you are authorized\n"); fflush(stdout);
		execve("/bin/sh", NULL, NULL);
	}
	else
	{
		fprintf(stderr, "Authentication failure\n");
	}
}
