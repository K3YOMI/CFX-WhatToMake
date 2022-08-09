import os
import json
import random
import time
import sys
from os.path import exists
Prefix = '[TAG-HERE]'

def CreatePath(resName):
    parent_dir = os.getcwd() + "/Resources"
    path = os.path.join(parent_dir, Prefix+resName)
    file_exists = exists(path)
    if not file_exists:
        os.mkdir(path)
        f = open(path+"/fxmanifest.lua", "w")
        ManiffestFile = "author '" + Prefix + "'\ngame 'common'\nfx_version 'adamant'\nserver_scripts {'Server/*.lua'}\nclient_scripts {'Client/*.lua'}\nshared_scripts {'Shared/*.lua'}\n"
        f.write(ManiffestFile)
        f.close()
        os.mkdir(path+"/Server")
        os.mkdir(path+"/Client")
        os.mkdir(path+"/Shared")
        f = open(path+"/Server/sv.lua", "w")
        f.write("-- This is the start of the server script.")
        f.close()
        f = open(path+"/Client/cl.lua", "w")
        f.write("-- This is the start of the client script.")
        f.close()
        f = open(path+"/Shared/sh.lua", "w")
        f.write("-- This is the start of the shared script.")
        f.close()

def RandomlyGetSomeThingFromAFile():
    try:
        os.system("clear || cls")
        readFile = open('_TempData.json', 'r')
        convertJson = json.load(readFile)
        ChooesenSourceName = random.choice(convertJson)
        os.system("clear || cls")
        print("=== Warning : Some things may not make sense ===\n")
        print("We have an idea for you to create...")
        print("Try making: "+Prefix+ ChooesenSourceName)
        print("Want to create a directory for it? [Y/n]")
        Choice = input()
        if Choice == "N" or Choice == "n" or Choice == "":
            RandomlyGetSomeThingFromAFile()
        else:
            CreatePath(ChooesenSourceName)
            RandomlyGetSomeThingFromAFile()
    except KeyboardInterrupt:
        print("\n\nThanks for using this program.\n")
        sys.exit()
RandomlyGetSomeThingFromAFile()
