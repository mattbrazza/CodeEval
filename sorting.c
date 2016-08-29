#include <stdio.h>

void swap(int arr[], int a, int b) {
	int temp = arr[a]; arr[a] = arr[b]; arr[b] = temp; return; }

void bubble(int arr[], int n);
void quick(int arr[], int start, int end);
void merge(int arr[], int start, int end);

int main(int argc, char* argv[]){
	int arr[50], n, i;

	printf("Enter number of elements\n");
	scanf("%d", &n);
	printf("Enter %d integers\n",n);
	for (i=0; i<n; i++) {
		scanf("%d", &arr[i]);
	}

//	bubble(arr, n);
//	quick(arr, 0, n-1);
	merge(arr, 0, n);

	printf("Printing list:\n");
	for (i=0; i<n; i++) {
		printf("%d ", arr[i]);
	} printf("\n");

return 0;
}

void mergesort(int arr[], int ls, int le, int rs, int re) {
	int l_len = le - ls;
	int r_len = re - rs;
	int l_h[l_len];
	int r_h[r_len];
	int l=0, r=0, i=ls;
	
    // copy values into temporary lists
    for (i=ls; i<le; i++,l++) { l_h[l] = arr[i]; }
    for (i=rs; i<re; i++,r++) { r_h[r] = arr[i]; }

	for (i=ls, l=r=0; (l<l_len)&&(r<r_len); i++) {
//printf("L:%d, R:%d\n",arr[ls+l],arr[rs+r]);
		if (l_h[l] < r_h[r]) {
			arr[i] = l_h[l];
			l++;
		} else {
			arr[i] = r_h[r];
			r++;
		}
	}
	for (; l<l_len; i++,l++) { arr[i] = l_h[l]; }
	for (; r<r_len; i++,r++) { arr[i] = r_h[r]; }

	return;
}

void merge(int arr[], int start, int end) {
	if (end - start <= 1) { return; }
	int l_srt = start;
	int l_end = (start+end)/2;
	int r_srt = l_end;
	int r_end = end;

	merge(arr, l_srt, l_end);
	merge(arr, r_srt, r_end);
	mergesort(arr, l_srt, l_end, r_srt, r_end);

	return;
}

void quick(int arr[], int start, int end) {
	if (start < end) {
		int pivot_index = (start+end)/2;
		int pivot = arr[pivot_index];
		int chg, i, temp;

		swap(arr, pivot_index, end);
		for (i=chg=start; i<end; i++) {
			if (arr[i] < pivot) {
				swap(arr, i, chg);
				chg++;
			}
		}
		swap(arr, chg, end);
		quick(arr, start, chg - 1);
		quick(arr, chg + 1, end);
	}

	return;
}

void bubble(int arr[], int n) {
	int i, j;

	for (i=0; i<(n-1); i++) {
		for (j=0; j<n-i-1; j++) {
			if (arr[j] > arr[j+1]) {
				swap(arr, j, j+1);
			}
		}
	}

	return;
}

