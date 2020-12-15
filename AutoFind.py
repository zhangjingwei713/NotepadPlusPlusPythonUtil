def AutoFind():
    editor.wordLeft()
    leftPos = editor.getCurrentPos()
    editor.wordRightExtend()
    rightPos = editor.getCurrentPos();
    
    print(leftPos)
    print(rightPos)
    copy = editor.copyRange(leftPos - 1, rightPos + 1)
    currentView = notepad.getCurrentView()
    otherView = 0
    if currentView == 0:
        otherView = 1
        
    index = notepad.getCurrentDocIndex(otherView)
    notepad.activateIndex(otherView, index)
    
    notepad.menuCommand(MENUCOMMAND.SEARCH_FIND)
    
    
AutoFind()