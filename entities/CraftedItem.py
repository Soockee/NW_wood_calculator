from entities.Item import Item
from entities.RawItem import RawItem


class CraftedItem(Item):
    def __init__(self, type: str, count: int):
        Item.__init__(self, type, count)
        self.parts = self.calculateParts()

    def calculateParts(self):
        parts = []
        if(self.type.casefold() == "lumber"):
                parts.append(CraftedItem("timber", 2 * self.count))
                parts.append(RawItem("agedwood", 4 * self.count))

        elif(self.type.casefold() == "timber"):
                parts.append(RawItem("greenwood", 4 * self.count))

        elif(self.type.casefold() == "wyrdwoodplanks"):
                parts.append(CraftedItem("lumber", 2 * self.count))
                parts.append(RawItem("wyrdwood", 6 * self.count))

        elif(self.type.casefold() == "ironwoodplanks"):
                parts.append(CraftedItem("wyrdwoodplanks", 2 * self.count))
                parts.append(RawItem("ironwood", 8 * self.count))
        else:
            return 1
        return parts
