# dictionary for different classes
import math

def classSpells(exp, charClass, data_dict, verbose=False):
	if verbose:
				text_sneak_attack="""Sneak Attack:
Once per turn, you can deal an extra {} damage to one creature you hit with an attack if you have advantage on the attack roll. The attack must use a finesse or a ranged weapon. You don't need advantage on the attack roll if another enemy of the target is within 5 feet of it, that enemy isn't incapacitated, and you don't have disadvantage on the attack roll.
""".format(calc_sneak_attack(exp))

	else:
		text_sneak_attack="Sneak Attack({})".format(calc_sneak_attack(exp))

	if charClass == "Rogue":
		data_dict["Features and Traits"] = text_sneak_attack


	return data_dict


def calc_sneak_attack(exp):
	damage = "{}d6".format(math.floor((calc_xp2lvl(exp)/2)-0.5)+1)
	return damage



"""
1st +2 1d6 Expertise, Sneak Attack,
Thieves’ Cant
2nd +2 1d6 Cunning Action
3rd +2 2d6 Roguish Archetype
4th +2 2d6 Ability Score Improvement
5th +3 3d6 Uncanny Dodge
6th +3 3d6 Expertise
7th +3 4d6 Evasion
8th +3 4d6 Ability Score Improvement
9th +4 5d6 Roguish Archetype feature
10th +4 5d6 Ability Score Improvement
11th +4 6d6 Reliable Talent
12th +4 6d6 Ability Score Improvement
13th +5 7d6 Roguish Archetype feature
14th +5 7d6 Blindsense
15th +5 8d6 Slippery Mind
16th +5 8d6 Ability Score Improvement
17th +6 9d6 Roguish Archetype feature
18th +6 9d6 Elusive
19th +6 10d6 Ability Score Improvement
20th +6 10d6 Stroke of Luck
"""
def debug_calc_xp2lvl():
	# I ran this, everything seems fine in conversion
	for i in range(0,755000):
		level_last = calc_xp2lvl(i)
		level_now = calc_xp2lvl(i+1)
		if level_last != level_now:
			print("exp: {}".format(i+1))
			print("level: {}".format(level_now))

def calc_xp2lvl(exp):
	level = 0
	if exp<300:
		level = 1
	elif exp<900:
		level = 2
	elif exp<2700:
		level = 3
	elif exp<6500:
		level = 4
	elif exp<14000:
		level = 5
	elif exp<23000:
		level = 6
	elif exp<34000:
		level = 7
	elif exp<48000:
		level = 8
	elif exp<64000:
		level = 9
	elif exp<85000:
		level = 10
	elif exp<100000:
		level = 11
	elif exp<120000:
		level = 12
	elif exp<140000:
		level = 13
	elif exp<165000:
		level = 14
	elif exp<195000:
		level = 15
	elif exp<225000:
		level = 16
	elif exp<265000:
		level = 17
	elif exp<305000:
		level = 18
	elif exp<355000:
		level = 19
	else:
		level = 20
	return level

"""
0 1 +2
300 2 +2
900 3 +2
2,700 4 +2
6,500 5 +3
14,000 6 +3
23,000 7 +3
34,000 8 +3
48,000 9 +4
64,000 10 +4
85,000 11 +4
100,000 12 +4
120,000 13 +5
140,000 14 +5
165,000 15 +5
195,000 16 +5
225,000 17 +6
265,000 18 +6
305,000 19 +6
355,000 20 +6
"""