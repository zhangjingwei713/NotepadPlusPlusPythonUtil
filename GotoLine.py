def GotoLine():
    currentView = notepad.getCurrentView()
    currentLine = editor.getCurLine()
    
    if currentView == 1:
        otherView = 0
    else:
        otherView = 1
    
    index = notepad.getCurrentDocIndex(otherView)
    notepad.activateIndex(otherView, index)
    
    lineCount = editor.getLineCount()
        
    for lineIndex in range(lineCount):
        lineContent = editor.getLine(lineIndex)
            
        if currentLine == lineContent:                
            editor.gotoLine(lineIndex)
            
            desLineIndex = 0
            if lineIndex >= 15:
                desLineIndex = lineIndex - 15
                
            editor.setFirstVisibleLine(desLineIndex)
            break
        
    
GotoLine()