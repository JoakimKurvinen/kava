import subprocess

f = open("filewritetest.txt","w+")
#det=subprocess.call(["date"])
det=subprocess.Popen("date", stdout=subprocess.PIPE)
dit= det.stdout.read()
f.write("%s" %dit)
#f.write("24")
f.close()
