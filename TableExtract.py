import io
import re

row_open = 0
table_open = 0
outvalue = ''
first_time = 1

f = open("myiris.html","r")
of = open("output.txt","a")

for line in f:
       if (re.search("<table.*",line) and table_open ==0):
               table_open = 1
               print "Table Open"
               continue

       elif (re.search("<th.*",line)):
               continue

       elif (re.search("<tr.*", line)):
               row_open = 1
               continue

       elif row_open == 1 and re.search('<td(.*)<\/td>',line,re.IGNORECASE):
               if (re.search('<td.*><a href.*><img.*><\/img><\/a><\/td>',line)):
                       continue

               elif (re.search('<a href.*>',line)):
                       data = re.search('<a href.*>(.*)<\/a><\/td>',line,re.IGNORECASE)
                       if data:

                               value = data.group(1)
                               if(first_time):
                                       outvalue = value
                                       first_time = 0
                                       continue
                               else:
                                       outvalue = outvalue + ',' + value
                                       continue

               elif (re.search('<font.*>',line)):
                       data = re.search('<font.*>(.*)<\/font><\/td>',line,re.IGNORECASE)
                       if data:
                               value = data.group(1)
                               if(first_time):
                                       outvalue = value
                                       first_time = 0
                                       continue
                               else:
                                       outvalue = outvalue + ',' + value
                                       continue

               else:
                       data = re.search('<td.*>(.*)<\/td>',line,re.IGNORECASE)
                       if data:
                               value = data.group(1)
                               if(first_time):
                                       outvalue = value
                                       first_time = 0
                                       continue
                               else:
                                       outvalue = outvalue + ',' + value
                                       continue

       elif (re.search("<\/tr.*",line) and row_open ==1):
               outvalue = outvalue + "\n"
               of.write(outvalue)
               row_open = 0
               outvalue = ''
               first_time = 1
               continue

       elif (re.search("<\/table.*",line) and table_open ==1):
               table_open = 0
               of.close()
               print "Table Close"
       else: continue

