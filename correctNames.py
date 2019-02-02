#! /usr/bin/python

import os
import pdfrw
import math
from pprint import pprint

INVOICE_TEMPLATE_PATH = 'inPDF.pdf'
INVOICE_OUTPUT_PATH = 'inPDF_fixed.pdf'


ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'

# This dict has the old name as key and the new one as item.
# {"Old name": "The name it will get"}
box_dict = {
	"Check Box 11": "ST STR box",
	"Check Box 12": "DS success 1",
	"Check Box 13": "DS success 2",
	"Check Box 14": "DS success 3",
	"Check Box 15": "DS failure 1",
	"Check Box 16": "DS failure 2",
	"Check Box 17": "DS failure 3",
	"Check Box 18": "ST DEX box",
	"Check Box 19": "ST CON box",
	"Check Box 20": "ST INT box",
	"Check Box 21": "ST WIS box",
	"Check Box 22": "ST CHA box",
	"Check Box 23": "Acrobatics box",
	"Check Box 24": "Animal Handling box",
	"Check Box 25": "Arcana box",
	"Check Box 26": "Athletics box",
	"Check Box 27": "Deception box",
	"Check Box 28": "History box",
	"Check Box 29": "Insight box",
	"Check Box 30": "Intimidation box",
	"Check Box 31": "Investigation box",
	"Check Box 32": "Medicine box",
	"Check Box 33": "Nature box",
	"Check Box 34": "Perception box",
	"Check Box 35": "Performance box",
	"Check Box 36": "Persuasion box",
	"Check Box 37": "Religion box",
	"Check Box 38": "Sleight of Hand box",
	"Check Box 39": "Stealth box",
	"Check Box 40": "Survival box",
	"DEXmod ": "DEXmod",
	"CHamod": "CHAmod",
	"Race ": "Race",
	"Wpn2 Damage ": "Wpn2 Damage",
	"Wpn2 AtkBonus ": "Wpn2 AtkBonus",
	"Wpn3 AtkBonus  ": "Wpn3 AtkBonus",
	"Wpn3 Damage ": "Wpn3 Damage",
	"PersonalityTraits ": "PersonalityTraits",
	"Acrobatics": "Acrobatics Dex",
	"Animal": "Animal Handling Wis",
	"Arcana": "Arcana Int",
	"Athletics": "Athletics Str",
	"Deception ": "Deception Cha",
	"History ": "History Int",
	"Insight": "Insight Wis",
	"Intimidation": "Intimidation Cha",
	"Investigation ": "Investigation Int",
	"Medicine": "Medicine Wis",
	"Nature": "Nature Int",
	"Perception ": "Perception Wis",
	"Performance": "Performance Cha",
	"Persuasion": "Persuasion Cha",
	"Religion": "Religion Int",
	"SleightofHand": "Sleight of Hand Dex",
	"Stealth ": "Stealth Dex",
	"Survival": "Survival Wis"
	}



def write_fillable_pdf(input_pdf_path, output_pdf_path, data_dict):
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    annotations = template_pdf.pages[0][ANNOT_KEY]
    for annotation in annotations:
        if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            if annotation[ANNOT_FIELD_KEY]:
                key = annotation[ANNOT_FIELD_KEY][1:-1]
                

                if key in data_dict.keys():
                    annotation.update(
                        pdfrw.PdfDict(T=data_dict[key])
                        )
                    

                    #annotation.update(
                    #    pdfrw.PdfDict(AS='{}'.format(data_dict[key]))
                    #    )

    pdfrw.PdfWriter().write(output_pdf_path, template_pdf)


def print_annotation_values(input_pdf_path, data_dict):
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    annotations = template_pdf.pages[0][ANNOT_KEY]

    for annotation in annotations:
        if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            if annotation[ANNOT_FIELD_KEY]:
                key = annotation[ANNOT_FIELD_KEY][1:-1]
                
                if "box" not in annotation["/T"]:
                  print(annotation["/T"])
                  print(annotation["/V"])
                  print(annotation["/AP"])
                  print("#"*30)

    for annotation in annotations:
        if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            if annotation[ANNOT_FIELD_KEY]:
                key = annotation[ANNOT_FIELD_KEY][1:-1]
                
                if "box" in annotation["/T"]:
                  print(annotation["/T"])
                  print(annotation["/V"])
                  print(annotation["/AP"])
                  print("#"*30)

write_fillable_pdf(INVOICE_TEMPLATE_PATH, INVOICE_OUTPUT_PATH, box_dict)
print_annotation_values(INVOICE_OUTPUT_PATH, box_dict)