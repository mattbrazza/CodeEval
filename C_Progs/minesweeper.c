#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[]) {
	FILE* file=fopen(argv[1],"r"); char line[1024];
	int m, n, i, j, q;
	char * ans, * org;

	while (fgets(line,1024,file)) {
		m = atoi(strtok(line,","));
		n = atoi(strtok(NULL,";"));
		org = strtok(NULL,"\n");
printf("%d-%d-%s",m,n,org);
		int mat[m][n];
		ans = malloc(sizeof(char)*m*n);
//		mat = malloc(sizeof(int*)*m);
//		for (i=0; i<m; i++) { mat = malloc(sizeof(int)*n); }
		i=0; j=0;
		for (q=0; q<strlen(org); q++) {
			mat[i][j] = (org[q] == '*') ? -10 : -1;
			j = (j == n) ? 0 : (j+1);
			i = (j == n) ? (i+1) : i;
		}
printf("--ARR:\n");
for (i=0; i<m; i++) { for (j=0; j<n; j++) { printf("%d\t",mat[i][j]); } printf("\n"); } printf("\n");

//		printf("%s",ans);
//		free(mat);
		free(ans);
	}
	return 0;
}

/*
**...
.....
.*...

**100
33200
1*100


*...
....
.*..
....

*100
2210
1*10
1110
*/

