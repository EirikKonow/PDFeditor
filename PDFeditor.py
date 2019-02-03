#! /usr/bin/python

import os
import pdfrw
import math
from pprint import pprint
from classSpells import classSpells
from classSpells import calc_xp2lvl


INVOICE_TEMPLATE_PATH = 'inPDF_fixed.pdf'
INVOICE_OUTPUT_PATH = 'outPDF.pdf'


ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'

# annotation.update(pdfrw.PdfDict(AS='/Yes')) #, /Off
def print_annotation_values(input_pdf_path, output_pdf_path, data_dict):
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    annotations = template_pdf.pages[0][ANNOT_KEY]

    for annotation in annotations:
        if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            if annotation[ANNOT_FIELD_KEY]:
                key = annotation[ANNOT_FIELD_KEY][1:-1]
                
                if "Box" not in annotation["/T"]:
                  print(annotation["/T"])
                  print(annotation["/V"])
                  print(annotation["/AP"])
                  print("#"*30)

    for annotation in annotations:
        if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            if annotation[ANNOT_FIELD_KEY]:
                key = annotation[ANNOT_FIELD_KEY][1:-1]
                
                if "Box" in annotation["/T"]:
                  print(annotation["/T"])
                  print(annotation["/V"])
                  print(annotation["/AP"])
                  print("#"*30)

"""
                if key in data_dict.keys():
                    annotation.update(
                        pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                        )
                    if "Box" in annotation["/T"]: # If not check box
                      print(annotation["/T"])
                      annotation.update(pdfrw.PdfDict(AP=''))
 
                    if "Box" in annotation["/T"]:
                      print(annotation["/T"])
                      print(annotation["/V"])
                      print(annotation["/AP"])
"""

def write_fillable_pdf(input_pdf_path, output_pdf_path, data_dict):
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    annotations = template_pdf.pages[0][ANNOT_KEY]
    for annotation in annotations:
        if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            if annotation[ANNOT_FIELD_KEY]:
                key = annotation[ANNOT_FIELD_KEY][1:-1]
                

                if key in data_dict.keys():
                    annotation.update(
                        pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                        )
                    if "box" not in annotation["/T"]: # If not check box
                      annotation.update(pdfrw.PdfDict(AP=''))
                    
                    
                    if "/Yes" in annotation["/V"]:
                      #print(annotation["/T"])
                      #print(annotation["/V"])
                      #print(annotation["/AP"])
                      #annotation.update(
                      #  pdfrw.PdfDict(T='{}'.format("TA_WIS_box"))
                      #  )
                    
                      annotation.update(
                        pdfrw.PdfDict(AS='{}'.format(data_dict[key]))
                        )

    pdfrw.PdfWriter().write(output_pdf_path, template_pdf)



STR = 10
DEX = 16
CON = 10
INT = 11
WIS = 11
CHA = 14
charRace = "Dwarf(Hill)"
exp = 900


def calcStatmod(stat):
  mod = math.floor((stat-10) / 2)
  return str(mod)

data_dict = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA',]
data_dict = {key: eval(key) for key in data_dict}

def add_race_modifiers(keys, charRace):
  # Strength
  if charRace in ("Dwarf(Mountain)", "Half-orc", "Dragonborn"):
    keys["STR"] += 2
  if charRace == "Human":
    keys["STR"] += 1

  # Dexterity
  if charRace in ("Elf(High)", "Elf(Wood)", "Elf(Dark)", "Halfling(Stout)", "Halfling(Lightfoot)"):
    keys["DEX"] += 2
  if charRace in ("Gnome(Forest)", "Human"):
    keys["DEX"] += 1

  # Constitution
  if charRace in ("Dwarf(Mountain)", "Dwarf(Hill)"):
    keys["CON"] += 2
  if charRace in ("Elf(High)", "Halfling(Stout)", "Gnome(Rock)", "Half-orc", "Human"):
    keys["CON"] += 1

  # Intelligence
  if charRace in ("Gnome(Forest)", "Gnome(Rock)"):
    keys["INT"] += 2
  if charRace in ("Tiefling", "Human", "Elf(High)"):
    keys["INT"] += 1

  # Wisdom
  if charRace in ("Dwarf(Hill)", "Elf(Wood)", "Human"):
    keys["WIS"] += 1

  # Charisma

  if charRace in("Half-elf", "Tiefling"):
    keys["CHA"] += 2
  if charRace in ("Elf(Dark)", "Halfling(Lightfoot)", "Dragonborn", "Human"):
    keys["CHA"] += 1

  return data_dict

data_dict = add_race_modifiers(data_dict, charRace)

add_keys = []
for val in data_dict:
  add_keys.append(val+"mod")
for val in add_keys:
  data_dict[val] = None

for key in data_dict:
  if "mod" in key:
    data_dict[key] = calcStatmod(eval(str(data_dict[key[0:3]])))


def add_ProfBonus(data_dict, exp):
	bonus = 2
	bonus = 2 + math.floor(((calc_xp2lvl(exp)+3)/4)-1)
	data_dict["ProfBonus"] = bonus
	return data_dict

def add_CheckBoxDict(charClass, charBackground, data_dict):
  box_keys = [
  "DS success 1",
  "DS success 2",
  "DS success 3",
  "DS failure 1",
  "DS failure 2",
  "DS failure 3",
  "ST STR box",
  "ST DEX box",
  "ST CON box",
  "ST INT box",
  "ST WIS box",
  "ST CHA box",
  "Acrobatics box",
  "Animal Handling box",
  "Arcana box",
  "Athletics box",
  "Deception box",
  "History box",
  "Insight box",
  "Intimidation box",
  "Investigation box",
  "Medicine box",
  "Nature box",
  "Perception box",
  "Performance box",
  "Persuasion box",
  "Religion box",
  "Sleight of Hand box",
  "Stealth box",
  "Survival box"
  ]

  for key in box_keys:
    data_dict[key] = None

  if charClass == "Rogue":
    data_dict["ST DEX box"] = "/Yes"
    data_dict["ST INT box"] = "/Yes"

  if charBackground == "Folk Hero":
    data_dict["Stealth box"] = "/Yes"
    data_dict["Check Box 40"] = "/Yes"

  return data_dict

def add_STvalues(data_dict):
  ST_keys = [
  "ST Strength",
  "ST Dexterity",
  "ST Constitution",
  "ST Intelligence",
  "ST Wisdom",
  "ST Charisma"
  ]

  for ST_key in ST_keys:
    if data_dict["ST "+ST_key[3:6].upper()+" box"] == "/Yes":
      data_dict[ST_key] = int(data_dict[ST_key[3:6].upper()+"mod"]) + int(data_dict["ProfBonus"])
    else:
      data_dict[ST_key] = data_dict[ST_key[3:6].upper()+"mod"]
  return data_dict

def add_skills(data_dict):
  skill_keys = [
    "Acrobatics Dex",
    "Animal Handling Wis",
    "Arcana Int",
    "Athletics Str",
    "Deception Cha",
    "History Int",
    "Insight Wis",
    "Intimidation Cha",
    "Investigation Int",
    "Medicine Wis",
    "Nature Int",
    "Perception Wis",
    "Performance Cha",
    "Persuasion Cha",
    "Religion Int",
    "Sleight of Hand Dex",
    "Stealth Dex",
    "Survival Wis"
  ]

  for key in skill_keys:
    if data_dict[key[0:-4]+" box"] == "/Yes":
      try:
        data_dict[key] = int(data_dict[key[-3:len(key)].upper()+"mod"]) + int(data_dict["ProfBonus"])
      except:
        pass
    else:
      try:
        data_dict[key] = int(data_dict[key[-3:len(key)].upper()+"mod"])
      except:
        pass
  return data_dict

 # dictionary for different classes


def calcRogue(stats, exp):
  charClass = "Rogue"

  charBackground = "Folk Hero"

  charRace = "Dwarf(Hill)"

  data_dict = add_ProfBonus(stats, exp)

  data_dict = add_CheckBoxDict(charClass, charBackground, data_dict)

  data_dict = add_STvalues(data_dict)

  data_dict = add_skills(data_dict)

  data_dict = classSpells(exp, charClass, data_dict)

  data_dict["ClassLevel"] = "{}, {}".format(charClass, calc_xp2lvl(exp))

  data_dict["XP"] = exp

  data_dict["Race"] = charRace

  return data_dict



if __name__ == '__main__':
  data_dict = calcRogue(data_dict, exp)
  print(data_dict)
  write_fillable_pdf(INVOICE_TEMPLATE_PATH, INVOICE_OUTPUT_PATH, data_dict)