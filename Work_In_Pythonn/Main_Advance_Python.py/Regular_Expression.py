'''
expressions are used when we need to find anything in large set of data. 
Syntax:- patter = "Was"
like here i had mention pattern = was which means after running this it will check the hole paragraph and give me the output wheather was is present or not
# match = re.search(patter,text) ---------->> this is the syntax to search.   
'''

import re
pattern = "was"
text = '''
Caitlin Clark (born January 22, 2002) is an American professional basketball player for the Indiana Fever of the Women's National Basketball Association (WNBA).
In her college freshman season with the Iowa Hawkeyes, she earned All-American honors; as a sophomore, Clark was again first-team All-American and in her junior
and senior seasons, she was the national player of the year. She became the Division I women's career and single-season leader in points and is regarded as one of the 
greatest collegiate players of all time. Clark was selected first overall by Indiana Fever in the 2024 WNBA draft. In her first season, she won the WNBA Rookie of the 
Year award, made the All-WNBA First Team and WNBA All-Star Game. At youth international level, Clark won three gold medals with the United States, including two at the 
FIBA Under-19 Women's World Cup. Since her college career, she has helped to popularize women's basketball, a trend known as the "Caitlin Clark effect". (Full article...)
'''
match = re.search(pattern, text)  #--->> if we do this then the loop or the output will be prinrd once because the re.search method breaks the condition on the first time 
# he got matched with pattern. no matter what is there is any-other pattern matched as well but it will ignore it and will print the first matched pattern. 
print(match)





# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------






# Another Example := 
import re

pattern = r"[A-Z]+merican" # here [A-Z] --> represent that all the elements must be in capital letters. In the box[] we write the condition of the pattern.
text = '''
Caitlin Clark (born January 22, 2002) is an American professional basketball player for the Indiana Fever of the Women's National Basketball Association (WNBA).
In her college freshman season with the Iowa Hawkeyes, she earned All-American honors; as a sophomore, Clark was again first-team All-American and in her junior
and senior seasons, she was the national player of the year. Zmerican She became the Division I women's career and single-season leader in points and is regarded as one of the 
greatest collegiate players of all time. Clark was selected first overall by Indiana Fever in the 2024 WNBA draft. In her first season, she won the WNBA Rookie of the 
Year award, made the All-WNBA First Team and WNBA All-Star Game. At youth international level, Clark won three gold medals with the United States, including two at the 
FIBA Under-19 Women's World Cup. Since her college career, she has helped to popularize women's basketball, a trend known as the "Caitlin Clark effect". (Full article...)
'''
matches = re.finditer(pattern,text)
for Match in matches:
    print(Match.span()) #--->> span means the location of the matched condition.
# by this we can find all the elements that are matched by the patter


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Different Types Of Metacharacters Used In Expressions. 

# [] -->  A set of characters	"[a-m]"	
# Example - 
import re
text = "There is rain in spain"
match =  re.findall("[a-m]",text)
print(match)


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# \	 -->  Signals a special sequence (can also be used to escape special characters)	"\d"	
import re 
text = "There are total 89 students"
a = re.findall("\d",text)
print(a)


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# .	 -->  Any character (except newline character)	"he..o"	

import re
txt = "hello planet"
#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
x = re.findall("he..o", txt)
print(x)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ^  -->  Starts with	"^hello"	
import re

txt = "hello planet"

#Check if the string starts with 'hello':

x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# $	 -->  Ends with	"planet$"	
import re

txt = "hello planet"

#Check if the string ends with 'planet':

x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# *	 -->  Zero or more occurrences	"he.*o"	
import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

x = re.findall("he.*o", txt)

print(x)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# +	 -->  One or more occurrences	"he.+o"	
import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":

x = re.findall("he.+o", txt)

print(x)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ?	 -->  Zero or one occurrence	"he.?o"	
import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":

x = re.findall("he.?o", txt)

print(x)

#This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# {} -->  Exactly the specified number of occurrences	"he.{2}o"	
import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

x = re.findall("he.{2}o", txt)

print(x)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# |	 -->  Either or	"falls|stays"	
import re

txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains either "falls" or "stays":

x = re.findall("falls|stays", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# () -->  Capture and group

