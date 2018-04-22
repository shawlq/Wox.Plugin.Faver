# coding:utf-8
from wox import Wox
from faves import ToSee
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
    def query(self, key):
        cmd, para = QueryString.Parse(key)
        logger.debug("[main]----key----:%s, cmd:%s, para:%s.", key, cmd, para)

        if cmd in Helper.ACTIONS:
            #logger.debug("[main] query:%s, cmd:%s,para:%s.", key, cmd, para)
            return  [
                        Helper.Show(cmd, para)
                    ]

        results = self.listall(cmd, para)
        return results if len(results) != 0 else Helper.Show(cmd, para)

    def add(self, para):
        try:
            ToSee.Add(para)
        except Exception as e:
            logger.exception("[main] add except:%s", str(e))

    def erase(self, para):
        try:
            ToSee.Erase(para):
        except Exception as e:
            logger.exception("[main] erase except:%s", str(e))

    def delete(self, para):
        try:
            ToSee.Delete(para)
        except Exception as e:
            logger.exception("[main] delete except:%s", str(e))

    def listall(self, label = None, sn = None):
        try:
            results = []
            for lbl, s_n, data in ToSee.List(label, sn):
                results.append(Helper.ShowList(lbl, s_n, data, "click"))
            return results if results else Helper.Show(label, "")
        except Exception as e:
            logger.exception("[main] listall except:%s", str(e))
            return []

    def click(self, data):
        try:
            ToSee.Click(data)
        except Exception as e:
            logger.exception("[main] click except:%s", str(e))  

    def donothing(self, para):
    	pass      

if __name__ == "__main__":
    Main()
