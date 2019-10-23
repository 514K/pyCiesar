#include<stdio.h>
#include<locale.h>
#include<wchar.h>
#include<string.h>
#include <stdlib.h>
int main(){
    setlocale(LC_ALL,"Russian");
    wchar_t ch[100];
    //memset(ch,0,sizeof(ch));
    wscanf(L"%s", ch);
    for (int i = 0; i<10; i++){
        wprintf(L"%d ", ch[i]);
    }
    ch[0] = L'а';
    ch[1]++;
    wprintf(L"\n%s %d\n", ch, ch[0]);
    for (int i = 0; i<10; i++){
        wprintf(L"%d ", ch[i]);
    }
    
    
    
    
    /*if ((f=_wfopen(L"C:\\Users\\SAS\\Documents\\sas.txt", L"r+"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }
    wchar_t a[100];
    fgetws(a, 100, f);
    
    for (int i = 0; i < 101; i++) wprintf(L"%c",a[i]);
    fclose(f);*/
    
    /*wchar_t a = L'а';
    wprintf(L"%c %d\n",a,a);
    wchar_t u;
    u = getwchar();
    u += 16;
    wprintf(L"%d %c\n",u, u);
    if (u>=L'а' && u<=L'я'){ wprintf(L"Поздравляю, вы русский, с вами бог\n");}
    for (int i = 1072; i < 1104; i++) {
        u = i;
        wprintf(L"%c ",u);
    }*/

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    /*wchar_t c[1000];
    memset(c,0,sizeof(c));
    c[0] = L'ф';
    wprintf(L"%c\n",c[0]);
    wscanf(L"%s",&c);
    wprintf(L"%s\n",c);

    for (int i = 0; i < 1000; i++){
        wprintf(L"%c",c[i]);
    }
    printf("\n");*/
    
    
    
    
    
    
    /*wchar_t *b;
    b = (wchar_t*)malloc(k*sizeof(int));*/
    return 0;
}