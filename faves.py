from log import logger
from data import Info
class ToSee:

    @classmethod
    def Alert(cls, title, content):
        from wox import WoxAPI
        WoxAPI.show_msg(title, content, r"./Images/pic.png")

    @classmethod
    def Parse(cls, para):
        return Info.Parse2Str(para)

    @classmethod
    def Add(cls, para):
        #para: [label|sn|data] 
        label, sn, data = cls.Parse(para)
        label = label if label else Info.DEFAULT
        if not label or not sn or not data:
            return

        if Info.Save(label, sn, data):
            cls.Alert("Success Saved!", "%s"%str(data))


    @classmethod
    def Erase(cls, para):
        #para: [label|sn|] using last | for confirm erasing the sn of label
        label, sn, data = cls.Parse(para)
        if not label or not sn or data is not '': #data must be empty not None.
            return False
        if Info.Erase(label, sn):
            cls.Alert("Success Erased!", "[%s] <%s>"%(label, sn))
            return True
        return False

        
    @classmethod
    def Delete(cls, para):
        #para: [label||] using last || for confirm deleting label
        label, sn, data = cls.Parse(para) #sn, data must be empty not None.
        if not label or sn is not '' or data is not '':
            return False
        if Info.Delete(label):
            cls.Alert("Success Deleted!", "[%s]"%label)
            return True
        return False
        
    @classmethod
    def List(cls, label, sn):
        return Info.Get(label, sn)

        
    @classmethod
    def Click(cls, url):
        import webbrowser
        webbrowser.open(url)
        