from django.conf import settings
import os
import ntpath
import zipfile

def generateOutpath(zipPath):
    return zipPath

def validateUpload(filePath):
    filePath = settings.MEDIA_ROOT + "/" + filePath.split(settings.MEDIA_URL)[1]
    zip_ref = zipfile.ZipFile(filePath, 'r')
    zip_ref.extractall(generateOutpath())
    zip_ref.close()

    return True

def getUploadPath(docObject):
    return docObject.doc_file.path

def getUnzippedPath(zipPath):
    # TODO: duplicate file names :|
    unzippedPath = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/datasets/" + ntpath.basename(zipPath)[:-4]
    zip_ref = zipfile.ZipFile(zipPath, 'r')
    zip_ref.extractall(unzippedPath)
    zip_ref.close()

    return unzippedPath

def chopToMicrotasks(filePath):
    
    return True
