#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, const char * argv[]) {
	FILE *file = fopen(argv[1], "r");
	char line[1024];
	int temp, i, ender, tot;
	char* tok;
	int arr[50];
	while (fgets(line, 1024, file)) {
		temp=0; i=0; ender=0; tot=0;
		if (line[0]=='\n') { continue; }
		for (tok=strtok(line," "); strcmp(tok,"|")!=0; tok=strtok(NULL," ")) {
			temp = atoi(tok);
			arr[i] = temp; i++;
		}
		temp = atoi(tok);
		arr[i] = temp;
		tot = i;
		ender = atoi(strtok(NULL," "));
		for (i=0; i<tot; i++) { printf("%d ",arr[i]); } printf("\n");
		for (;ender>0;ender--) {
			for (i=1; i<tot; i++) {
				if (arr[i] < arr[i-1]) {
					temp = arr[i];
					arr[i] = arr[i-1];
					arr[i-1] = temp;
				}
			}
		}
		for (i=0; i<tot; i++) { printf("%d ",arr[i]); } printf("\n");
	}
return 0;
}
