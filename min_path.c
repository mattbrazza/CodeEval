#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int helper(int mat[], int i, int j, int n) {
	if (i+j == 0) { return mat[0]; }
	if (i < 0) { return -99999; }
	if (j < 0) { return -99999; }
	int ans1, ans2, ans;
	ans1 = helper(mat, i-1, j, n);
	ans2 = helper(mat, i, j-1, n);
	if (ans1 < 0) { return (ans2+mat[(i*n)+j]); }
	if (ans2 < 0) { return (ans1+mat[(i*n)+j]); }
	ans = (ans1 < ans2) ? ans1 : ans2;
	return (ans+mat[(i*n)+j]);
}

int main(int argc, const char * argv[]) {
	FILE *file = fopen(argv[1],"r"); char line[1024];
	int iter=0, n, ans, i, j;
	int* mat; char* num;

	while (fgets(line, 1024, file)) {
		if (iter<1) {
			n = atoi(line);
			mat = malloc(sizeof(int)*n*n);
			i=0; j=0; ans=0;
			iter = n;
			continue;
		} else {}

		num = strtok(line,",");
		mat[(i*n)+0] = atoi(num);
		for (j=1; j<n-1; j++) {
			num = strtok(NULL,",");
			mat[(i*n)+j] = atoi(num);
		}
		num = strtok(NULL,"\n");
		mat[(i*n)+j] = atoi(num);

		i++;
		iter--;
		if (iter==0) {
			ans = helper(mat, n-1, n-1, n);
			printf("%d\n",ans);
			free(mat);
		}
	}
return 0;
}

