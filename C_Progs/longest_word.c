#include <stdio.h>
#include <string.h>

int main(int argc, const char * argv[]) {
    FILE *file = fopen(argv[1], "r");
    char line[1024];
    while (fgets(line, 1024, file)) {
        if (line[0]=='\n') { continue; }
        char* tok = strtok(line," ");
		char* ans = tok;
        int len = strlen(tok); int tlen=len, i=0;
//printf("%s=%d\n",tok,len);
        for (; tok!=NULL; tok=strtok(NULL," \n")) {
			tlen = strlen(tok);
//printf("%s=%d\n",tok,tlen);
            if (tlen > len) {
                len = tlen;
                ans = tok;
            } else {}
        }
        printf("%s\n",ans);
    }
    return 0;
}
