#include <stdio.h>
#include <string.h>

int helper(char base[], char cue[], int bi, int ci);

int helper(char base[], char cue[], int bi, int ci) {
	if (ci > strlen(cue)) { return 1; }
	if (bi > strlen(base)) { return 0; }
	int ans=0;
	if (base[bi] == cue[ci]) {
		ans += helper(base, cue, bi+1, ci+1);
	}
	return ans+=helper(base, cue, bi+1, ci);
}

int main(int argc, const char * argv[]) {
	FILE *file = fopen(argv[1], "r"); char line[1024];
	char* base; char* cue;
	int ans=0;
	while (fgets(line, 1024, file)) {
		base = strtok(line,",");
		cue = strtok(NULL, "\n");
		ans = helper(base, cue, 0, 0);
		printf("%d\n",ans);
	}
return 0;
}

