class UniModule:
    def __init__(self, code, name, year, credit, grade = 0, PFP = False, discovery = False):
        self.code = code
        self.name = name
        self.year = year
        self.credit = credit
        self.grade = grade
        self.PFP = PFP
        self.discovery = discovery

    def display_details(self):
        nPFP = ""
        ndiscovery = ""
        if not self.PFP:
            nPFP = "N"
        if not self.discovery:
            ndiscovery = "N"
        message = f"{self.code}:{self.name}:Y{self.year}:{self.credit}CR:{self.grade}GRD:{nPFP}PFP:{ndiscovery}DISC"
        print (message)
COMP1011 = UniModule("COMP1011", "Intro to Prog.", 1, 10, discovery=True)
COMP1011.display_details()
