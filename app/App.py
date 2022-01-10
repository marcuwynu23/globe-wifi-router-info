import wx  
class MainPanel(wx.Panel):
    def __init__(self,parent,id):
        wx.Panel.__init__(self,parent,id,style=wx.BORDER_SIMPLE)

class MainFrame(wx.Frame):
    def __init__(self,parent,id,style):
        wx.Frame.__init__(self,parent=parent,id=id,style=style)
        
    def add_data(self,data):
        self.data = data

    def SetBodyInitial(self):
        mainPanel = MainPanel(self,-1)
        mainPanel.SetBackgroundColour("#343434")

        st = wx.StaticText(mainPanel,label=str(self.data),style=wx.ALIGN_LEFT|wx.EXPAND)
        st.SetForegroundColour("white")
        font = wx.Font(12,family=wx.FONTFAMILY_DEFAULT,style=0,weight=wx.BOLD)
        st.SetFont(font)
        self.SetLabel("Wifi Router Information")
        self.SetSize((400,650))
        self.SetSizeHints((400,650))
        self.SetMaxSize((400,650))
        self.SetMinSize((400,650))
        self.Centre()
        self.Show(True)

class Application:
    def __init__(self):
        self.app = wx.App()
        self.mainFrame = MainFrame(None,-1,style=wx.DEFAULT_FRAME_STYLE) 
        
    def set_data(self,data):
        self.mainFrame.add_data(data)
        self.mainFrame.SetBodyInitial()
    def run(self):
        self.app.MainLoop()
