forecasts = open("forecasts_test_new.csv", "r").readlines()

old_value = 1
new_list = []
for f in forecasts[1:]:
    strpf = f.replace('"','').strip()
    new_str = "%s,%s\n" % (strpf, old_value)
    newspl = new_str.strip().split(",")
    final_str = "%s,%s\n" % (newspl[0], newspl[2])
    final_str = final_str.replace('"','')
    old_value = f.strip().split(',')[1]
    new_list.append(final_str)

out = open("forecasts_new.csv", "w")
for n in new_list:
    out.write(n)