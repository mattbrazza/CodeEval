#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, const char * argv[]) {
    FILE *file = fopen(argv[1], "r");
    char line[1024];
    char cmd[8];
    int x=0, i=0, j=0, ans=0;
	int BOARD[256][256];
    
    for (i=0; i<256; i++) { bzero(BOARD[i], 256); }
    while (fgets(line, 1024, file)) {
        sscanf(line, "%s %d %d\n", cmd, &i, &x);
        ans=0;
//printf("=>%s, %d, %d\n",cmd, i, x);
        if (strcmp(cmd,"SetRow")==0) {
            for (j=0; j<256; j++) { BOARD[i][j]=x; }
        } else if (strcmp(cmd,"SetCol")==0) {
            for (j=0; j<256; j++) { BOARD[j][i]=x; }
        } else if (strcmp(cmd,"QueryRow")==0) {
            for (j=0; j<256; j++) { ans+=BOARD[i][j]; }
            printf("%d\n",ans);
        } else if (strcmp(cmd,"QueryCol")==0) {
            for (j=0; j<256; j++) { ans+=BOARD[j][i]; }
            printf("%d\n",ans);
        } else {}
    }
    return 0;
}

