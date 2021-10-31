from turtle import Screen, numinput, Turtle
from entities.CraftedItem import CraftedItem
from entities.RawItem import RawItem
	

def handle(screen: Screen,  pen, type: str,):
	pen.clear()
	craftedItem = CraftedItem(type.casefold(), askCount())
	output = ""
	output += craftedItem.type 
	output += "\t" + str(craftedItem.count) + ": \n"
	output += "-----\n"

	for part in craftedItem.parts:
		output += getItemInfo(part,False, 0)

	pen.write(output,align="center", font=("Courier", 24, "normal"))


def getItemInfo(item, child, level):
	output = ""
	if isinstance(item,RawItem):
		if child:
			for i in range(level):
				output += "\t"
		output += "{} -- {}".format( item.type, item.count)
		output += "\n"
	elif isinstance(item,CraftedItem):
		if child:
			for i in range(level):
				output += "\t"
		output += "{} -- {}".format( item.type, item.count)
		output += "\n"
		for part in item.parts:
			output += getItemInfo(part,True,level+1)


	return output

def askCount():
	return int(numinput(title="CraftingChoiceCount",prompt="Wie viel brauchst du ? ",minval=0,maxval=10000))


