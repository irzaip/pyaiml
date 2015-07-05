import re

def strip_punc(tostrip):
    a = tostrip
    a = re.sub('[,./;:"-=+_!@#$%^&*()?{}\']','',a)
    return a

def oneline():
    f = open("peribahasa.txt","r")
    while True:
      print "<li>" + f.readline().rstrip() + "</li>"
      f.readline()
      f.readline()

def twoline():
    f = open("peribahasa.txt","r")
    while True:
      t = strip_punc(f.readline().rstrip())
    
      print "<category>"
      print "  <pattern>*</pattern>"
      print "  <that>" + t.upper() + "</that>"
      print "  <template>Artinya "+ f.readline().rstrip() +"</template>"
      print "</category>"
      f.readline()
    
    
print "Use oneline(), twoline() ... put peribahasa.txt in root"
