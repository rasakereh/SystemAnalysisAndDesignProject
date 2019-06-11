from django.conf import settings
import zipfile

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

def chopToMicrotasks(filePath):
    return True
