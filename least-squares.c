#include <stdio.h>
#include <math.h>
#include <gmp.h>

void find_sum(long double x[], int n, mpf_t p)
{
	int i;
	mpf_t cur_term;
	mpf_init(cur_term);
	for (i = 0; i <n; i++)
	{
		mpf_set_d(cur_term, x[i]);
		mpf_add(p,p,cur_term);
	
		//mpf_out_str(stdout,10,10,p);
		//printf("\n");
	}
	
	/*printf("THISS");
	mpf_out_str(stdout,10,10,p);
	printf("\n------\n\n");*/
}
 
void find_sum_power(long double x[], int n, mpf_t p)
{
	int i = 0;
	mpf_t cur_term;
	mpf_t prod;
	mpf_init(cur_term);
	mpf_init(prod);
	
	for (i = 0; i <n; i++)
	{
		mpf_set_d(cur_term, x[i]);
		mpf_mul(prod, cur_term, cur_term);
		mpf_add(p,p,prod);
	}
}

void find_sum_two_variables(long double x[], long double y[], int n, mpf_t p)
{
	int i = 0;
	mpf_t cur_x;
	mpf_t cur_y;
	mpf_t prod;
	mpf_init(cur_x);
	mpf_init(cur_y);
	mpf_init(prod);
	
	for (i = 0; i <n; i++)
	{
		mpf_set_d(cur_x, x[i]);
		mpf_set_d(cur_y, y[i]);
		mpf_mul(prod, cur_x, cur_y);
		mpf_add(p,p,prod);
	}
}

struct a_record {
    int id;
    long double x;
    long double y;
};

int main()
{
	//mpf_set_default_prec(30);
	
	FILE* a_file = fopen("hist_a_specter.csv", "r");
	struct a_record records[601];
	int sid;
	double sx;
	double sy;
	size_t count;
	//for (count = 0; count < sizeof(records)/sizeof(records[0]); count++)
	for (count = 0; count < sizeof(records)/sizeof(records[0]); count++)
	{
		//int read_status = fscanf(a_file, "%d %lf %lf\n", &sid, &sx, &sy);
		int read_status = fscanf(a_file, "%d %Lf %Lf\n", &records[count].id, &records[count].x, &records[count].y);
		//printf("%d %Lf %Lf\n", records[count].id, records[count].x, records[count].y);
		if (read_status == 0) break; // wrong number of tokens - maybe end of file
	}
	 
	fclose(a_file);

	long double x[601], y[601];
	int i, n = 0;
	for (i = 0; i < 600; i++)
	{
		if (records[i].y != 0)
		{
			n += 1;
			x[i] = records[i].x;
			y[i] = log(records[i].y);
			//printf("ID = %lf, X = %Lf, Y = %Lf\n", records[i].id, records[i].x, records[i].y);
			//printf("X = %Lf, Y = %Lf\n", x[i], y[i]);
		}
	}
	
	
	/*BIG NUM STUFF*/
	
	mpf_t p, q, r, s, lam, det, c;
	mpf_t np, qq, nr, qs, qr, ps;
	
	mpf_init_set_ui(p, 0);
	mpf_init_set_ui(q, 0);
	mpf_init_set_ui(r, 0);
	mpf_init_set_ui(s, 0);
	
	mpf_init(np);
	mpf_init(qq);
	mpf_init(nr);
	mpf_init(qs);
	mpf_init(qr);
	mpf_init(ps);
	
	mpf_init(lam);
	mpf_init(det);
	mpf_init(c);
	
	printf("\n");
	find_sum_power(x, n, p);
	mpf_out_str(stdout,10,10,p);
	printf("\n");

	find_sum(x, n, q);
	mpf_out_str(stdout,10,10,q);
	printf("\n");
	
	find_sum_two_variables(x, y, n, r);
	mpf_out_str(stdout,10,10,r);
	printf("\n");
	
	find_sum(y, n, s);
	mpf_out_str(stdout,10,10,s);
	printf("\n");
	
	printf("------------------\n");
	
	mpf_mul_ui(np, p, n);
	mpf_mul(qq, q, q);
	mpf_mul_ui(nr, r, n);
	mpf_mul(qs, q, s);
	mpf_mul(qr, q, r);
	mpf_mul(ps, p, s);
	
	mpf_out_str(stdout,10,10,np);
	printf("\n");
	mpf_out_str(stdout,10,10,qq);
	printf("\n");
	mpf_out_str(stdout,10,10,nr);
	printf("\n");
	mpf_out_str(stdout,10,10,qs);
	printf("\n");
	mpf_out_str(stdout,10,10,qr);
	printf("\n");
	mpf_out_str(stdout,10,10,ps);
	printf("\n");
	printf("------------------\n");
	
	mpf_sub(det, np, qq);
	mpf_ui_div(det,1,det);
	
	mpf_sub(lam, nr, qs);
	mpf_mul(lam, det, lam);
	
	mpf_sub(c,ps,qr);
	mpf_mul(c,det,c);
	
	mpf_out_str(stdout,10,10,det);
	printf("\n");
	mpf_out_str(stdout,10,10,lam);
	printf("\n");
	mpf_out_str(stdout,10,10,c);
	printf("\n");
	printf("------------------\n");
	
	printf("\nThe slope of the line in the log space is:\t");
	mpf_out_str(stdout,10,10,lam);
	printf("\nThe intercept of the line in the log space is:\t");
	mpf_out_str(stdout,10,10,c);
	printf("\n\n");
}
