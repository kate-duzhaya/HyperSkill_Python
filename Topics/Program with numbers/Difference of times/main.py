departure_h = int(input())
departure_m = int(input())
departure_s = int(input())
returned_h = int(input())
returned_m = int(input())
returned_s = int(input())

departure_total_s = departure_h * 3600 + departure_m * 60 + departure_s

returned_total_s = returned_h * 3600 + returned_m * 60 + returned_s

diff_s = returned_total_s - departure_total_s
print(diff_s)