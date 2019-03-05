

class Helper:
    ACTIONS = ["tag", "untag"]
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

    # @classmethod
    # def HELP_ADD(cls, cmd, para):
    #     para = para if para else "[label|sn|url]"
    #     return  {
    #                 "Title": "to add %s" % para,
    #                 "SubTitle": "Typing <todo add [label|sn|url]> for adding a new url",
    #                 "IcoPath": "Images/add.png",
    #                 "JsonRPCAction": {
    #                     "method": "add",
    #                     "parameters": [para, ],
    #                     "dontHideAfterAction": True
    #                 }
    #             }

    # @classmethod
    # def HELP_ERASE(cls, cmd, para):
    #     para = "[%s] NOT FOUND"%para if para else "[label|sn]"
    #     return  {
    #                 "Title": "to erase %s" % para,
    #                 "SubTitle": "Typing <todo erase [label|sn|]>, the last | for confirming to erase a short name",
    #                 "IcoPath": "Images/erase.png",
    #                 "JsonRPCAction": {
    #                     "method": "erase",
    #                     "parameters": [para, ],
    #                     "dontHideAfterAction": True
    #                 }
    #             }

    # @classmethod
    # def HELP_DELETE(cls, cmd, para):
    #     para = "[%s] NOT FOUND"%para if para else "[label||]"
    #     return  {
    #                 "Title": "to delete %s" % para,
    #                 "SubTitle": "Typing <todo delete [label||]>, the last double | for confirming to delete a label",
    #                 "IcoPath": "Images/delete.png",
    #                 "JsonRPCAction": {
    #                     "method": "delete",
    #                     "parameters": [para, ],
    #                     "dontHideAfterAction": True
    #                 }
    #             }

    # @classmethod
    # def Show(cls, cmd = None, para = None):
    #     if cmd and hasattr(cls, "HELP_%s"%cmd.upper()):
    #         return [ getattr(cls, "HELP_%s"%cmd.upper())(cmd, para) ]
    #     else:
    #         return  [
    #                     cls.HELP_NONE(cmd),
    #                     cls.HELP_ADD(cmd, para),
    #                     cls.HELP_ERASE(cmd, para),
    #                     cls.HELP_DELETE(cmd, para)
    #                 ]

    @classmethod
    def ShowList(cls, descript, data, fn_para, click_fn):
        from random import randint
        return  {
                    "Title": "%s" % (descript),
                    "SubTitle": "url: %s" % data,
                    "IcoPath": "Images/click%s.png"%randint(0,3),
                    "JsonRPCAction": {
                        "method": u"%s"%click_fn,
                        "parameters": [fn_para, ],
                        "dontHideAfterAction": True
                    }
                }

    @classmethod
    def SHOW_TAG(cls, para):
        return  {
                    "Title": "tag %s" % (para),
                    "SubTitle": "You can tag mutil labels for url, i.e. tag label1 label2 url",
                    "IcoPath": "Images/add.png",
                    "JsonRPCAction": {
                        "method": "tag",
                        "parameters": [para, ],
                        "dontHideAfterAction": True
                    }
                }

    @classmethod
    def SHOW_UNTAG(cls, para):
        return  {
                    "Title": "untag %s" % (para),
                    "SubTitle": "You can untag labelX for url, i.e. untag labelX and choose url",
                    "IcoPath": "Images/erase.png",
                    "JsonRPCAction": {
                        "method": "untag",
                        "parameters": [para, ],
                        "dontHideAfterAction": True
                    }
                }


    @classmethod
    def ShowCmd(cls, cmd, para):
        return getattr(cls, "SHOW_%s"%cmd.upper())(para)
