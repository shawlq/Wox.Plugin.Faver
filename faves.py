from log import logger
from data import Info
class ToSee:

    @classmethod
    def Alert(cls, title, content):
        from wox import WoxAPI
        WoxAPI.show_msg(title, content, r"./Images/pic.png")

    @classmethod
    def Add(cls, para):
        #para: [label|sn|data]
        label, sn, data = Info.Parse2Str(para)
        label = label if label else Info.DEFAULT
        if not label or not sn or not data:
            logger.info("ToSee.Add:%s,%s,%s.", label, sn, data)
            return

        if Info.Save(label, sn, data):
            cls.Alert("Success Saved!", "%s"%str(data))


    @classmethod
    def Erase(cls, para):
        #para: [label|sn]
        label, sn, _ = Info.Parse2Str(para)
        if Info.Erase(label, sn):
            cls.Alert("Success Erased!", "[%s] <%s>"%(label, sn))
            return True
        return False

        
    @classmethod
    def Delete(cls, para):
        #para: [label]
        label, _, _ = Info.Parse2Str(para)
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
        