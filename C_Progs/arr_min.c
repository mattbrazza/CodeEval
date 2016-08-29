#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int helper(int orig[], int start, int end, int n) {
	int i, temp, stop=1;
	int sz = (sizeof(int)*(end-start));

	int* m = malloc(sz);
	memcpy(m, orig+start, sz);

printf("===O====\n"); for (i=9; i<n; i++) { printf("%d ",orig[i]); } printf("\n");
printf("===M====\n"); for (i=start; i<end; i++) { printf("%d ",m[i]); } printf("\n");

	while (stop>0) { stop=0;
	for (i=start; i<end; i++) {
		if (m[i] > m[i+1]) {
			temp = m[i];
			m[i] = m[i+1];
			m[i+1] = temp;
			stop++;
		}
	}
	}
	for (i=start; i<end; i++) {
		if (m[i] != m[i+1]-1) { return (m[i]+1); }
	}
	temp = ((m[start]-1)>0) ? (m[start]-1) : (m[i]+1);
	return temp;
}

int main(int argc, char* argv[]) {
	FILE * file = fopen(argv[1],"r"); char line[1024];
	int n,k,a,b,c,r, i;
	int* m;
	
	while (fgets(line, 1024, file)) {
		n =atoi(strtok(line,","));
		k =atoi(strtok(NULL,","));
		a =atoi(strtok(NULL,","));
		b =atoi(strtok(NULL,","));
		c =atoi(strtok(NULL,","));
		r =atoi(strtok(NULL,"\n"));
		m = malloc(sizeof(int)*n);
		m[0] = a;
		for (i=1; i<k; i++) { m[i] = (b*m[i-1]+c)%r; }
m[i] = (b*m[i-1]+c)%r;
for (i=0; i<k; i++) { printf("%d ",m[i]); } printf("\n");
		for (i=k; i<n; i++) {
			m[i] = helper(m,i-k,i,n);
		}
printf("\n"); for (i=0; i<n; i++) { printf("%d ",m[i]); } printf("\n");
		printf("%d\n",m[n-1]);
		return 0;
	}
	return 0;
}
