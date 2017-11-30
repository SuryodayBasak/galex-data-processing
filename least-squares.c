#include <stdio.h>
#include <math.h>

double find_sum(double x[], int n)
{
	int i;
	double sum = 0.0;
	for (i = 0; i <n; i++)
	{
		sum += x[i];
	}
	return sum;
}
 
double find_sum_power(double x[], int n)
{
	int i = 0;
	double sum = 0.0;
	for (i = 0; i <n; i++)
	{
		sum += x[i]*x[i];
	}
	return sum;
}

double find_sum_two_variables(double x[], double y[], int n)
{
	int i = 0;
	double sum = 0.0;
	for (i = 0; i <n; i++)
	{
		sum += x[i]*y[i];
	}
	return sum;
}

struct a_record {
    int id;
    double x;
    double y;
};

int main()
{
	FILE* a_file = fopen("hist_a_specter.csv", "r");
	struct a_record records[601];
	size_t count;
	for (count = 0; count < sizeof(records)/sizeof(records[0]); count++)
	{
		int read_status = fscanf(a_file, "%d,%lf,%lf", &records[count].id, &records[count].x, &records[count].y);
		if (read_status != 2) break; // wrong number of tokens - maybe end of file
	}
	fclose(a_file);

	double x[601], y[601];
	int i, n = 0;
	for (i = 0; i < 601; i++)
	{
		if ((records[i].y != 0) || (records[i].y != 0))
		{
			n += 1;
			x[i] = records[i].x;
			y[i] = log(records[i].y);
		}
	}

	double p, q, r, s, lambda, det;
	long double c;
	//int n;
	//double x[5] = {1,2,3,4,5};
	//double y[5] = {12,24,31,46,52};
	
	//n = sizeof x / sizeof x[0];
	p = find_sum_power(x, n);
	q = find_sum(x, n);
	r = find_sum_two_variables(x, y, n);
	s = find_sum(y, n);
	det = 1/((n*p) - (q*q));
	lambda = det*((n*r) - (q*s));
	c = det*(-(q*r) + (p*s));
	
	printf("Det = %lf, Lambda = %lf, C = %Lf\n", det, lambda, c);
	printf("p = %lf\nq = %lf\nr = %lf\ns = %lf\n", p,q,r,s);
}
