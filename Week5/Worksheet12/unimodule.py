class UniModule:
    def __init__(self, code, name, year, credit,
                 grade=0, PFP=False, discovery=False):
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
        message = f"{self.code}:" \
                  f"{self.name}:" \
                  f"Y{self.year}:" \
                  f"{self.credit}CR:" \
                  f"{self.grade}GRD:" \
                  f"{nPFP}PFP:" \
                  f"{ndiscovery}Disc"
        print(message)


class Transcript:
    def __init__(self):
        self.modules = []

    def add_module(self, item):
        for module in self.modules:
            if module == item:
                raise ValueError("module already exists!")
        if not isinstance(item, UniModule):
            raise ValueError("expected item be an instance of UniModule.")
        self.modules.append(item)

    def print_transcript(self):
        for module in self.modules:
            module.display_details()
