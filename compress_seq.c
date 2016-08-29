#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, const char * argv[]) {
    FILE *file = fopen(argv[1], "r");
    char line[1024];
    int base=0, pbase=0, cnt=0;
    char* tok;
    while (fgets(line, 1024, file)) {
        if (line[0]=='\n') { continue; }
        base=0; pbase=0; cnt=0;
        tok=strtok(line," ");
        base = atoi(tok); pbase=base;
        for (; tok!=NULL; tok=strtok(NULL," ")) {
            base = atoi(tok);
            if (base == pbase) {
                cnt++;
            } else {
                printf("%d %d ", cnt, pbase);
                pbase = base;
                cnt=1;
            }
        }
//printf("OKAY\n");
//        tok = strtok(NULL,"\n");
printf("%s\n",tok);
        base = atoi(tok);
printf("%d\n",base);
        if (base == pbase) {
            printf("%d %d\n", cnt+1, pbase);
        } else {
            printf("%d %d ", cnt+1, pbase);
            printf("1 %d\n", base);
        }
    }
    return 0;
}
