#include <stdio.h>
#include <string.h>

void search(char* pat, char* text){
    int m = strlen(pat);
    int n = strlen(text);

    for (int i = 0; i <= n-m; i++){
        int j;
        for (j = 0; j < m; j++){
            if(text[i+j] != pat[j]){
                break;
            }
        }
        if(j == m){
            printf("Pattern found at index of %d \n", i);
        }
    }
}
int main(void){
    char txt[] = "AABAACAADAABAABA";
    char pat[] = "AABA";

    search(pat, txt);
}
