#!/usr/bin/env python3
def fib(n):
	if(n==0 or n==1):
		return n
	else:
		return fib(n-1)+fib(n-2)
		
n=int(input("Enter Number : "))
print("Their fib sum: :",fib(n))
