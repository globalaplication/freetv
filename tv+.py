import os
import urllib
ln = "https://raw.githubusercontent.com/globalaplication/freetv/master/ln.tv"
fl = "./ln.tv"
clist = dict()
def channelList():
	global ln, fl
	if os.path.exists(fl) is False:
		source = urllib.urlopen(ln).read().splitlines()
		for line in source:
			host, request = ("https://www.youtube.com",
			"/videos?view=2&flow=grid")
			channel = line.split(":")[-2]
			ln = "{}{}{}".format(host, 
			line.split(":")[-1], 
			request)
			with open (fl, "a") as w:
				w.write("{}::{}\n".format(
				channel, ln))
def openChannel(cindex):
	global clist
	for enum, test in enumerate(open(fl),1):		
		clist[enum] = {"channel":test.split("::")[-2], 
		"ln": test.split("::")[-1][0:-1]}
	source = urllib.urlopen(clist.get(cindex)["ln"]).readlines() 
	for x in source:
		if x.find("data-context-item-id") > -1:
			start = x.find('"')+1
			end = x.find('"', start) 
			string = """<iframe width='{}' height='{}' 
src='https://www.youtube.com/embed/{}?rel=0&amp;controls=0&amp;showinfo=0&amp;autoplay={}' 
frameborder='0'>
</iframe>""".format(500,500, x[start:end], 0)
	with open ("./tv.html", "w") as frame:
		frame.write(string)
	return clist.get(cindex)
def view(cindex):
	li = False
	for enum, test in enumerate(open(fl),1):		
		clist[enum] = {"channel":test.split("::")[-2], 
		"ln": test.split("::")[-1][0:-1]}
	live = urllib.urlopen(clist.get(cindex)["ln"]).read() #canli yayindami?
	source = live.splitlines()	
	if live.find("yt-badge-live") > -1: 
		li = True		
	for v in source:
		if v.find("yt-lockup-meta-info") > -1:
			start = v.find("<li>")+4
			end = v.find(chr(32), start)
			output = {"yt-badge-live":li, "views":v[start:end], 
			"channel":clist.get(cindex)
			["channel"]}
			if li is False:
				output = {"yt-badge-live":li, 
				"views":-1, 
				"channel":clist.get(cindex)
				["channel"]}
			break
	return output
def info():
	return

channelList() #baslangicta (bir defa) calisacak olan fonksiyon!

print openChannel(1) #1.kanali ac
#print view(1) #izlenme sayisi
