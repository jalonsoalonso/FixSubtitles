"""
Description: module to fix subtitle files with SRT format.

From and original SRT file, it is possible to generate a new version by either
1) Setting the first dialogue time to a specific value using 
   the syntax "hh:mm:ss,lll".
2) Shifting all the dialogues for a specific amount of seconds with
   float point precision.

Last update: April 15th, 2022 

Example uses:
1) Set the starting time to 1 second
createSRTFromFileStart('StarWarsIV.srt','start.srt','00:00:01,000')
2) Set the starting time to 1 hour, 1 minute, 1 second, 999 milliseconds
createSRTFromFileStart('StarWarsIV.srt','start.srt','01:01:01,999')
3) Shift time values 1.5 seconds
createSRTFromFileShift('StarWarsIV.srt','shift1.srt',1.5)
4) Shift time values -30.2 seconds
createSRTFromFileShift('StarWarsIV.srt','shift2.srt',-30.2)

SRT Protocol: list of sequences
Sequence:
	sequence number
	hh:mm:ss,lll --> hh:mm:ss,lll
	text
	[text]
	\n
SRT example file:
	1
	00:02:48,336 --> 00:02:50,171
	Did you hear that?

	2
	00:02:50,255 --> 00:02:53,508
	They shut down the main reactor.
	We'll be destroyed for sure.

	3
	00:02:53,591 --> 00:02:54,759
	This is madness.
"""

#input: files_source (string), source file name
#       file_dest (string), destination file name
#       offset_time (float), seconds with milliseconds
#output: creates a new file updating all time occurrences shifting them
#        according to the offset_time value
def createSRTFromFileShift(file_source, file_dest, offset_time):
	with open(file_source, 'r') as f:
		data = f.read()
	lseq = data.split('\n\n')

	s = shift(lseq, offset_time)
		
	with open(file_dest, 'w') as f:
		f.write(s)

#input: files_source (string), source file name
#       file_dest (string), destination file name
#       start_time (string), time with syntax "hh:mm:ss,lll"
#output: creates a new file updating all time occurrences setting the initial
#        value to the start_time value
def createSRTFromFileStart(file_source, file_dest, start_time):
	with open(file_source, 'r') as f:
		data = f.read()
	lseq = data.split('\n\n')
	
	lines = lseq[0].split('\n')
	t1, t2 = lines[1].split(' --> ')
	diff = computeDifference(start_time, t1)
	
	s = shift(lseq, diff)
	
	with open(file_dest, 'w') as f:
		f.write(s)

		
""" Auxiliar functions, call hierarchy:
createSRTFromFileShift
  |-- shift
        |-- updateDifference
              |-- getSeconds
	          |-- createTimeString
createSRTFromFileStart
  |-- computeDifference
        |-- getSeconds
  |-- shift
        |-- updateDifference
              |-- getSeconds
	          |-- createTimeString
"""

#input: lseq (list), list of SRT sequences
#       seconds (float), seconds with milliseconds
#output: string, SRT sequences updated according to seconds difference
#        and joined with the '\n\n' string
def shift(lseq, seconds):
	l = []
	for seq in lseq:
		lines = seq.split('\n')
		t1, t2 = lines[1].split(' --> ')
		lines[1] = updateDifference(t1, t2, seconds)
		s = '\n'.join(lines)
		l.append(s)
	s = '\n\n'.join(l)
	return s
      
#input: st1 (string), time with syntax "hh:mm:ss,lll"
#       st2 (string), time with syntax "hh:mm:ss,lll"
#output: float, difference time between st1 and st2 in seconds
def computeDifference(st1, st2):
	t1 = getSeconds(st1)
	t2 = getSeconds(st2)
	return t1-t2

#input: stime (string), time with syntax "hh:mm:ss,lll"
#output: float, number of seconds with milliseconds
def getSeconds(stime):
	hms, ms = stime.split(',')
	h, m, s = hms.split(':')
	t = int(h) * 3600
	t += int(m) * 60
	t += int(s)
	t += int(ms)/1000.0
	return t

#input: st1 (string), time with syntax "hh:mm:ss,lll"
#       st2 (string), time with syntax "hh:mm:ss,lll"
#       diff (float), time in seconds
#output: string with syntax "hh:mm:ss,lll --> hh:mm:ss,lll" resulting
#        from the update of st1 and st2 adding the diff value
def updateDifference(st1, st2, diff):
	t1 = getSeconds(st1)
	t1 += diff
	t2 = getSeconds(st2)
	t2 += diff
	s1 = createTimeString(t1)
	s2 = createTimeString(t2)
	return s1 + ' --> ' + s2

#input: seconds (float), time in seconds
#output: string with syntax "hh:mm:ss,lll"
def createTimeString(seconds):
	t = int(seconds)
	h = t//3600
	m = (t%3600)//60
	s = t%60
	ms = round(seconds - t, 3)
	ms = int(ms * 1000)
	return '{:02d}:{:02d}:{:02d},{:03d}'.format(h,m,s,ms)
