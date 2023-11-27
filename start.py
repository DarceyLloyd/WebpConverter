import os
import pathlib
import glob
import subprocess
import sys
import threading
from subprocess import Popen
import time

# Resource
# https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
# https://stackoverflow.com/questions/15928956/how-to-run-an-exe-file-with-the-arguments-using-python
# https://blog.floydhub.com/multiprocessing-vs-threading-in-python-what-every-data-scientist-needs-to-know/


# Set this to the webp quality you want 70 to 80 is recommended
webpQuality = 70


def cls():
    # clear = "\n" * 100
    # print(clear)
    os.system('cls' if os.name=='nt' else 'clear')

cls()

path = str(pathlib.Path().resolve())
# print("path = ",path)

exe = path + "\\cwebp.exe"
# print("exe = " + exe)

sourcePath = path + "\\input\\"
sourcePath = str(pathlib.Path(sourcePath).resolve())
# print("sourcePath = ",sourcePath)

outputPath = path + "\\output\\"
outputPath = str(pathlib.Path(outputPath).resolve())
# print("outputPath = ",outputPath)

globString = str(sourcePath) + "\\*.png"
files = glob.glob(globString)
noOfFiles = len(files)-1
# print(noOfFiles)

# print("file at index 0 = ",files[0])

# sys.exit()


print("NODEJS: Will do a quicker job on 5000 to 8000 files.")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("PYTHON: Will do a quicker job on larger.")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("Depending on your machine.")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - -")
time.sleep(10)



def convert(quality,source,target):
    sourceFilePath, sourceFileName = os.path.split(source)
    outputFileName = sourceFileName.replace(".png",".webp")
    outputFilePath = outputPath+"\\"+ outputFileName

    # print(outputFilePath)
    # command = [
    #     "cwebp",
    #     ("-q " + str(quality) + " " + source + " -o " + outputFilePath)
    # ]

    command2 = "cwebp.exe -q " + str(quality) + " " + source + " -o " + outputFilePath
    # print(command2)

    # subprocess.run(["RegressionSystem.exe", "-config filename"])
    # subprocess.call(command2)
    FNULL = open(os.devnull, 'w')
    # subprocess.call(command2, stdout=FNULL, stderr=FNULL, shell=False)
    subprocess.run(command2, stdout=FNULL, stderr=FNULL, shell=False)




# noOfFiles = 3
noOfFilesAtATime = 50

for i in range (0,noOfFiles):
    f = files[i]
    # f.append(files[n])
    convert(webpQuality,f,outputPath)
    print("Converting file " + str((i+1)) + " of " + str(noOfFiles))



# for i in range (0,noOfFiles,noOfFilesAtATime):
#     # os.path.

#     f = []
#     for n in range (i,(i+noOfFilesAtATime)):
#         f = files[n]
#         # f.append(files[n])
#         convert(70,f,outputPath)
#         print(str(n) + " of " + str(noOfFiles))





# MULTI THREADING Work in progress scratchings


# noOfFiles = 1
# noOfFilesAtATime = 1

# def w1():
#     os.system(exe)

# def w2():
#     os.system(exe)

# def w3():
#     os.system(exe)

# def w4():
#     os.system(exe)

# def w5():
#     os.system(exe)


# for i in range (0,noOfFilesAtATime):
#     os.system(exe)


# for i in range (0,noOfFiles,noOfFilesAtATime):
#     # os.path.

#     f = []
#     for n in range (i,(i+noOfFilesAtATime)):
#         source = files[n]
#         sourceFilePath, sourceFileName = os.path.split(source)
#         outputFileName = sourceFileName.replace(".png",".webp")
#         outputFilePath = outputPath+"\\"+ outputFileName


#         a = [
#             " -q ",
#             " 70 ",
#             " ",
#             source,
#             " -o ",
#             outputFilePath
#         ]

#         t1 = threading.Thread(target=exe, args=(a))
#         t1.start()
#         t1.join()
