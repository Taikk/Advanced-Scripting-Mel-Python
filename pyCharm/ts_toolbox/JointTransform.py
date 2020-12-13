import maya.cmds as cmds


class JointTransform:
    def __init__(self):
        self.my_window = 'tsJointWindow'

    def delete(self):
        if cmds.window(self.my_window, exists=True):
            cmds.deleteUI(self.my_window)

    def create(self):
        self.delete()

        self.my_window = cmds.window(self.my_window,
                                     title='Joint Transform Display',
                                     widthHeight=(200, 200))
        self.col_layout = cmds.columnLayout(parent=self.my_window,
                                            adjustableColumn=True)
        cmds.button(parent=self.col_layout,
                    label='JointDisplay',
                    c=lambda *x: self.AxisDisplay())
        cmds.showWindow(self.my_window)

    def AxisDisplay(self):
        return



my_window = JointTransform()
my_window.create()
