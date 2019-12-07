#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on Sat Dec  7 15:13:54 2019
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'ps6'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/laurenvomberg/Documents/U of T fall classes/Coding/Psychopy/ps6.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1,1,1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instructions_2"
instructions_2Clock = core.Clock()
instructions = visual.TextStim(win=win, name='instructions',
    text='In this experiment, you will be presented with 2 tones. Your job is to identify whether the tones went up or down; that is, was the second tone higher or lower than the first? If you think the second tone was higher, please press “m”. If you think the second tone was lower, please press “z”. The instructions will remain on the screen for the duration of the experiment. \n\nYou will be presented with a series of trials and receive feedback for your responses.\n\nPlease ask the experimenter if you have any questions. If you do not have any questions, please press the spacebar to proceed with the experiment. \n',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp1 = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
sound1_1 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound1_1')
sound1_1.setVolume(1)
sound1_2 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound1_2')
sound1_2.setVolume(1)
higher_lower_msg = visual.TextStim(win=win, name='higher_lower_msg',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
feedback_2 = visual.TextStim(win=win, name='feedback_2',
    text='Any text\n\nincluding line breaks',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "the_end"
the_endClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Thank you for participating!',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions_2"-------
# update component parameters for each repeat
key_resp1.keys = []
key_resp1.rt = []
# keep track of which components have finished
instructions_2Components = [instructions, key_resp1]
for thisComponent in instructions_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instructions_2"-------
while continueRoutine:
    # get current time
    t = instructions_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions* updates
    if instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions.frameNStart = frameN  # exact frame index
        instructions.tStart = t  # local t and not account for scr refresh
        instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions, 'tStartRefresh')  # time at next scr refresh
        instructions.setAutoDraw(True)
    
    # *key_resp1* updates
    waitOnFlip = False
    if key_resp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp1.frameNStart = frameN  # exact frame index
        key_resp1.tStart = t  # local t and not account for scr refresh
        key_resp1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp1, 'tStartRefresh')  # time at next scr refresh
        key_resp1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp1.status == STARTED and not waitOnFlip:
        theseKeys = key_resp1.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp1.keys = theseKeys.name  # just the last key pressed
            key_resp1.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions_2"-------
for thisComponent in instructions_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions.started', instructions.tStartRefresh)
thisExp.addData('instructions.stopped', instructions.tStopRefresh)
# check responses
if key_resp1.keys in ['', [], None]:  # No response was made
    key_resp1.keys = None
thisExp.addData('key_resp1.keys',key_resp1.keys)
if key_resp1.keys != None:  # we had a response
    thisExp.addData('key_resp1.rt', key_resp1.rt)
thisExp.addData('key_resp1.started', key_resp1.tStartRefresh)
thisExp.addData('key_resp1.stopped', key_resp1.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructions_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
main_stimuli = data.TrialHandler(nReps=1, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('main_stimuli.xlsx'),
    seed=None, name='main_stimuli')
thisExp.addLoop(main_stimuli)  # add the loop to the experiment
thisMain_stimulu = main_stimuli.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMain_stimulu.rgb)
if thisMain_stimulu != None:
    for paramName in thisMain_stimulu:
        exec('{} = thisMain_stimulu[paramName]'.format(paramName))

for thisMain_stimulu in main_stimuli:
    currentLoop = main_stimuli
    # abbreviate parameter names if possible (e.g. rgb = thisMain_stimulu.rgb)
    if thisMain_stimulu != None:
        for paramName in thisMain_stimulu:
            exec('{} = thisMain_stimulu[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    # update component parameters for each repeat
    sound1_1.setSound(sound1, secs=1.0, hamming=True)
    sound1_1.setVolume(1, log=False)
    sound1_2.setSound(sound2, secs=1.0, hamming=True)
    sound1_2.setVolume(1, log=False)
    higher_lower_msg.setColor('black', colorSpace='rgb')
    higher_lower_msg.setPos((0, 0))
    higher_lower_msg.setText('Was the second tone higher ("m") or lower ("z") than the first tone?\n\n')
    higher_lower_msg.setFont('Arial')
    higher_lower_msg.setHeight(0.05)
    key_resp.keys = []
    key_resp.rt = []
    # keep track of which components have finished
    trialComponents = [sound1_1, sound1_2, higher_lower_msg, key_resp]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound1_1
        if sound1_1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            sound1_1.frameNStart = frameN  # exact frame index
            sound1_1.tStart = t  # local t and not account for scr refresh
            sound1_1.tStartRefresh = tThisFlipGlobal  # on global time
            sound1_1.play(when=win)  # sync with win flip
        if sound1_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound1_1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound1_1.tStop = t  # not accounting for scr refresh
                sound1_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound1_1, 'tStopRefresh')  # time at next scr refresh
                sound1_1.stop()
        # start/stop sound1_2
        if sound1_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            sound1_2.frameNStart = frameN  # exact frame index
            sound1_2.tStart = t  # local t and not account for scr refresh
            sound1_2.tStartRefresh = tThisFlipGlobal  # on global time
            sound1_2.play(when=win)  # sync with win flip
        if sound1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound1_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound1_2.tStop = t  # not accounting for scr refresh
                sound1_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound1_2, 'tStopRefresh')  # time at next scr refresh
                sound1_2.stop()
        
        # *higher_lower_msg* updates
        if higher_lower_msg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            higher_lower_msg.frameNStart = frameN  # exact frame index
            higher_lower_msg.tStart = t  # local t and not account for scr refresh
            higher_lower_msg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(higher_lower_msg, 'tStartRefresh')  # time at next scr refresh
            higher_lower_msg.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['z', 'm'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp.keys = theseKeys.name  # just the last key pressed
                key_resp.rt = theseKeys.rt
                # was this 'correct'?
                if (key_resp.keys == str(corrAns)) or (key_resp.keys == corrAns):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound1_1.stop()  # ensure sound has stopped at end of routine
    main_stimuli.addData('sound1_1.started', sound1_1.tStartRefresh)
    main_stimuli.addData('sound1_1.stopped', sound1_1.tStopRefresh)
    sound1_2.stop()  # ensure sound has stopped at end of routine
    main_stimuli.addData('sound1_2.started', sound1_2.tStartRefresh)
    main_stimuli.addData('sound1_2.stopped', sound1_2.tStopRefresh)
    main_stimuli.addData('higher_lower_msg.started', higher_lower_msg.tStartRefresh)
    main_stimuli.addData('higher_lower_msg.stopped', higher_lower_msg.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for main_stimuli (TrialHandler)
    main_stimuli.addData('key_resp.keys',key_resp.keys)
    main_stimuli.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        main_stimuli.addData('key_resp.rt', key_resp.rt)
    main_stimuli.addData('key_resp.started', key_resp.tStartRefresh)
    main_stimuli.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if key_resp.keys == corrAns:
        feedback_2 = visual.TextStim(win=win, name='feedback_2',
        text='correct',
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color=[-1,-1,-1], colorSpace='rgb', opacity=1)
        feedback_2.draw()
        win.flip()
        core.wait(3)
    else:
        feedback_2 = visual.TextStim(win=win, name='feedback_2',
        text='incorrect',
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color=[-1,-1,-1], colorSpace='rgb', opacity=1)
        feedback_2.draw()
        win.flip()
        core.wait(3) 
    if not key_resp.keys:
        text="No response recorded"
    # keep track of which components have finished
    feedbackComponents = [feedback_2]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_2* updates
        if feedback_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_2.frameNStart = frameN  # exact frame index
            feedback_2.tStart = t  # local t and not account for scr refresh
            feedback_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_2, 'tStartRefresh')  # time at next scr refresh
            feedback_2.setAutoDraw(True)
        if feedback_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                feedback_2.tStop = t  # not accounting for scr refresh
                feedback_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback_2, 'tStopRefresh')  # time at next scr refresh
                feedback_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    main_stimuli.addData('feedback_2.started', feedback_2.tStartRefresh)
    main_stimuli.addData('feedback_2.stopped', feedback_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'main_stimuli'


# ------Prepare to start Routine "the_end"-------
# update component parameters for each repeat
# keep track of which components have finished
the_endComponents = [text]
for thisComponent in the_endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
the_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "the_end"-------
while continueRoutine:
    # get current time
    t = the_endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=the_endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in the_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "the_end"-------
for thisComponent in the_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# the Routine "the_end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
