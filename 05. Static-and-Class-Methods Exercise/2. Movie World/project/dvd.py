class DVD:

    def __init__(self, name: str, dvd_id: int, creation_year: int, creation_month: int, age_restriction: int):
        self.name = name
        self.id = dvd_id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @staticmethod
    def from_date(self, dvd_id: int, name: str, date: str, age_restriction: int):
        self.id = dvd_id
        self.name = name
        self.date = date
        self.age_restriction = age_restriction

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year})" \
               f" has age restriction {self.age_restriction}. Status: {self.is_rented}"
        
        