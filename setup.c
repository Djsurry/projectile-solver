#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <errno.h>

int main(){
	system("cp ./projectile /usr/local/bin");
		system("cp ./projectile /usr/bin");
	printf("All ready to go! Just open a terminal and write \"projectile\" to start the program!\n");
	return 0;
}
