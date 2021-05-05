words = ['sof','dru','pal']

d = {}
for w in words:
    s_w = ''.join(sorted(w))
    d[s_w] = w

print(d)