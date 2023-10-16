h = '0x' + input()
for i in range(1,16):
    print(f"{h[2:]}*{format(i,'X')}={format(int(h,16)*i,'X')}")