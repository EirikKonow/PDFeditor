#!/usr/bin/env python3

import re
import pprint

def replacePDFcode(pdfIn, pdfOut, oldCode, newCode):
	with open(pdfIn, "rb") as myfile: #errors='ignore'
		pdfFile = myfile.read()
	#myfile.close()
	
	for i in range(len(pdfFile)-50):
		strings = str.encode("(/Yes)") #"".join(map(chr, pdfFile[i:i+6]))
		if strings in pdfFile[i:i+6]:
			print("Found yes!")
		#pass
#		print(i)
		#print("".join(map(chr, pdfFile[i:i+1])))
	#print("".join(map(chr, pdfFile[1:2])))

	syntax_code = r"{}".format(oldCode)

	fixed_pdfFile = re.sub(str.encode("\(/Yes\)"), str.encode(r"/Yes"), pdfFile, flags=re.M | re.S)

	outFile = open(pdfOut, "wb")
	outFile.write(fixed_pdfFile)
	outFile.close()

replacePDFcode("outPDF.pdf", "outPDF_fixed.pdf", "(/Yes)", "/Yes")