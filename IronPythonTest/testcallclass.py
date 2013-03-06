#-*- coding:utf-8 -*-
'''
Created on 2013-3-6

@author: GFTOwenWang
'''
import clr
clr.AddReference("System.Windows.Forms")

from System.Windows.Forms import *

form = Form(Text="Hello World Form")
label = Label(Text="Hello World!")

form.Controls.Add(label)

Application.Run(form)
