from django.conf import settings
import zipfile
import csv, os
from pprint import pprint

def generateOutpath(zipPath):
    return zipPath

def validateUpload(filePath):
    filePath = settings.MEDIA_ROOT + "/" + filePath.split(settings.MEDIA_URL)[1]
    zip_ref = zipfile.ZipFile(filePath, 'r')
    zip_ref.extractall(generateOutpath)
    zip_ref.close()

    return True

def saveFile(filePath):
    return filePath

def chopToMicrotasks(filePath, contentModel, saverModel, category):
    
    with open(filePath, newline='') as csvfile:
        questionList = list(csv.reader(csvfile, delimiter=','))
        for question in questionList:
            qText, isForAll, filename, choices, qid = question
            qText, isForAll, filename, choices, qid = qText.strip(), isForAll.strip() == "true", filename.strip(), choices.strip(), int(qid.strip())
            if isForAll:
                pass
            else:
                queryContentPath = os.path.join(os.path.dirname(filePath), category + "/" + filename)
                content = contentModel.objects.filter(contentPath = queryContentPath).latest('id')
                newTask = saverModel(content=content, category=category)
                newTask.question = qText
                newTask.answerChoices = None if choices == "NA" else choices
                newTask.qid = qid
                newTask.save()
    return questionList
