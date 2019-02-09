#!/usr/bin/env python3

import re

def replacePDFcode(pdfIn, pdfOut, oldCode, newCode):
	with open(pdfIn, "rb") as myfile: #errors='ignore'
		pdfFile = myfile.read()
	#myfile.close()
	oldCode = re.escape(oldCode)
	newCode = re.escape(newCode)

	"""
	count = 0
	print(len(pdfFile))
	for i in range(len(pdfFile)-50):
		strings = str.encode("(/You)") #"".join(map(chr, pdfFile[i:i+6]))
		if strings in pdfFile[i:i+6]:
			count = count + 1
	print("Found {} instances of {}".format(count, oldCode))
	"""
		#pass
		#print(i)
		#print("".join(map(chr, pdfFile[i:i+1])))
	#print("".join(map(chr, pdfFile[1:2])))

	syntax_code = r"{}".format(oldCode)

	fixed_pdfFile = re.sub(str.encode(oldCode), str.encode(newCode), pdfFile, flags=re.M | re.S)

	outFile = open(pdfOut, "wb")
	outFile.write(fixed_pdfFile)
	outFile.close()

if __name__=="__main__":
	replacePDFcode("outPDF.pdf", "outPDF_fixed.pdf", "(/Yes)", "/Yes")