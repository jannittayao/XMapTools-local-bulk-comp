import sys

def del_col(filename):
    """Cleans element map text file.

    :param str filename: file path for raw element map data
                         File name must have the format [Elem]_raw.txt where
                         [Elem] is replaced by the name of the element.
    """
    f = open(filename,"r")
    g = open(filename[:-8] + ".txt","w")

    lines = f.readlines()
    del lines[0:48] # <---- edit the end index depending on size of the header

    for line in lines:
        g.write("\t".join(line.split()[1:]) + "\n")

    f.close
    g.close

if __name__ == '__main__':
    del_col(*sys.argv[1:])
