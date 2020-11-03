#! python3
# mclip.py - A multi-clipboard program
# .bat file to be saved in C:\Users\<username> for direct access to the bat file through win+R (Run)
TEXT = {'agree':""" Yes, I agree. That sounds fine to me.""",
        'busy':""" Sorry, can we do this later this week or next week? """,
        'upsell':""" Would you consider making this a monthly donation? """}
import sys, pyperclip
if len(sys.argv)<2:
    print("Usage: Python mclip.pt [keyphrase] - copy phrase text")
    sys.exit()
keyphrase = sys.argv[1] 
if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for '+ keyphrase)
    
