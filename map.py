import sys

def del_col(filename):
    f = open(filename,"r")
    g = open(filename[:-8] + ".txt","w")

    lines = f.readlines()
    del lines[0:48]

    for line in lines:
        g.write("\t".join(line.split()[1:]) + "\n")

    f.close
    g.close

if __name__ == '__main__':
    del_col(*sys.argv[1:])
