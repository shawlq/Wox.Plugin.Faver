# coding:utf-8
from wox import Wox
from log import logger
try:
    from faves import Faver
    from helper import Helper
except Exception as e:
    logger.exception("import exception:%s"%str(e))

class QueryString:
    @classmethod
    def Parse(cls, key):
        if not key:
            return None, None
        return key.split(" ", 1) if (" " in key) else (key, None)



class Main(Wox):
    def __init__(self):
        self.__cmds = ['tag', 'untag']
        super().__init__()
        

    def query(self, inputs):
        logger.debug("query, inputs:%s", inputs)
        try:
            if not inputs:
                return Helper.ShowHelp()

            cmd, para = QueryString.Parse(inputs)
            if cmd in self.__cmds:
                return getattr(self, "%s"%cmd)(para)

            return self.showlist(inputs)
        except Exception as e:
            logger.exception("query exception:%s"%str(e))

    def tag(self, para):
        try:
            para = "" if para is None else para
            args = para.split(" ")
            if (len(args) < 2):
                return [Helper.HELP_NONE("at least one label and one url")]
            return [Helper.ShowList("tag %s for url:%s"%(" & ".join(args[:-1]), args[-1]), "click for comfirm", para, "clickfortag")]
        except Exception as e:
            logger.exception("[main] tag except:%s", str(e))

    def untag(self, para):
        if not para:
            return [Helper.HELP_NONE("at least one label")]
        def Result(labels, url):
            return Helper.ShowList(labels.replace(" ", " & "), url, " ".join([labels, url]), "clickforuntag")

        return self.listin(para, Result)

    def showlist(self, para = None):
        def Result(labels, url):
            return Helper.ShowList(labels.replace(" ", " & "), url, url, "clickforurl")

        return self.listin(para, Result)

    def listin(self, para, Result):
        try:
            results = []
            sucess, msg, found, no_mores = Faver.List(para)
            if not sucess:
                return [Helper.HELP_NONE(msg)]

            for labels, urls in found:
                logger.debug("listin:%s", labels)
                for url in urls:
                    results.append(Result(labels, url))

            for labels, msg in no_mores:
                results.append(Helper.ShowList(labels.replace(" ", " & "), msg, "", "donothing"))

            return results if len(results) != 0 else [Helper.HELP_NONE("Nothing Found for '%s'."%para.replace(" ", " & "))]
        except Exception as e:
            logger.exception("[main] listall except:%s", str(e))
            return []

    def clickforurl(self, para):
        try:
            Faver.Click(para)
        except Exception as e:
            logger.exception("[main] click except:%s", str(e))

    def clickforlabel(self, para):
        return self.listall(para)

    def clickfortag(self, para):
        try:
            para = "" if para is None else para
            args = para.split(" ")
            if (len(args) < 2):
                return [Helper.HELP_NONE("at least one label and one url")]
            Faver.Tag(args)
        except Exception as e:
            logger.exception("[main] tag except:%s", str(e))

    def clickforuntag(self, para):
        try:
            Faver.Untag(para)
        except Exception as e:
            logger.exception("[main] click for untag except:%s", str(e))

    def donothing(self, para):
    	pass      

if __name__ == "__main__":
    Main()
