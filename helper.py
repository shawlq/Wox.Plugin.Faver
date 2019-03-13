

class Helper:
    @classmethod
    def HELP_NONE(cls, msg):
        return  {
                    "Title": "%s" % msg,
                    "SubTitle": "",
                    "IcoPath": "Images/notfound.png",
                    "JsonRPCAction": {
                        "method": "donothing",
                        "parameters": ["", ],
                        "dontHideAfterAction": True
                    }
                }

    @classmethod
    def ShowHelp(cls, cmd = None, para = None):
        return  [
                    cls.HELP_TAG(),
                    cls.HELP_UNTAG(),
                    cls.HELP_LIST()
                ]

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
    def HELP_TAG(cls):
        return  {
                    "Title": "tag label url",
                    "SubTitle": "You can tag mutil labels for url, i.e. tag label1 label2 url",
                    "IcoPath": "Images/add.png",
                    "JsonRPCAction": {
                        "method": "donothing",
                        "parameters": ["", ],
                        "dontHideAfterAction": True
                    }
                }

    @classmethod
    def HELP_UNTAG(cls):
        return  {
                    "Title": "untag label",
                    "SubTitle": "You can untag label for url, i.e. untag label and choose url",
                    "IcoPath": "Images/erase.png",
                    "JsonRPCAction": {
                        "method": "donothing",
                        "parameters": ["", ],
                        "dontHideAfterAction": True
                    }
                }

    @classmethod
    def HELP_LIST(cls):
        return  {
                    "Title": "label1 label2",
                    "SubTitle": "You can type mutil labels to quickly find url",
                    "IcoPath": "Images/erase.png",
                    "JsonRPCAction": {
                        "method": "donothing",
                        "parameters": ["", ],
                        "dontHideAfterAction": True
                    }
                }