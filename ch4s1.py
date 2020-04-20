from ch3s1 import single_xor_crack

def main():
    f = open("ch4s1data.txt") 
    linecount = 1
    for line in f:
        if not(linecount == 327):
            cipher = line[:-1].decode("hex")
        else : 
            cipher = line.decode("hex")
        print(linecount)
        single_xor_crack(cipher , 1)
        linecount += 1
        
if __name__ == "__main__":
    main()

#ln 171 , c = 53