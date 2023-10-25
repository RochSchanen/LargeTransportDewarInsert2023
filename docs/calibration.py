
table = """
0.0 0.0 0.00%
1.0 1.1 0.88%
2.0 4.1 3.29%
3.0 8.6 6.86%
4.0 14.2 11.29%
5.0 20.3 16.12%
6.0 26.2 20.76%
7.0 31.8 25.26%
8.0 37.5 29.76%
9.0 43.2 34.26%
10.0 48.8 38.76%
11.0 54.5 43.25%
12.0 60.2 47.75%
13.0 65.8 52.25%
14.0 71.5 56.75%
15.0 77.2 61.24%
16.0 82.8 65.74%
17.0 88.5 70.24%
18.0 94.2 74.74%
19.0 99.8 79.24%
20.0 105.6 83.83%
21.0 111.7 88.66%
22.0 117.3 93.10%
23.0 121.8 96.68%
24.0 124.9 99.10%
25.0 126.0 100.00%
"""

data, i = [], -1
for l in table.split("\n"):

	# skip empty lines
	if not l: continue

	# add new line
	data.append([])
	i += 1
	
	# parse line
	for s in l.split(" "):
		# remove possible percent sign
		if s[-1] == "%": s = s[:-1]
		# convert to float
		data[i].append(float(s))

# get radius from volumes
from numpy import sqrt, pi
h0, v0, p0 = data[0]		# initial values
for h1, v1, p1 in data[1:]:
	dv = (v1-v0)*1E3		# delta volume in cc (from litres)
	dh = (h1-h0)*2.54		# delta height = 1 inch -> cm
	r = sqrt(dv/pi/dh) 		# radius in cm
	# print(f"{dh:6.2f}\t{dv:6.2f}\t{2*r:6.2f}")
	# print(f"{2*r:6.2f}")	# display diameter table in cm
	print(f"{r:6.2f}\t{h1*2.54:6.2f}")	# display radius vs height in cm
	h0, v0 = h1, v1

