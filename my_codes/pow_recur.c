#include <stdio.h>

int factorial(int n)
{
	if (n == 1)
		return (n);
	return (n * factorial(n - 1));

}
int main(void)
{
	int num, answer;


	printf("enter the number:\n");
	scanf("%d", &num);
	answer = factorial(num);
	
	printf("The factorial of %d is == %d\n", num, answer);
}
