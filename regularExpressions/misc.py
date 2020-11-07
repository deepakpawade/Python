import re
                       
                        # wildcard (dot) wwcharacter 
atRegex = re.compile(r'.T')  #it provides a list, where each element of the list
# has the regex character and one character before it
# so there should atleast be one character before the provided regex, present in the search string 
# to be able to extract it
# print(atRegex.findall(""" The. cat. in the hat sat on the flat mat."""))



                    #   Dot-Star
nameRegex = re.compile(r'First Name:(.*) Last Name:(.*)')
mo = nameRegex.search('First Name:Al Last Name:Sweigart')
# print(mo.group(1))
# print(mo.group(2))

nongreedyRegex = re.compile(r'<.*?>') #Match an opening angle bracket, followed by anything, 
#followed by a closing angle bracket.” 
# But the string '<To serve man> for dinner.>' has two possible matches for the closing angle bracket.
#In the non-greedy version of the regex, Python matches the shortest possible string: '<To serve man>'.
mo = nongreedyRegex.search('<To serve man> for dinner.>')
# print(mo.group())

                    #newlines with dot-star
newlineRegex = re.compile('.*', re.DOTALL)
print(newlineRegex.search('Serve the public trust\nProtect the innocent.\nUphold the law.').group())

lineRegex = re.compile('.*')
print(lineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
