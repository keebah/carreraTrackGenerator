# carreraTrackGenerator
Small tool to generate very simple tracks for carrera evolution model race track system

# Track Layout definition

The tool currently supports straights and 60° corners. The track layout is defined as a list of strings.

- s: a straight
- l: a left hand turn of 60°
- r: a right hand turn of 60°

A track layout defined as ['r','r','r','r','r','r'] would therefore be a full circle of right hand corners. Obviously it doesn't have a start/finish section so the smallest possible track would be an ['s','r','r','r','s','r','r','r'].

# Validity checking
A valid track is one where the start and end points are identical. Also the heading of the vehicle should be identical. This is the case for a heading as multitudes of a full circle. Assuming starting with 0 valid headings for the last point of the track are -360, 0, 360, ... Typical race tracks do have a heading of either -360 or 360 deg. An well-known example of a racetrack with a heading of 0 is Suzuka. https://de.wikipedia.org/wiki/Suzuka_International_Racing_Course.

# Fairness checking
The driver cannot chose the driving lane at the entry level carrera kit. To ensure fairness the track should therefore be equal length for the left and right corners. This is the case for a heading being 0. The check validity function of the tool is checking for the start and end point to be equal and the heading to be 0.

# Search function
The tool can search for a valid track configuration using the parts available to the user. The quantity of straights and corners needs to be set, afterwards a random search algorithm will try to find suitable tracks. The validity function is described in the section "validity checking"
