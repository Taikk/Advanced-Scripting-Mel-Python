import maya.cmds as mc

mc.polySphere(name='mySphere_geo',
              subdivisionsHeight=20,
              subdivisionsAxis=32)
mc.polySphere(name='middleSphere_geo',
              subdivisionsHeight=20,
              subdivisionsAxis=32)
mc.move(0,1,0,
        'middleSphere_geo',
        absolute=True)
mc.scale(.75, .75, .75,
         'middleSphere_geo',
         absolute=True)
mc.polySphere(name='topSphere_geo',
              subdivisionsHeight=20,
              subdivisionsAxis=32)
mc.move(0,1.80,0,
        'topSphere_geo',
        absolute=True)
mc.scale(.6, .6, .6,
         'topSphere_geo',
         absolute=True)

#Arms of the Model

mc.polyCylinder(name='rightArm_geo',
                sh=1,
                sa=1)
mc.move(1,.9,0,
        'rightArm_geo',
        absolute=True)
mc.scale(.1, 1, .1,
         'rightArm_geo',
         absolute=True)
mc.select('rightArm_geo')
mc.rotate(0, 0, '45deg', r=True)

mc.polyCylinder(name='leftArm_geo',
                sh=1,
                sa=1)
mc.move(-1,.9,0,
        'leftArm_geo',
        absolute=True)
mc.scale(.1, 1, .1,
         'leftArm_geo',
         absolute=True)
mc.select('leftArm_geo')
mc.rotate(0, 0, '-45deg', r=True)

mc.polyCylinder(name='lowerHat_geo',
                sh=1,
                sa=1)
mc.scale(.75, .05, .75,
         'lowerHat_geo',
         a=True)
mc.move(0, 2.10, 0,
        'lowerHat_geo',
        a=True)
mc.polyCylinder(name='upperHat_geo',
                sh=1,
                sa=1)
mc.scale(.5, 1, .5,
         'upperHat_geo',
         a=True)
mc.move(0, 2.25, 0,
        'upperHat_geo',
        a=True)
mc.polyCube(n='rightEye_geo',
            d=.12,
            w=.12,
            h=.12,)
mc.move(.4, 1.9, .5,
        'rightEye_geo',
        a=True)
mc.polyCube(n='leftEye_geo',
            d=.12,
            w=.12,
            h=.12,)
mc.move(-.4, 1.9, .5,
        'leftEye_geo',
        a=True)
mc.polyCube(n='mouth_geo',
            d=.1,
            w=.2,
            h=.1,)
mc.move(0, 1.7, .6,
        'mouth_geo',
        a=True)

# Tie

mc.polyCube(n='tie_geo',
            d=.1,
            w=.1,
            h=.1,)
mc.move(0, 1.5, .6,
        'tie_geo',
        a=True)
mc.polyCube(n='tieLength_geo',
            d=.1,
            w=.1,
            h=.8,)
mc.move(0, 1.1, .75,
        'tieLength_geo',
        a=True)
mc.rotate('-20deg', 0, 0, r=True)