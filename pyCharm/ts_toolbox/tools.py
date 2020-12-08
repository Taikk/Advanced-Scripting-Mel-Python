import maya.cmds as cmds


def rename_geo(new_name):
    sels = cmds.sel(sl=True)

    for sel in sels:
        cmds.rename(sel, '%s_Geo' % new_name)