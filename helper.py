

class Helper:
    ACTIONS = ["add", "erase", "delete"]
    @classmethod
    def HELP_NONE(cls, cmd):

        return  {
                    "Title": "Not Found <%s>" % cmd,
                    "SubTitle": "",
                    "IcoPath": "Images/notfound.png",
                    "JsonRPCAction": {
                        "method": "donothing",
                        "parameters": ["", ],
                        "dontHideAfterAction": True
                    }
                }

    @classmethod
    def HELP_ADD(cls, cmd, para):
        para = para if para else "[label|sn|url]"
        return  {
                    "Title": "to add %s" % para,
                    "SubTitle": "Typing <todo add [label|sn|url]> for adding a new url",
                    "IcoPath": "Images/add.png",
                    "JsonRPCAction": {
                        "method": "add",
                        "parameters": [para, ],
                        "dontHideAfterAction": True
                    }
                }

    @classmethod
    def HELP_ERASE(cls, cmd, para):
        para = para if para else "[label|sn]"
        return  {
                    "Title": "to erase [%s] NOT FOUND" % para,
                    "SubTitle": "Typing <todo erase [label|sn|]>, the last | for confirming to erase a short name",
                    "IcoPath": "Images/erase.png",
                    "JsonRPCAction": {
                        "method": "erase",
                        "parameters": [para, ],
                        "dontHideAfterAction": True
                    }
                }

    @classmethod
    def HELP_DELETE(cls, cmd, para):
        para = para if para else "[label]"
        return  {
                    "Title": "to delete [%s] NOT FOUND" % para,
                    "SubTitle": "Typing <todo delete [label||]>, the last double | for confirming to delete a label",
                    "IcoPath": "Images/delete.png",
                    "JsonRPCAction": {
                        "method": "delete",
                        "parameters": [para, ],
                        "dontHideAfterAction": True
                    }
                }

    @classmethod
    def Show(cls, cmd = None, para = None):
        if cmd and hasattr(cls, "HELP_%s"%cmd.upper()):
            return [ getattr(cls, "HELP_%s"%cmd.upper())(cmd, para) ]
        else:
            return  [
                        cls.HELP_NONE(cmd),
                        cls.HELP_ADD(cmd, para),
                        cls.HELP_ERASE(cmd, para),
                        cls.HELP_DELETE(cmd, para)
                    ]

    @classmethod
    def ShowList(cls, label, sn, data, fn_para, click_fn):
        from random import randint
        return  {
                    "Title": "[%s] <%s>" % (label, sn),
                    "SubTitle": "url: %s" % data,
                    "IcoPath": "Images/click%s.png"%randint(0,2),
                    "JsonRPCAction": {
                        "method": click_fn,
                        "parameters": [fn_para, ],
                        "dontHideAfterAction": True
                    }
                }