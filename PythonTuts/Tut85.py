import re   # re means regular expression

mystr='''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +919719040173
Phone: +919152382638
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
Arpan bhai lekin
bahut hi badia aadmi haiaiin'''

#Meta Characters:

# regular expressions functions:findall,search,split,sub,finditer
# patt = re.compile(r'fass')  # hum regular expression me r(raw string) ka use karte hai
# match=patt.finditer(mystr)
# for i in match:
#     print(i)  # it returns a match object and span values
#     print(mystr[448:452])   # this will print by span value


# patt = re.compile(r'.adm')
# match=patt.finditer(mystr)
# for i in match:
#     print(i)
#     print(mystr[485:489])


# patt = re.compile(r'^Tata')
# match=patt.finditer(mystr)
# for i in match:
#     print(i)
#     print(mystr[0:4])  # mystr[0:4] means slicing


# patt = re.compile(r'iin$')
# match=patt.finditer(mystr)
# # for i in match:
# #     print(i)
# #     print(mystr[485:489])


# patt=re.compile((r'ai*'))
# match=patt.finditer(mystr)
# for i in match:
#     print(i)
    # print(mystr[1:2])  # it prints those items which only have gap of one span
    # print(mystr[141:143])  # it prints those items which have gap of one span as well as gap of two span


# patt=re.compile((r'a*i*'))
# match=patt.finditer(mystr)
# for i in match:
#     print(i)


# patt=re.compile((r'ai+'))
# match=patt.finditer(mystr)
# for i in match:
#     print(i)


# patt = re.compile(r'ai{2}')
# match=patt.finditer(mystr)
# for i in match:
#     print(i)
#     print(mystr[494:497])

# patt = re.compile(r'(ai){2}')
# match=patt.finditer(mystr)
# for i in match:
#     print(i)
#     print(mystr[492:496])

# patt = re.compile(r'(ai){1}')
# match=patt.finditer(mystr)
# for i in match:
#     print(i)

# patt = re.compile(r'ai{1}|t')  # ai{1}|t -> ai or t
# match=patt.finditer(mystr)
# for i in match:
#     print(i)

# patt = re.compile(r'ai{1}|Fax')  # ai{1}|Fax -> ai or Fax
# match=patt.finditer(mystr)
# for i in match:
#     print(i)

#Special Sequences:

# patt=re.compile(r'\ATata')
# match = patt.finditer(mystr)
# for i in match:
#     print(i)

# patt = re.compile(r'\bFax')
# match = patt.finditer(mystr)
# for i in match:
#     print(i)

# patt = re.compile(r'Fax\b')
# match = patt.finditer(mystr)
# for i in match:
#     print(i)

# patt = re.compile(r'27\b')
# match = patt.finditer(mystr)
# for i in match:
#     print(i)

# patt = re.compile(r'\d{5}-\d{4}')
# match = patt.finditer(mystr)
# for i in match:
#     print(i)

patt = re.compile(r'[+91]\d{10}')
match = patt.finditer(mystr)
for i in match:
    print(i)

# Meta Characters:
# [] A set of characters
# \ Signals a special sequence (can also be used to escape special characters)
# . Any character (except newline character)
# ^ Starts with
# $ Ends with
# * Zero or more occurrences
# + One or more occurrences
# {} Exactly the specified number of occurrences
# | Either or
# () Capture and group

# Special Sequences:
# \A Returns a match if the specified characters are at the beginning of the string
# \b Returns a match where the specified characters are at the beginning or at the end of a word r"ain\b"
# \B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
# \d Returns a match where the string contains digits (numbers from 0-9)
# \D Returns a match where the string DOES NOT contain digits
# \s Returns a match where the string contains a white space character
# \S Returns a match where the string DOES NOT contain a white space character
# \w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
# \W Returns a match where the string DOES NOT contain any word characters
# \Z Returns a match if the specified characters are at the end of the string