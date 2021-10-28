import sys
import os
def tfmapper():
  for line in sys.stdin:
    words = line.strip().split()
    for word in words:
      print "%s\t%s\t1" % (word,os.getenv('mapreducemap_csvfile','noname'))
if __name__ == '__main__':
  tfmapper()
  
def tfreducer():
  curprefix = None
  curcount = None
  for line in sys.stdin:
    word,filename,count = line.strip().split('\t')
    prefix = '%s\t%s' % (word,filename)
    if curprefix == None:
      curprefix = prefix
      curcount = eval(count)
    elif curprefix == prefix:
      curcount += eval(count)
    else:
      print "%s\t%s" % (curprefix,curcount)
      curprefix = prefix
      curcount = eval(count)
  print "%s\t%s" % (curprefix,curcount)
if __name__=='__main__':
  tfreducer()
  
  


def dfmapper():
  for line in sys.stdin:
    print "%s\t1" % line.strip()
if __name__ == '__main__':
  dfmapper()
  
  

def dfreducer():
  curword = None
  curcount = None
  space = []
  for line in sys.stdin:
    word,filename,wordcount,count = line.strip().split()
    prefix = "%s\t%s\t%s" %(word,filename,wordcount)
    if word == None:
      curword = word
      curcount = eval(count)
      space.append(prefix)
    elif curword == word:
      curcount += eval(count)
      space.append(prefix)
    else:
      for item in space:
        print "%s\t%d" % (item,curcount)
      curword = word
      curcount = eval(count)
      space = [prefix]
  for item in space:
    print "%s\t%d" % (item,curcount)
if __name__=='__main__':
  dfreducer()