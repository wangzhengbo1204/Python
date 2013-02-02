#-*- coding:utf-8 -*-
'''
Created on 2012-9-20

@author: GFTOwenWang
'''
import cgi
import cgitb; 

cgitb.enable()  # for troubleshooting

print "Content-type: text/html"
print

print """
<html>

<head><title>Sample CGI Script</title></head>

<body>

  <h3> Sample CGI Script </h3>
"""

form = cgi.FieldStorage()
message = form.getvalue("message", "(no message)")

print """

  <p>Previous message: %s</p>

  <p>form

  <form method="post" action="index.cgi">
    <p>message: <input type="text" value="owen" name="message"/></p>
  </form>

""" % cgi.escape(message)

message = form.getvalue("message", "(no message)")

print """

  <p>Previous message: %s</p>


</body>

</html>
""" % cgi.escape(message)