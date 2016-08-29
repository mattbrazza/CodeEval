#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(int argc, const char * argv[]) {
    FILE *file = fopen(argv[1], "r");
    char line[1024];
    int num, i, curr, cnt=0;
    while (fgets(line, 1024, file)) {
        if (line[0] == '\n') { continue; }
        num = atoi(line);
        i = log(num)/log(2);
        curr = pow(2, i);
		cnt = 0;
		while (num > 0) {
//printf("%d=%d=%d=%.2f=%d\n",num,curr,i,pow(2,i),cnt);
            if (num-curr >= 0) {
                num-=curr;
                cnt++;
            }
            i--;
            curr = pow(2,i);
        }
        printf("%d\n",cnt);
    }
    return 0;
}
/*
64  32  16  8   4   2   1
0   0   0   1   0   1   0 = 10
0   0   1   0   1   1   0 = 22
0   1   1   1   0   0   0 = 56
*/
