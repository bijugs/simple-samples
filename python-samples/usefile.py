def usefile(f):
  fh = open(f,'w')
  fh.write("Line 1\n")
  fh.write("Line 2\n")
  fh.close()
  fh = open(f,'r')
  for l in fh:
    print(l)
  fh.close()
