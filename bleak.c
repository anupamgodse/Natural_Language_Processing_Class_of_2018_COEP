#include <stdio.h>

int count(int a) {
    int t=0;
    while(a) {
        if(a & 1) {
            t++;
        }
        a >>= 1;
    }  
    return t;
}

int ceiling2(int a) {
    int t=0;
    a--;
    while(a) {
        a>>=1;
        t++;
    }
    return t;
}

int isBleak(int a) {
    printf("%d\t%d\n", count(a), ceiling2(a));
    for(int i = a - ceiling2(a); i < a ; i++) {
        if(count(i) + i == a) {
            return 0;
        }    
    }
    return 1;
}

int main() {
	//code
	int n;
	
	scanf("%d", &n);
	
	int a;
	for(int i = 0; i < n; i++) {
        scanf("%d", &a);
        //isBleak(a);
        printf("%d\n", isBleak(a));
	}
	return 0;
}
