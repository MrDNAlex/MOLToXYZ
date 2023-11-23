from random import random
import tkinter as tk
import os
from tkinter import filedialog

def GetBanner () -> str:
    #Get Banner Path
    script_dir = os.path.dirname(__file__).removesuffix("Python")
    rel_path = "Decorations\\Banner.txt"
    bannerPath = os.path.join(script_dir, rel_path)
   
    with open(bannerPath, "r") as file:
        bannerContent = file.read()

    return bannerContent

def GetHeader () -> str:
    #Get Header Path
    script_dir = os.path.dirname(__file__).removesuffix("Python") #<-- absolute dir the script is in
    rel_path = "Decorations\\Signature.txt"
    headerPath = os.path.join(script_dir, rel_path)

    with open(headerPath, "r") as file:
        headerContent = file.read()

    return headerContent


def GetFileOutputHeader () -> str:
    #Get Header Path
    script_dir = os.path.dirname(__file__).removesuffix("Python") #<-- absolute dir the script is in
    rel_path = "Decorations\\FileOutput.txt"
    fileOutputPath = os.path.join(script_dir, rel_path)

    with open(fileOutputPath, "r") as file:
        fileOutputContent = file.read()

    return fileOutputContent

def PrintHeaderAndBanner () -> str:
    #Prints header and banner in Console / Command Prompt / Terminal
    print(GetBanner())

    print(GetHeader())

def GetFileContent () -> str:
    #Asks a windows file explorer tab to open
    print("\n \n \n Select a .MOL File to Convert:")

    file_path = filedialog.askopenfilename()

    with open(file_path, "r") as file:
        file_content = file.read()

    return file_content

def GetNumOfAtoms (molFile: [str]) -> int:
    config = molFile[3].lstrip()
    return int(config.split(' ')[0])

def GetXYZHeader (atomNum: int, molName: str) -> str:
    header = str(atomNum) + "\n"
    header += molName + "\n"
    return header

def GetMOLArray (line: str) -> [str]:
    #Strip the first spaces
    newLine = line.lstrip()

    #Split into array
    array = newLine.split(' ')

    #Remove all ('') from array
    while (array.__contains__('')):
        array.remove('')

    return array

def FormatFromMOLToXYZ (molArray: [str]) -> [str]:
    #Temporary list of Info (X, Y, Z, Name)
    info = [1,2,3,4]
    info[0] = molArray[0]
    info[1] = molArray[1]
    info[2] = molArray[2]
    info[3] = molArray[3]

    #Format to --> (Name, x, y, z)
    return [info[3], info[0],info[1], info[2]]

def ConvertToXYZLine (formatArray: [str]) -> str:
    XYZ_Line = ''

    #Loop and add the 
    for i in formatArray:
        XYZ_Line += i + " "

    return XYZ_Line

def CreateXYZFile () -> str:
    #Ask for Molecule name
    root.withdraw()
    moleculeName = input("\n \nInput Molecule Name:")

    #Get File Header
    XYZ = GetXYZHeader(NumOfAtoms, moleculeName)

    for i in range(4, 4 + NumOfAtoms):
        #Get array
        MOLArray = GetMOLArray(splitMOLFile[i])

        #Format to XYZ Format
        FormattedInfo = FormatFromMOLToXYZ(MOLArray)

        XYZAtom = ConvertToXYZLine(FormattedInfo)

        XYZ += XYZAtom + "\n"
    
    return XYZ

def SaveFileToDrive (writeFile: str):
    root.wm_attributes('-topmost', 1)

    print("\n \nName and save the XYZ File to your preffered Location:")

    output_path = filedialog.asksaveasfilename(defaultextension=".xyz", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

    with open(output_path, 'w') as file:
        # Write the data to the file
        file.write(writeFile)
    
#Surround By try except to prevent error logs from showing
try:
    #Sets up the folder
    root = tk.Tk()
    root.withdraw()

    #Prints Header and Banner
    PrintHeaderAndBanner()

    MOL_File = GetFileContent()

    #Splits the content line by line
    splitMOLFile = MOL_File.split('\n')

    #Gets the number of Atoms
    NumOfAtoms = GetNumOfAtoms(splitMOLFile)

    #Start the XYZ File
    XYZ_File = CreateXYZFile()

    #Save File to Device
    SaveFileToDrive(XYZ_File)

     #Export File Output Header
    print("\n \n " + GetFileOutputHeader() + "\n \n" + XYZ_File)

except:
    print("\n\nAn Error Has Occured\n\n")