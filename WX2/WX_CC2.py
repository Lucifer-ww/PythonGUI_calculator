import wx


class Caluculate(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Caluculate, self).__init__(*args, **kwargs)
        self.panel = wx.Panel(self)
        self.printbtn = wx.TextCtrl(
            self.panel, style=wx.TE_MULTILINE | wx.HSCROLL)
        self.num1 = wx.Button(self.panel, label="1")
        self.num2 = wx.Button(self.panel, label="2")
        self.num3 = wx.Button(self.panel, label="3")
        self.num4 = wx.Button(self.panel, label="+")
        self.num5 = wx.Button(self.panel, label="4")
        self.num6 = wx.Button(self.panel, label="5")
        self.num7 = wx.Button(self.panel, label="6")
        self.num8 = wx.Button(self.panel, label="-")
        self.num9 = wx.Button(self.panel, label="7")
        self.num10 = wx.Button(self.panel, label="8")
        self.num11 = wx.Button(self.panel, label="9")
        self.num12 = wx.Button(self.panel, label="*")
        self.num13 = wx.Button(self.panel, label="0")
        self.num14 = wx.Button(self.panel, label=".")
        self.num15 = wx.Button(self.panel, label="=")
        self.num16 = wx.Button(self.panel, label="/")

        self.Boxset()
        self.Event_bind()
        self.Show()

    def Boxset(self):
        sbox1 = wx.BoxSizer()
        sbox2 = wx.BoxSizer()
        sbox3 = wx.BoxSizer()
        sbox4 = wx.BoxSizer()
        sbox5 = wx.BoxSizer()
        vbox = wx.BoxSizer(wx.VERTICAL)
        sbox1.Add(self.printbtn, proportion=1, flag=wx.EXPAND |
                  wx.LEFT | wx.RIGHT | wx.DOWN, border=5)
        sbox2.Add(self.num1, proportion=1, flag=wx.EXPAND | wx.LEFT, border=5)
        sbox2.Add(self.num2, proportion=1, flag=wx.EXPAND |
                  wx.LEFT | wx.RIGHT, border=2)
        sbox2.Add(self.num3, proportion=1, flag=wx.EXPAND |
                  wx.LEFT | wx.RIGHT, border=2)
        sbox2.Add(self.num4, proportion=1, flag=wx.EXPAND | wx.RIGHT, border=5)
        sbox3.Add(self.num5, proportion=1, flag=wx.EXPAND | wx.LEFT, border=5)
        sbox3.Add(self.num6, proportion=1, flag=wx.EXPAND |
                  wx.LEFT | wx.RIGHT, border=2)
        sbox3.Add(self.num7, proportion=1, flag=wx.EXPAND |
                  wx.LEFT | wx.RIGHT, border=2)
        sbox3.Add(self.num8, proportion=1, flag=wx.EXPAND | wx.RIGHT, border=5)
        sbox4.Add(self.num9, proportion=1, flag=wx.EXPAND | wx.LEFT, border=5)
        sbox4.Add(self.num10, proportion=1, flag=wx.EXPAND |
                  wx.LEFT | wx.RIGHT, border=2)
        sbox4.Add(self.num11, proportion=1, flag=wx.EXPAND |
                  wx.LEFT | wx.RIGHT, border=2)
        sbox4.Add(self.num12, proportion=1,
                  flag=wx.EXPAND | wx.RIGHT, border=5)
        sbox5.Add(self.num13, proportion=1, flag=wx.EXPAND | wx.LEFT, border=5)
        sbox5.Add(self.num14, proportion=1, flag=wx.EXPAND |
                  wx.LEFT | wx.RIGHT, border=2)
        sbox5.Add(self.num15, proportion=1, flag=wx.EXPAND |
                  wx.LEFT | wx.RIGHT, border=2)
        sbox5.Add(self.num16, proportion=1,
                  flag=wx.EXPAND | wx.RIGHT, border=5)
        vbox.Add(sbox1, proportion=1, flag=wx.EXPAND | wx.ALL, border=2)
        vbox.Add(sbox2, proportion=1, flag=wx.EXPAND | wx.ALL, border=2)
        vbox.Add(sbox3, proportion=1, flag=wx.EXPAND | wx.ALL, border=2)
        vbox.Add(sbox4, proportion=1, flag=wx.EXPAND | wx.ALL, border=2)
        vbox.Add(sbox5, proportion=1, flag=wx.EXPAND | wx.ALL, border=2)
        self.panel.SetSizer(vbox)

    def test1appd(self, event):
        prv_result = self.printbtn.GetValue()
        self.printbtn.AppendText("1")

    def test2appd(self, event):
        self.printbtn.AppendText("2")

    def test3appd(self, event):
        self.printbtn.AppendText("3")

    def test4appd(self, event):
        self.printbtn.AppendText("+")

    def test5appd(self, event):
        self.printbtn.AppendText("4")

    def test6appd(self, event):
        self.printbtn.AppendText("5")

    def test7appd(self, event):
        self.printbtn.AppendText("6")

    def test8appd(self, event):
        self.printbtn.AppendText("-")

    def test9appd(self, event):
        self.printbtn.AppendText("7")

    def test10appd(self, event):
        self.printbtn.AppendText("8")

    def test11appd(self, event):
        self.printbtn.AppendText("9")

    def test12appd(self, event):
        self.printbtn.AppendText("*")

    def test13appd(self, event):
        self.printbtn.AppendText("0")

    def test14appd(self, event):
        self.printbtn.AppendText(".")

    def test15appd(self, event):
        pre_result = str(self.printbtn.GetValue())
        result = eval(pre_result)
        self.printbtn.SetValue(str(result))

    def test16appd(self, event):
        self.printbtn.AppendText("/")

    def Event_bind(self):
        self.num1.Bind(wx.EVT_BUTTON, self.test1appd)
        self.num2.Bind(wx.EVT_BUTTON, self.test2appd)
        self.num3.Bind(wx.EVT_BUTTON, self.test3appd)
        self.num4.Bind(wx.EVT_BUTTON, self.test4appd)
        self.num5.Bind(wx.EVT_BUTTON, self.test5appd)
        self.num6.Bind(wx.EVT_BUTTON, self.test6appd)
        self.num7.Bind(wx.EVT_BUTTON, self.test7appd)
        self.num8.Bind(wx.EVT_BUTTON, self.test8appd)
        self.num9.Bind(wx.EVT_BUTTON, self.test9appd)
        self.num10.Bind(wx.EVT_BUTTON, self.test10appd)
        self.num11.Bind(wx.EVT_BUTTON, self.test11appd)
        self.num12.Bind(wx.EVT_BUTTON, self.test12appd)
        self.num13.Bind(wx.EVT_BUTTON, self.test13appd)
        self.num14.Bind(wx.EVT_BUTTON, self.test14appd)
        self.num15.Bind(wx.EVT_BUTTON, self.test15appd)
        self.num16.Bind(wx.EVT_BUTTON, self.test16appd)


if __name__ == "__main__":
    app = wx.App()
    Caluculate(None, title="计算器")
    app.MainLoop()
