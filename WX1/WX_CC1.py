#!/usr/bin/python
# -*- coding: utf-8 -*-

# calculator.py

import wx


class Example(wx.Frame):
    bianliang1 = '0'
    bianliang2 = '0'
    judge = ""

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(300, 250))

        self.InitUI()
        self.Centre()
        self.Show()

    def OnButtonClick0(self, event):
        var = self.display.GetValue()
        var = int(var)*10 + 0
        self.display.Value = str(var)

    def OnButtonClick1(self, event):
        var = self.display.GetValue()
        var = int(var)*10 + 1
        self.display.Value = str(var)

    def OnButtonClick2(self, event):
        var = self.display.GetValue()
        var = int(var)*10 + 2
        self.display.Value = str(var)

    def OnButtonClick3(self, event):
        var = self.display.GetValue()
        var = int(var)*10 + 3
        self.display.Value = str(var)

    def OnButtonClick4(self, event):
        var = self.display.GetValue()
        var = int(var)*10 + 4
        self.display.Value = str(var)

    def OnButtonClick5(self, event):
        var = self.display.GetValue()
        var = int(var)*10 + 5
        self.display.Value = str(var)

    def OnButtonClick6(self, event):
        var = self.display.GetValue()
        var = int(var)*10 + 6
        self.display.Value = str(var)

    def OnButtonClick7(self, event):
        var = self.display.GetValue()
        var = int(var)*10 + 7
        self.display.Value = str(var)

    def OnButtonClick8(self, event):
        var = self.display.GetValue()
        var = int(var)*10 + 8
        self.display.Value = str(var)

    def OnButtonClick9(self, event):
        var = self.display.GetValue()
        var = int(var)*10 + 9
        self.display.Value = str(var)

    def OnButtonCls(self, event):
        self.display.Value = '0'

    def OnButtonBck(self, event):
        var = self.display.GetValue()
        var = int(var)/10
        self.display.Value = str(var)

    def OnButtonClickClose(self, event):
        wx.Exit()

    def OnButtonClickJia(self, event):
        self.bianliang1 = self.display.GetValue()
        self.display.Value = '0'
        self.judge = "+"

    def OnButtonClickJian(self, event):
        self.bianliang1 = self.display.GetValue()
        self.display.Value = '0'
        self.judge = "-"

    def OnButtonClickChe(self, event):
        self.bianliang1 = self.display.GetValue()
        self.display.Value = '0'
        self.judge = "*"

    def OnButtonClickChu(self, event):
        self.bianliang1 = self.display.GetValue()
        self.display.Value = '0'
        self.judge = "/"

    def OnButtonClickEqu(self, event):
        bianliang2 = self.display.GetValue()
        if self.judge == '+':
            self.display.Value = str(int(self.bianliang1)+int(bianliang2))
        elif self.judge == '-':
            self.display.Value = str(int(self.bianliang1)-int(bianliang2))
        elif self.judge == '*':
            self.display.Value = str(int(self.bianliang1)*int(bianliang2))
        elif self.judge == '/':
            self.display.Value = str(int(self.bianliang1)/int(bianliang2))

    def InitUI(self):

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        vbox = wx.BoxSizer(wx.VERTICAL)
        self.display = wx.TextCtrl(self, style=wx.TE_RIGHT, value='0')
        vbox.Add(self.display, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=4)
        gs = wx.GridSizer(5, 5, 5, 5)

        buttonCls = wx.Button(self, label='Cls')
        buttonBck = wx.Button(self, label='Bck')
        buttonClose = wx.Button(self, label='Close')
        button7 = wx.Button(self, label='7')
        button8 = wx.Button(self, label='8')
        button9 = wx.Button(self, label='9')
        buttonChu = wx.Button(self, label='/')
        button4 = wx.Button(self, label='4')
        button5 = wx.Button(self, label='5')
        button6 = wx.Button(self, label='6')
        buttonChen = wx.Button(self, label='*')
        button1 = wx.Button(self, label='1')
        button2 = wx.Button(self, label='2')
        button3 = wx.Button(self, label='3')
        buttonJian = wx.Button(self, label='-')
        button0 = wx.Button(self, label='0')
        buttonDot = wx.Button(self, label='.')
        buttonEqu = wx.Button(self, label='=')
        buttonPlus = wx.Button(self, label='+')

        gs.AddMany([
            (buttonCls, 0, wx.EXPAND),
            (buttonBck, 0, wx.EXPAND),
            (wx.StaticText(self), wx.EXPAND),
            (buttonClose, 0, wx.EXPAND),
            (button7, 0, wx.EXPAND),
            (button8, 0, wx.EXPAND),
            (button9, 0, wx.EXPAND),
            (buttonChu, 0, wx.EXPAND),
            (button4, 0, wx.EXPAND),
            (button5, 0, wx.EXPAND),
            (button6, 0, wx.EXPAND),
            (buttonChen, 0, wx.EXPAND),
            (button1, 0, wx.EXPAND),
            (button2, 0, wx.EXPAND),
            (button3, 0, wx.EXPAND),
            (buttonJian, 0, wx.EXPAND),
            (button0, 0, wx.EXPAND),
            (buttonDot, 0, wx.EXPAND),
            (buttonEqu, 0, wx.EXPAND),
            (buttonPlus, 0, wx.EXPAND)
        ])

        buttonCls.Bind(wx.EVT_BUTTON, self.OnButtonCls)
        buttonBck.Bind(wx.EVT_BUTTON, self.OnButtonBck)
        buttonClose.Bind(wx.EVT_BUTTON, self.OnButtonClickClose)
        button0.Bind(wx.EVT_BUTTON, self.OnButtonClick0)
        button1.Bind(wx.EVT_BUTTON, self.OnButtonClick1)
        button2.Bind(wx.EVT_BUTTON, self.OnButtonClick2)
        button3.Bind(wx.EVT_BUTTON, self.OnButtonClick3)
        button4.Bind(wx.EVT_BUTTON, self.OnButtonClick4)
        button5.Bind(wx.EVT_BUTTON, self.OnButtonClick5)
        button6.Bind(wx.EVT_BUTTON, self.OnButtonClick6)
        button7.Bind(wx.EVT_BUTTON, self.OnButtonClick7)
        button8.Bind(wx.EVT_BUTTON, self.OnButtonClick8)
        button9.Bind(wx.EVT_BUTTON, self.OnButtonClick9)
        buttonEqu.Bind(wx.EVT_BUTTON, self.OnButtonClickEqu)
        buttonPlus.Bind(wx.EVT_BUTTON, self.OnButtonClickJia)
        buttonJian.Bind(wx.EVT_BUTTON, self.OnButtonClickJian)
        buttonChen.Bind(wx.EVT_BUTTON, self.OnButtonClickChe)
        buttonChu.Bind(wx.EVT_BUTTON, self.OnButtonClickChu)

        vbox.Add(gs, proportion=1, flag=wx.EXPAND)
        self.SetSizer(vbox)


app = wx.App()
Example(None, title='Calculator')
app.MainLoop()
