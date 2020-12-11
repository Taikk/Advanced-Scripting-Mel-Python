import maya.cmds as cmds


class FreezeTransform:

    def freeze(self):
        selection = cmds.ls(s=True)

        for x in selection:
            cmds.makeIdentity(a=True, t=0, r=0, s=0, n=0)