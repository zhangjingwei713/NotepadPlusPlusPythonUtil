import re


def SimplifyStack():
    contentAfterSimplifyStack = list()
    
    (start, end) = editor.getUserLineSelection();
    lineCount = editor.getLineCount()
    if start == 0 and end == lineCount - 1:
        return;
    
    for lineIndex in range(start, end + 1):
        changed = False
        lineContent = editor.getLine(lineIndex)
        if len(lineContent) > 0:
            atStartPos = lineContent.find('(at ')
            if atStartPos > 0:
                newLine = lineContent[:atStartPos]
                
                stackStr = re.findall('\(at (.+?)$', lineContent)
                if len(stackStr) > 0:
                    lastPos = stackStr[0].rfind('/')
                    if lastPos >= 0:
                        afterStr = stackStr[0][lastPos + 1:]
                        newLine += '(' + afterStr
                        changed = True
                        editor.replaceLine(lineIndex, newLine)

        # if changed:
        #     contentAfterSimplifyStack.append(newLine)       
        # else:
        #     contentAfterSimplifyStack.append(lineContent)
 

    # editor.clearAll()
    # 
    # for newLine in contentAfterSimplifyStack:
    #     editor.addText(newLine)
        

SimplifyStack()