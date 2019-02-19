#coding:utf8
import nuke
nuke.pluginAddPath("./gizmos", addToSysPath=True)
nuke.pluginAddPath("./images", addToSysPath=True)
nuke.pluginAddPath("./scripts", addToSysPath=True)
nuke.pluginAddPath("./lib", addToSysPath=True)

#nukePath=os.environ

#Format
nuke.addFormat("24 24 nukeIcon")
nuke.addFormat("360 360 kakaoEmoticon")
