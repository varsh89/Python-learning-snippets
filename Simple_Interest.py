import math
def simple_interest(principal:float, rateofinterest:float, time:float) -> int:
    si=(principal * rateofinterest * time)/100
    return math.floor(si)
def main():
    principal=float(input().strip())
    rateofinterest=float(input().strip())
    time=float(input().strip())
    result=simple_interest(principal,rateofinterest,time)
    print(result)
if __name__=="__main__":
    main()
