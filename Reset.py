def Reset():
    currentId = notepad.getCurrentBufferID()
    currentFilename = notepad.getCurrentFilename()
    print(currentId)
    allFiles = notepad.getFiles()
    
    for file in allFiles:
        filename = file[0]
        fileId = file[1]
        print(filename)
        print(fileId)
        
        notepad.activateBufferID(fileId)
        
        if ':\\' in filename:
            if fileId != currentId:
                editor.emptyUndoBuffer()
        else:
            editor.clearAll()
            
    
    notepad.activateBufferID(currentId)
    notepad.closeAllButCurrent()
    
    notepad.open('D:\QuickSearch.txt')
    notepad.menuCommand(MENUCOMMAND.VIEW_CLONE_TO_ANOTHER_VIEW)
    
    notepad.open('D:\QuickSearchClass.txt')
    notepad.menuCommand(MENUCOMMAND.VIEW_CLONE_TO_ANOTHER_VIEW)
    
    notepad.new()
    notepad.menuCommand(MENUCOMMAND.VIEW_GOTO_ANOTHER_VIEW)
    editor.addText(currentFilename)
    
    notepad.activateBufferID(currentId)
    
    
Reset()