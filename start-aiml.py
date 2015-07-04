import pyaiml
k = pyaiml.Kernel()
k.learn("D:\Portable\Portable Python 2.7.6.1\App\Lib\site-packages\pyaiml\std-startup.xml")
k.respond("LOAD AIML IRZA")
while True: print k.respond(raw_input("> "))

