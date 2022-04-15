# FixSubtitles
Module to fix subtitle files with SRT format.

From and original SRT file, it is possible to generate a new version by either
- Setting the first dialogue time to a specific value using the syntax "hh:mm:ss,lll".
- Shifting all the dialogues for a specific amount of seconds with float point precision.

Example uses:

Set the starting time to 1 second

	createSRTFromFileStart('StarWarsIV.srt','start.srt','00:00:01,000')

Set the starting time to 1 hour, 1 minute, 1 second, 999 milliseconds

	createSRTFromFileStart('StarWarsIV.srt','start.srt','01:01:01,999')

Shift time values 1.5 seconds

	createSRTFromFileShift('StarWarsIV.srt','shift1.srt',1.5)

Shift time values -30.2 seconds

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
