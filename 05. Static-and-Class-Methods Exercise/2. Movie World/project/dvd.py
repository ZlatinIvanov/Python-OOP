import datetime


class DVD:

    def __init__(self, name: str, dvd_id: int, creation_year: int, creation_month: int, age_restriction: int):
        self.name = name
        self.id = dvd_id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        # mapper = {1: "January", 2: "February", 3: "March", 4: "April"}
        day, month_number_as_string, year = date.split(".")
        # month = mapper[int(month_number)]
        monthinteger = int(month_number_as_string)
        month = datetime.date(1900, monthinteger, 1).strftime('%B')

        return cls(name, id, int(year), month, age_restriction)

    def __repr__(self):
        rented_status = 'rented' if self.is_rented else 'not rented'
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year})" \
               f" has age restriction {self.age_restriction}. Status: {rented_status}"
        
        