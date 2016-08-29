#include <stdio.h>
#include <stdlib.h>

void fizzbuzz(int num){
	int i=0;
	
	for (i=0; i<num; i++) {
		if ((i%3!=0) && (i%5!=0)) {
			printf("%d", i);
		} else {
			if (i%3==0) { printf("fizz"); }
			if (i%5==0) { printf("buzz"); }
		}
		printf(", ");
	}
	printf("\n");

}

int main(int argc, char* argv[]) {
	int num;
	
	num = atoi(argv[1]);
	fizzbuzz(num);
return 0;
}
