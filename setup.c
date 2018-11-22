#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <errno.h>

int main(){
	DIR* dir = opendir("/usr/local/bin");
        if (dir)
	{
	system("mv ./projectile /usr/local/bin");
    	closedir(dir);
	}
	else if (ENOENT == errno)
	{
		system("mv ./projectile /usr/bin");
	}
	system("mv ./projectile /usr/local/bin");
	printf("All ready to go! Just open a terminal and write \"projectile\" to start the program!\n");
	return 0;
}
