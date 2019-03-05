# coding:utf-8
from wox import Wox
from faves import Faver
from log import logger

from helper import Helper

class QueryString:
    @classmethod
    def Parse(cls, key):
        if not key:
            return None, None
        logger.debug("QueryString.Parse:key:%s, has_space:%s.", key.split(" ", 1), " " in key)
        return key.split(" ", 1) if (" " in key) else (key, None)



class Main(Wox):
    def query(self, inputs):
        cmd, para = QueryString.Parse(inputs)
        logger.debug("[main]----key----:%s, cmd:%s, para:%s.", key, cmd, para)
        return self.showcmd(cmd, para) if cmd in Helper.ACTIONS else self.listall(inputs)

    def tag(self, para):
        try:
            Faver.Tag(para)
        except Exception as e:
            logger.exception("[main] tag except:%s", str(e))

    def untag(self, para):
        try:
            results = []
            descript = " & ".join(para.split(" "))
            for url in Faver.List(para):
                results.append(Helper.ShowList(descript, url, " ".join(para,url), "clickforuntag"))
            return results if len(results) != 0 else [Helper.HELP_NONE(descript)]
        except Exception as e:
            logger.exception("[main] untag except:%s", str(e))
            return []

    def showcmd(self, cmd, para):
        try:
            results = []
            # TODO：label, sn, _ = Faver.Parse(para)
            for lbl, s_n, data in Faver.List(label, sn):
                results.append(Helper.ShowCmd(cmd, para, lbl, s_n, data))
            return results if len(results) != 0 else Helper.Show(cmd, para)
        except Exception as e:
            logger.exception("[main] showcmd except:%s", str(e))
            return []

    def listall(self, para = None):
        try:
            results = []
            descript = " & ".join(para.split(" "))
            for url in Faver.List(para):
                results.append(Helper.ShowList(descript, url, url, "clickforurl"))

            for labels_descript in Faver.FindLabels(para):
                results.append(Helper.ShowList(labels_descript, "", labels_descript, "clickforlabel"))

            return results if len(results) != 0 else [Helper.HELP_NONE(descript)]
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

    def clickforuntag(self, para):
        try:
            Faver.Untag(para)
        except Exception as e:
            logger.exception("[main] click for untag except:%s", str(e))
        

    def donothing(self, para):
    	pass      

if __name__ == "__main__":
    Main()
