import io
import re


def FindSpecificLine():
    allPreContent = list()

    allContent = list()
    allRegexContent = list()
    startFrame = 0
    endFrame = -1

    filename = editor.getLine(0)
    filename = filename.replace('\\', '/')
    filename = filename.strip()

    currentState = 0

    lineCount = editor.getLineCount()
    for lineIndex in range(lineCount):
        lineContent = editor.getLine(lineIndex)
        allPreContent.append(lineContent)

        if '$End$' in lineContent:
            break

    for lineIndex in range(lineCount):
        lineContent = editor.getLine(lineIndex)
        lineContent = lineContent.strip()

        if '$Content$' in lineContent:
            currentState = 1
            continue
        elif '$RegexContent$' in lineContent:
            currentState = 2
            continue
        elif '$StartFrame$' in lineContent:
            currentState = 3
            continue
        elif '$EndFrame$' in lineContent:
            currentState = 4
            continue
        elif '$End$' in lineContent:
            break

        if currentState == 1:
            allContent.append(lineContent)
        elif currentState == 2:
            allRegexContent.append(lineContent)
        elif currentState == 3:
            startFrame = int(lineContent)
        elif currentState == 4:
            endFrame = int(lineContent)

    validContent = list()
    f = io.open(filename, encoding='utf-8')
    for x in f:
        if len(x) <= 0:
            continue

        frameStr = re.findall('\d\d-\d\d \d\d:\d\d:\d\d:\d\d\d \[\w*\] \[(.+?)\]', x)
        if len(frameStr) <= 0:
            continue

        frameInt = int(frameStr[0])

        if frameInt < startFrame:
            continue

        if endFrame != -1 and frameInt > endFrame:
            break

        valid = False
        for content in allContent:
            if content in x:
                valid = True
                break

        if not valid:
            for content in allRegexContent:
                match = re.search(content, x)
                if match:
                    valid = True

        if valid:
            validContent.append(x)

    editor.clearAll()

    for content in allPreContent:
        editor.addText(content)

    editor.addText('\n')

    for validLine in validContent:
        editor.addText(validLine)


FindSpecificLine()
