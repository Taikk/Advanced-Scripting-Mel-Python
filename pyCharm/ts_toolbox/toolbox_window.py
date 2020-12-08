import maya.cmds as cmds


class Window:
    def __init__(self):
        self.my_window = 'tsCoolToolWindow'

    def delete(self):
        if cmds.window(self.my_window, exists=True):
            cmds.deleteUI(self.my_window)

    def create(self):
        self.delete()

        self.my_window = cmds.window(self.my_window,
                                     title='ToolBox Manager',
                                     widthHeight=(200, 200))
        self.col_layout = cmds.columnLayout(parent=self.my_window,
                                            adjustableColumn=True)
        self.size_slider = cmds.intSliderGrp(parent=self.col_layout,
                                             minValue=0,
                                             maxValue=25)

        cmds.button(parent=self.col_layout,
                    label='Random Generator',
                    c=lambda *x: self.ranGenFunc())
        cmds.button(parent=self.col_layout,
                    label='Rename Function',
                    c=lambda *x: self.renameFunc())

    def ranGenFunc(self):
        import RandGen
        reload(RandGen)

    def renameFunc(self):
        import Renamer
        reload(Renamer)
