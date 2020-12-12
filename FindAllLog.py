import re


def FindAllLog():
        allLog = list()
        currentId = notepad.getCurrentBufferID()
        lineCount = editor.getLineCount()
        
        for lineIndex in range(lineCount):
            lineContent = editor.getLine(lineIndex)
            
            match = re.search('\d\d-\d\d \d\d:\d\d:\d\d:\d\d\d', lineContent)
            if match:
                allLog.append(lineContent)

        notepad.new()
        notepad.menuCommand(MENUCOMMAND.VIEW_GOTO_ANOTHER_VIEW)
        for error in allLog:
            editor.addText(error)
            
            
        notepad.activateBufferID(currentId)
        
FindAllLog()