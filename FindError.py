import re


def FindError():
        allError = list()
        currentId = notepad.getCurrentBufferID()
        lineCount = editor.getLineCount()
        
        for lineIndex in range(lineCount):
            lineContent = editor.getLine(lineIndex)
            
            if '[Error]' in lineContent or '[Exception]' in lineContent:
                allError.append(lineContent)

        notepad.new()
        notepad.menuCommand(MENUCOMMAND.VIEW_GOTO_ANOTHER_VIEW)
        for error in allError:
            editor.addText(error)
            
        
        notepad.activateBufferID(currentId)
    
FindError()