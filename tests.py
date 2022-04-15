from fix_subtitles import *
#1) Set the starting time to 1 second
createSRTFromFileStart('StarWarsIV.srt','start1.srt','00:00:01,000')
#2) Set the starting time to 1 hour, 1 minute, 1 second, 999 milliseconds
createSRTFromFileStart('StarWarsIV.srt','start2.srt','01:01:01,999')
#3) Shift time values 1.5 seconds
createSRTFromFileShift('StarWarsIV.srt','shift1.srt',1.5)
#4) Shift time values -30.2 seconds
createSRTFromFileShift('StarWarsIV.srt','shift2.srt',-30.2)