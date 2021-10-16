def buy_sell(a):
    j=0
    profit=0

    for i in range(1,len(a)):
        if a[i]<a[i-1]:
            j=i
        if a[i-1]<a[i] and (i+1==len(a) or a[i]>a[i+1]):
            profit+=a[i]-a[j]
            print(f"buy on day {j+1} and sell on {i+1} ")
    print(" profit is ",profit)
a=[1, 5, 2, 3, 7, 6, 4, 5]
buy_sell(a)