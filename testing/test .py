import math
def daycount(y2, y1, m2, m1, d1, d2):
  x = 360 * (y2 - y1) + 30 * (m2-m1-1) + max(30-d1, 0) + min(d2, 30)
  return x

c_rate = 0.1
c_price = 111.2891
y2, m2, d2 = 1995, 3, 1 #maturaty date
y1, m1, d1 = 1993, 7, 1 #settlement date

all_day = daycount(y2, y1, m2, m1, d1, d2)
nc_date = 60

w = nc_date/all_day

print(w)
