import json

class Data:
    DATA_PATH = r"./DB/db.json"
    @classmethod
    def Save(cls, d):
        with open (cls.DATA_PATH, "w") as f:
            f.write(json.dumps(d))

    @classmethod
    def Load(cls):
        with open (cls.DATA_PATH, "r") as f:
            infos = f.read()
            return json.loads(infos) if infos else {}

class Info:

    SEG = "|"
    DEFAULT = "*"

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
    def Save(cls, label, sn, data):
        # {label : {sn : url} }
        infos = Data.Load()
        if label not in infos:
            infos[label] = {}
        if sn not in infos[label]:
            infos[label][sn] = []
        infos[label][sn].append(data)
        Data.Save(infos)

    @classmethod
    def Get(cls, label, sn):
        label = label if label is not '*' else ''
        results = []
        for lbl, sn_dict in Data.Load().items():
            if label and label not in lbl:
                continue
            for snkey, datas in sn_dict.items():
                if sn and sn not in snkey:
                    continue

                for data in datas:
                    results.append([lbl, snkey, data])
        return results



