

class Helper:
    ACTIONS = ["add", "erase", "delete"]
    @classmethod
    def HELP_NONE(cls, cmd):

        return  {
                    "Title": "delete %s" % cmd,
                    "SubTitle": "",
                    "IcoPath": "Images/pic.png",
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
                    "Title": "todo add %s" % para,
                    "SubTitle": "Typing <todo add [label|sn|url]> for adding a new url",
                    "IcoPath": "Images/pic.png",
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
                    "Title": "todo erase %s" % para,
                    "SubTitle": "Typing <todo erase [label|sn]> for erase a specific short name",
                    "IcoPath": "Images/pic.png",
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
                    "Title": "todo delete %s" % para,
                    "SubTitle": "Typing <todo delete [label]> for delete a specific label",
                    "IcoPath": "Images/pic.png",
                    "JsonRPCAction": {
                        "method": "delete",
                        "parameters": [para, ],
                        "dontHideAfterAction": True
                    }
                }

    @classmethod
    def Show(cls, cmd = None, para = None):
        if cmd and hasattr(cls, "HELP_%s"%cmd.upper()):
            return getattr(cls, "HELP_%s"%cmd.upper())(cmd, para)
        else:
            return  [
                        cls.HELP_NONE(cmd),
                        cls.HELP_ADD(cmd, para),
                        cls.HELP_ERASE(cmd, para),
                        cls.HELP_DELETE(cmd, para)
                    ]

    @classmethod
    def ShowList(cls, label, sn, data, freq, clickcb):
        return  {
                    "Title": "[%s] <%s>" % (label, sn),
                    "SubTitle": "Frequently: %s, url: %s" % (freq, data),
                    "IcoPath": "Images/pic.png",
                    "JsonRPCAction": {
                        "method": clickcb,
                        "parameters": [data, ],
                        "dontHideAfterAction": True
                    }
                }