import nuke
import nukescripts
import checkenv
import openNode
import openfile
import helloWidget
import makewrite
import makewrite3

tb = nuke.toolbar("Nodes")
m = tb.addMenu("namgwang", icon="nam_logo.png")
m.addMenu("Draw")
m.addCommand("Draw/Timecode_burnin", "nuke.createNode('timecode_burnin2')")
m.addMenu("Slate")
m.addCommand("Slate/slate", "nuke.createNode('slate')")

mb = menubar.addMenu("Nam")
mb.addCommand("Issue_and_Bugs", "nukescripts.start('https://github.com/lazypic/nuke/issues')")
mb.addCommand("-", "", "")
mb.addCommand("StartPerformanceTimers", "nuke.startPerformanceTimers()")
mb.addCommand("StopPerformanceTimers", "nuke.stopPerformanceTimers()")
mb.addCommand("Checkenv", "checkenv.main()")
mb.addCommand("OpenNode", "openNode.main()")
mb.addCommand("OpenFile", "reload(openfile);openfile.main()", "F8", shortcutContext=2)
mb.addCommand("HelloWorld", "helloWidget.main()")
mb.addCommand("makeWriteNode", "reload(makewrite);makewrite3.main()", "F10", shortcutContext=2)
