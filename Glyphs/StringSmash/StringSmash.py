#MenuTitle: StringSmash
# -*- coding: utf-8 -*-

__doc__ = '''
StringSmash is a simple RoboFont extension/Glyphs App script to generate strings
for spacing/kerning.
'''

# system
from vanilla import *
import os
import datetime 

# Glyphs
import GlyphsApp
import getpass

# presets
import StringSmashDicts
reload (StringSmashDicts)

class StringSmash(object):
    '''Returns string'''
    
    delimL = []
    listL = []
    listR = []
    delimR = []
    flip = False
    trio = False
    
    flipEnabled = True
    trioEnabled = True
    
    # diff
    if Glyphs.font:
        f = Glyphs.font
        font = []
        for i in f.glyphs:
        	font.append(i.name)
    else:
        font = []
    
    
    def __init__(self):
        '''A simple GUI'''
        self.w = FloatingWindow((-360, 40, 340, 330), "StringSmash v.1.0", textured=False)
        
        # list selections
        presetList = sorted(StringSmashDicts.presetDict.keys())
        delimList = sorted(StringSmashDicts.delimDict.keys())
        
        popUpLists = [
            ['-'] + delimList, # delimL
            ['-'] + presetList, # listL
            ['-'] + presetList, # listR
            ['-'] + delimList, # delimR
        ]
        
        # pick preset buttons
        yPos = [20, 55, 90, 125]
        names = ['delimL', 'listL', 'listR', 'delimR']
        presets = [delimList, presetList, presetList, delimList]
        dictList = [StringSmashDicts.delimDict, StringSmashDicts.presetDict, StringSmashDicts.presetDict, StringSmashDicts.delimDict]
        changeThis = ['', '', '', '']
        x = 0    
        for i in names:
            popupButton = PopUpButton((70, yPos[x], 160, 20),
                popUpLists[x], sizeStyle='regular', callback=self.pickPreset)
            popupButton.var = i
            popupButton.pickFrom = presets[x]
            popupButton.dict = dictList[x]
            setattr(self.w, i, popupButton)
            
            # get selection buttons
            squareButton = SquareButton((240, yPos[x], -10, 20), 'Get selection', sizeStyle='regular',
                callback=self.getSelection)
            squareButton.var = i
            setattr(self.w, 'button_%s' %i, squareButton)
            
            # diff
            # decoration
            imgPath = os.path.dirname(os.path.abspath(__file__))
            imgPath = os.path.join(imgPath, 'icons/%s.png' %i)
            imageButton = ImageButton((5, yPos[x]-2, 60, 24), imagePath=imgPath, title=None, bordered=False)
            setattr(self.w, 'image_%s' %i, imageButton)
            x += 1
        
        
        # generate buttons
        names = ['Generate and Open', 'Generate and Copy', 'Save String', 'Save MM style']
        callbackNames = ['generateAndOpen', 'generateAndCopy', 'saveString', 'saveMmStyle']
        callbacks = [self.button_generateAndOpen, self.button_generateAndCopy,
            self.button_saveString, self.button_saveMmStyle]
        xPos = [10, 175, 10, 175]
        yPos = [225 , 225, 275, 275]
        width = 155
        height = 40
        x = 0
        for i in names:
            button = SquareButton((xPos[x], yPos[x], width, height), i, sizeStyle='regular',
                callback=callbacks[x] )
            setattr(self.w, 'button_%s' %callbackNames[x], button)
            x += 1
        
        
        # checkboxes
        xPos = [95, 260]
        yPos = 175
        titles = ['Flip', 'Trio']
        x = 0
        for i in titles:
            checkBox = CheckBox((xPos[x], yPos, -10, 20), titles[x], sizeStyle='regular', value=False,
                callback=self.swithFlipTrio)
            temp = [0, 0]
            temp[x] = 1
            checkBox.var = temp
            setattr(self.w, 'checkBox_%s' %i, checkBox)
            x += 1
        
        
        # diff
        # checkbox images
        xPos = [20, 190]
        yPos = 175
        names = ['flip', 'trio']
        x = 0
        user = getpass.getuser()
        for i in names:
            imgPath = os.path.dirname(os.path.abspath(__file__))
            imgPath = os.path.join(imgPath, 'icons/%s.png' %i)
            imageButton = ImageButton((xPos[x], yPos-2, 60, 24), imagePath=imgPath, title=None, bordered=False)
            setattr(self.w, 'image_%s' %i, imageButton)
            x += 1
        
        # horizontal dividers
        yPos = [160, 210]
        for i in yPos:
            horizontalLine = HorizontalLine((0, i, -0, 1))
            setattr(self.w, 'horizontalLine_%i' %i, horizontalLine)
        
        self.w.verticalLine = VerticalLine((170, 161, 1, 50))
        
        self.w.open()
    
    def swithFlipTrio(self, sender):
        if sender.var == [1, 0]:
            if self.flip == True:
                self.flip = False
            else:
                self.flip = True
            if self.trioEnabled == True:
                self.w.checkBox_Trio.enable(False)
                self.trioEnabled = False
            else:
                self.w.checkBox_Trio.enable(True)
                self.trioEnabled = True
        
        if sender.var == [0, 1]:
            if self.trio == True:
                self.trio = False
            else:
                self.trio = True
            if self.flipEnabled == True:
                self.w.checkBox_Flip.enable(False)
                self.flipEnabled = False
            else:
                self.w.checkBox_Flip.enable(True)
                self.flipEnabled = True
    
    
    def pickPreset(self, sender):
        '''...'''
        # get the list items
        if sender.get() > 0:
            i = sender.get() - 1
            dictKey = sender.pickFrom[i]
            temp = sender.dict[dictKey]
        else:
            temp = []
        
        # pass it to list
        if sender.var == 'delimL':
            self.delimL = temp
        elif sender.var == 'delimR':
            self.delimR = temp
        elif sender.var == 'listL':
            self.listL = temp
        elif sender.var == 'listR':
            self.listR = temp
        else:
            pass
    
    
    # diff
    def getSelection(self, sender):
        if Glyphs.font:
            temp = []
            f = Glyphs.font
            if f.selectedLayers:
                for i in f.selectedLayers:
                    temp.append(i.parent.name)
            
            if sender.var == 'delimL':
                self.delimL = temp
                self.w.delimL.set(0)
            elif sender.var == 'delimR':
                self.delimR = temp
                self.w.delimR.set(0)
            elif sender.var == 'listL':
                self.listL = temp
                self.w.listL.set(0)
            elif sender.var == 'listR':
                self.listR = temp 
                self.w.listR.set(0)
            else:
                pass
            
        else:
            pass
    
    
    def button_generateAndOpen(self, sender):
        theString = self.generateString(self.listL, self.listR, self.delimL, self.delimR, self.flip, self.trio, True)
        
        if theString != '':
            self.openTab(theString)
        else:
            pass
    
    
    def button_generateAndCopy(self, sender):
        theString = self.generateString(self.delimL, self.delimR, self.listL, self.listR, self.flip, self.trio, False) 
        
        if theString != '':
            os.system('echo "%s" | pbcopy' % theString) # copy to Clipboard, neat
        else:
            pass
    
    
    def button_saveString(self, sender):
        theString = self.generateString(self.delimL, self.delimR, self.listL, self.listR, self.flip, self.trio, False) 
        
        if theString != '':
            self.saveFile('StringSmash_', theString)
        else:
            pass
    
    
    def button_saveMmStyle(self, sender):
        aList = [x + ' ' + y for y in self.listR for x in self.listL]
        theString = '\n'.join(aList) 
        
        if theString != '':
            theString = '#KPL:P: Generated with StringSmash\n' + theString
            self.saveFile('StringSmash_MM_', theString)
        else:
            pass
    
    
    def makeTimeStamp(self):
        mark = str(datetime.datetime.now())
        mark = mark.replace('-', '')
        mark = mark.replace(' ', '')
        mark = mark.replace(':', '')
        mark = mark.replace('.', '')
        return mark
    
    
    # diff
    def saveFile(self, name, content):
        if Glyphs.font:
            aDir, aFile = os.path.split(Glyphs.font.filepath)
        else:
            user = getpass.getuser()
            aDir = '/Users/' + user + '/Desktop'
            # should offer to select a folder
        
        stamp = self.makeTimeStamp()
        path = aDir + '/' + name + stamp + '.txt'
        
        aFile = open(path, 'w')
        aFile.write(content)
        aFile.close()
    
    
    # diff
    def openTab(self, aString):
        Glyphs.currentDocument.windowController().addTabWithString_(aString)
    
    
    ''' this is what needed to successfully generate a string
    the original version was completely refactored, it works now
    '''
    
    def makeString(self, aList, aString, bString):
        '''Makes /A strings using given list's members'''
        pairList = [aString + '/' + a + bString for a in aList]
        return ''.join(pairList)
    
    
    def makePairString(self, aList, bList, aString, bString):
        '''Returns /A/B strings using given lists's members'''
        pairList = [aString + '/' + a + '/' + b + bString for b in bList for a in aList]
        return ''.join(pairList)
    
    
    def makeFlipPairString(self, aList, bList, aString, bString):
        '''Returns /A/B/A/B strings using given lists's members'''
        pairList = [aString + '/' + a + '/' + b + bString + aString + '/' + b + '/' + a + bString for b in bList for a in aList]
        return ''.join(pairList)
    
    
    def makeTrioString(self, aList, bList, aString, bString):
        '''Returns /A/B/A strings using given lists's members'''
        pairList = [aString + '/' + a + '/' + b +'/' + a + bString for b in bList for a in aList]
        return ''.join(pairList)
    
    
    def subsetList(self, aList, bList):
        '''Returns section of two lists—keeps original order of first
        this better use this than 'sets' if you need the original order'''
        temp = [a for a in aList if a in bList]
        return temp
    
    
    def removeEmptyString(self, aList):
        '''Removes empty string elements from list'''
        newList = [a for a in aList if a != '']
        return newList
    
    
    def listToString(self, aList):
        '''Convert delimiter list to delimiter string'''
        if len(aList) == 0:
            return ''
        if len(aList) == 1:
            return '/' + aList[0]
        if len(aList) > 1:
            return '/' + '/'.join(aList)
    
    
    def generateString(self, listL, listR, delimL, delimR, flip, trio, subset):
        '''This generates strings'''
        if subset == True:
            # subset lists
            listL =  self.subsetList(self.listL, self.font)
            listR =  self.subsetList(self.listR, self.font)
            delimL = self.subsetList(self.delimL, self.font)
            delimR = self.subsetList(self.delimR, self.font)
            
            delimL =  self.listToString(self.removeEmptyString(delimL))
            delimR =  self.listToString(self.removeEmptyString(delimR))
        else:
            listL = self.listL
            listR = self.listR
            delimL = self.delimL
            delimR = self.delimR
            
            delimL =  self.listToString(self.removeEmptyString(delimL))
            delimR =  self.listToString(self.removeEmptyString(delimR))
        
        # both empty list
        if not listL and not listR:
            return 'No string at all'
        
        # neither list is empty   
        elif listL and listR:
            if trio:
                return self.makeTrioString(listL, listR, delimL, delimR)
            if flip:
                return self.makeFlipPairString(listL, listR, delimL, delimR)
            else:
                return self.makePairString(listL, listR, delimL, delimR)       
        
        # both empty list
        elif not listL and not listR :
            return ''
        
        # first list is an empty list
        elif listL == [] and delimL and delimR:
            listL = ['']
            listL, listR = listR, listR
            return self.makeString(listL, delimL, delimR)
        
        # second list is an empty list
        elif listR == [] and delimL and delimR:
            listR = ['']
            return self.makeString(listL, delimL, delimR)
        
        else:
            return 'No string at all'

StringSmash()