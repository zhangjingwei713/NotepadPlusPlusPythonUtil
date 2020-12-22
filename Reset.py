def Reset():
    currentView = notepad.getCurrentView()
    if currentView == 1:
        notepad.menuCommand(MENUCOMMAND.VIEW_GOTO_ANOTHER_VIEW)
        
    currentId = notepad.getCurrentBufferID()
    currentFilename = notepad.getCurrentFilename()
    allFiles = notepad.getFiles()
    
    for file in allFiles:
        filename = file[0]
        fileId = file[1]
        
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
    editor.addText('\n')
    editor.addText('$Content$\n')
    editor.addText('[ClientManager] Connected loginToken:\n')
    editor.addText('[ClientManager] client disconnected, loginToken:\n')
    editor.addText('GameLiftClientAgent.ConnectRoomWithPlayerSession: Connect to\n')
    editor.addText('[ServerManager] client connected, loginToken:\n')
    editor.addText('[ServerManager] client disconnected, loginToken:\n')
    editor.addText('[GameStateManager]\n')
    editor.addText('ActiveSceneChanged, oriScene:\n')
    editor.addText('$RegexContent$\n')
    editor.addText('\[Error\]|\[Exception\]\n')
    editor.addText('$StartFrame$\n')
    editor.addText('$EndFrame$\n')
    editor.addText('$End$\n')
    
    notepad.activateBufferID(currentId)
    
    
Reset()