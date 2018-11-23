#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <errno.h>
#include <limits.h>
#include <unistd.h>

int main(){
        char cwd[PATH_MAX];
        getcwd(cwd, sizeof(cwd));

        char* del = "rm -Rf ";
        system("mkdir /usr/local/bin");
        system("echo '/usr/local/bin' >> /etc/paths");
	system("cp ./projectile /usr/local/bin");
	printf("All ready to go! Just open a terminal and write \"projectile\" to start the program!\n");
        system("rm ../projectile.zip");
        strcat(del, cwd);
        system(del);
	return 0;
}
