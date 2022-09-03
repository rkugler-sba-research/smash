#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <curses.h>
#include <termios.h>

#define USERNAME_LENGTH 255

struct _user
{
	char username[30];
	int id;
} typedef user;

user*
init_user(char* username, char* password)
{
	user* current_user;
	int password_correct = -1;

	// check user/password

	current_user = (user*)malloc(sizeof(user));
	strcpy(current_user->username, username);
	current_user->id = 1000;
	
	return current_user;
}

int
main(int argc, char** argv)
{
	char input_username[USERNAME_LENGTH];
	char* input_password;
	user* current_user = NULL;
	char choice = NULL;
	int repeat = 1;

	while(repeat)
	{
		fputs("Welcome! (l=login, w=whoami, x=logout, s=stats, e=exit)\n", stdout);
		choice = getchar();
		switch(choice)
		{
		case 'x':
			printf("logging out ...\n");
			current_user = NULL;
			break;
		case 's':
			printf("all normal\n");
			break;
		case 'w':
			printf("whoami\n");
			if(current_user != NULL)
			{
				printf(current_user->username);
			} else {
				printf("please log in first ...\n");
			}
			break;
		case 'l':
			fputs("username: ", stdout); fflush(stdout);
			fgets(input_username, USERNAME_LENGTH, stdin);
			input_password = getpass("Password: "); fflush(stdout);

			if((current_user = init_user(input_username, input_password)) != NULL)
			{
				fprintf(stdout, "you are authorized\n"); fflush(stdout);
				if(current_user->id == 0)
				{
					printf("you are root\n");
					execve("/bin/sh", NULL, NULL);
				} 
				else
				{
					printf("you are limited\n");
				}
				free(current_user);
			}
			else
			{
				fprintf(stderr, "Authentication failure\n");
			}
			break;
		case 'e':
			repeat = 0;
			break;
		}
		printf("------\n");
	}
}
