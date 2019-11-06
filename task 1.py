def year(a):
    if a%4==0 and a%400==0:
        print('bissextible year')
    else:
        print('usual year')
year(2000)