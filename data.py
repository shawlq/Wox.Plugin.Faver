import json
from log import logger
import re

class Data:
    DATA_PATH = r"./DB/db.json"
    @classmethod
    def Save(cls, d):
        with open (cls.DATA_PATH, "w") as f:
            f.write(json.dumps(d))

    @classmethod
    def Load(cls):
        with open (cls.DATA_PATH, "r") as f:
            results = ''.join(f.read().split("\r\n"))
            logger.debug("Data.Load:%s", results)
            return results

    """
    @classmethod
    def Load(cls):
        results = {}
        with open (cls.DATA_PATH, "r") as f:
            for line in f:
                results.update(json.loads(line.strip()))
        return results
    """
    @classmethod
    def Append(cls, d):
        with open (cls.DATA_PATH, "a") as f:
            f.write(json.dumps(d))
class Info:

    SEG = "|"
    DEFAULT = "*"
    SN = "sn"
    DATA = "dat"

    @classmethod
    def Parse2Str(cls, para):
        try:
            l = [None, None, None]
            i = 0
            for p in para.split(cls.SEG):
                l[i] = p.strip()
                i += 1
            l[0] = l[0] if l[0] else cls.DEFAULT
            return l
        except Exception as e:
            logger.exception("Info.Parse2Str except:%s", str(e))
            return None, None, None

    @classmethod
    # label1|sn1|data1|0||label2|sn2|data2|5||
    def Save(cls, label, sn, data):
        info = cls.SEG.join([label, sn, data, '0', cls.SEG])
        logger.debug("Info.Save:%s", info)
        Data.Append(info)

    @classmethod
    def Get(cls, label, sn):
        infos = Data.Load()
        label = '' if label is '*' else label
        pattern = r"(\w*?%s\w*?\|\w*?%s\w*?\|.*?\|\d*)\|\|"%(label, sn)
        results = re.findall(pattern, infos, re.I)
        logger.debug("Info.Get:infos:%s, patt:%s, \nresults:%s", infos, pattern, results)
        return [x.split('|') for x in results]

    """
    @classmethod
    def Save(cls, label, sn, data):
        infos = Data.Load()
        if label not in infos:
            infos[label] = []
        infos[label].append({Info.SN:sn,Info.DATA:data})
        Data.Save(infos)

    @classmethod
    def Get(cls, label, sn):
        results = []
        for lbl, infos in Data.Load().items():
            if label and label is not '*' and label not in lbl:
                continue
            for info in infos:
                if sn and sn not in info[Info.SN]:
                    continue
                results.append([lbl, info[Info.SN], info[Info.DATA]])
        return results
    """


