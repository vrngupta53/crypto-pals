def main():
    f = open("ch8s1data.txt")
    hextext = f.read()
    string_list = hextext.split()
    max = 0    
    max_ind = -1
    max_string = ""
    ind = 0
    for hexstring in string_list:
        string = hexstring.decode("hex")
        ctr = 0
        for i in range(len(string)/16):
            for j in range(i+1,len(string)/16):
                if(string[16*i:16*(i+1)] == string[16*j:16*(j+1)]):
                     ctr += 1
        if(ctr > max):
            max = ctr
            max_string = string
            max_ind = ind
        ind += 1
    print(max_ind)
    print(max_string.encode("hex"))
    print(max)

if(__name__ == "__main__"):
    main()