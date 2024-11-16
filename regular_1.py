import re
string="""hello my number is 1234 and $ my friend number is 0987"""
regex='\d+' #number seperate 
# regex='\D+' # words seperate without numbers
# regex='\S+' # all words,number,special seperate
# regex='\W+' # special character seperate
matches=re.findall(regex,string)
print(matches)