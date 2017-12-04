/*c program demonstrating fscanf and its usage*/
#include<stdio.h>
int main()
{
    FILE* ptr = fopen("hist_a_specter.csv", "r");
    if (ptr==NULL)
    {
        printf("no such file.");
        return 0;
    }
 
    /* Assuming that abc.txt has content in below
       format
       NAME    AGE   CITY
       abc     12    hyderbad
       bef     25    delhi
       cce     65    bangalore */
    char* buf[100];
    int id;
    double x;
    double y;
    char str[50];
    char a[20], b[20], c[20];
    while (fscanf(ptr,"%s %s %s", &str)==1)
	{
		printf("We here\n");
        printf("%s", str);
    }
 
    return 0;
} 
