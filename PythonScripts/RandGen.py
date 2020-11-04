import maya.cmds as cmds
import random


def main(amnt, minX, maxX, minY, maxY, minZ, maxZ):
    list = []
    for x in range(0, amnt):
        items = cmds.duplicate(cmds.ls(selection=True))
        list.extend(items)
        for z in items:
            cmds.move(random.uniform(minX, maxX), random.uniform(minY, maxY),
                  random.uniform(minZ, maxZ))


print main(3, 0, 3, 0, 3, 0, 3)