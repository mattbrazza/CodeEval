#include <stdio.h>

int isprime(int num) {
    int i;
    for (i=2; i<num; i++) {
        if ((num%i)==0) { return 0; }
    }
    return 1;
}

int main(int argc, const char * argv[]) {
    int ans=0, cnt=0, num=1;

    while (cnt<=1000) {
        if (isprime(num)>0) {
            ans+=num;
            cnt++;
        }
        num++;
    }
    printf("%d\n",ans-1);
    return 0;
}

