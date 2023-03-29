#!/usr/bin/python

# Languages Transformer
class TransformLanguages:
    def __init__(self, conf):
        self.langs = conf["languages"]
        self.notAsTarget = conf.get("notAsTarget", [])

    @property
    def languages(self):
        matrix = {}
        englishVariants = ['en', 'simple']
        for i in range(len(self.langs)):
            lang = self.langs[i]
            matrix[lang] = list(filter(lambda l: False if (englishVariants.__contains__(l) and englishVariants.__contains__(lang)) else (l != lang and l not in self.notAsTarget), self.langs))
        return matrix
