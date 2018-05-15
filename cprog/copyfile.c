#include <stdio.h>



int main() {
char ch;


FILE *c, *test;
char f[10000];
c = fopen("<path>", "r");
test = fopen("<path>", "w");


 while( ( ch = fgetc(c) ) != EOF )
      fputc(ch, test);


//printf("%s\n" , f);
//fputs(f,test);
//printf("%s",f);

//printf("%s" , f);
fclose(c);
fclose(test);
}
