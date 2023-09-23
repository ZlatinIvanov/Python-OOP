from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:

    VALID_EQUIPMENTS = {
        "KneePad": KneePad,
        "ElbowPad": ElbowPad,
    }

    VALID_TEAMS = {
        "OutdoorTeam": OutdoorTeam,
        "IndoorTeam": IndoorTeam,
    }

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.isalnum() == "":
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        # equipment = [e for e in self.equipment if e.__class__.__name__ == equipment_type]

        if equipment_type not in self.VALID_EQUIPMENTS:
            raise Exception("Invalid equipment type!")

        equipment = self.VALID_EQUIPMENTS[equipment_type]()
        self.equipment.append(equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        # team_t = [t for t in self.teams if t.__class__.__name__ == team_type]
        # team_n = [t for t in self.teams if t.name == team_name]
        if team_type not in self.VALID_TEAMS:
            raise Exception("Invalid team type!")

        if self.capacity == len(self.teams):
            return "Not enough tournament capacity."

        team = self.VALID_TEAMS[team_type](team_name, country, advantage)
        self.teams.append(team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        team = [t for t in self.teams if t.name == team_name][0]
        equipment = [e for e in self.equipment if e.__class__.__name__ == equipment_type]

        if team.budget < equipment[0].price:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equipment[0])
        team.equipment.append(equipment[0])
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = [t for t in self.teams if t.name == team_name]

        if not team:
            raise Exception("No such team!")

        if team[0].wins > 0:
            raise Exception(f"The team has {team[0].wins} wins! Removal is impossible!")

        self.teams.remove(team[0])
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        team = [t.name for t in self.teams if t.equipment == equipment_type]
        equipment = [e for e in self.equipment if e.__class__.__name__ == equipment_type]
        number_of_changed_equipment = 0
        for e in equipment:
            if e not in team:
                e.increase_price()
                number_of_changed_equipment +=1

        return f"Successfully changed {number_of_changed_equipment}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        t1 = [t for t in self.teams if t.name == team_name1][0]
        t2 = [t for t in self.teams if t.name == team_name2][0]

        if t1.__class__.__name__ != t2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")
        avg_team_protection1 = 0
        equipment_price1 = 0
        equipment1 = [e for e in t1.equipment]
        for price in equipment1:
            equipment_price1 += price.price
            avg_team_protection1 += price.protection
        avg_team_protection2 = 0
        equipment_price2 = 0
        equipment2 = [e for e in t2.equipment]

        for price in equipment2:
            equipment_price2 += price.price
            avg_team_protection2 += price.protection

        t1_total = t1.advantage + equipment_price1
        t2_total = t2.advantage + equipment_price2

        if t1_total == t2_total:
            return "No winner in this game."
        elif t1_total > t2_total:
            t1.win()
            return f"The winner is {t1.name}."

        elif t2_total > t1_total:
            t2.win()
            return f"The winner is {t2.name}."

    def get_statistics(self):

        team = [t for t in self.teams]
        ordered = sorted(team, key=lambda x: -x.wins)
        result = []
        for s in ordered:
            result.append(s.get_statistics())
        return f"Tournament: {self.name}\n" \
               f"Number of Teams: {len(self.teams)}\n" \
               f"Teams:" \
               '\n'.join(str(x) for x in result)


t = Tournament('SoftUniada2023', 2)

print(t.add_equipment('KneePad'))
print(t.add_equipment('ElbowPad'))

print(t.add_team('OutdoorTeam', 'Levski', 'BG', 250))
print(t.add_team('OutdoorTeam', 'Spartak', 'BG', 250))
print(t.add_team('IndoorTeam', 'Dobrich', 'BG', 280))

print(t.sell_equipment('KneePad', 'Spartak'))

print(t.remove_team('Levski'))
print(t.add_team('OutdoorTeam', 'Lokomotiv', 'BG', 250))

print(t.increase_equipment_price('ElbowPad'))
print(t.increase_equipment_price('KneePad'))

print(t.play('Lokomotiv', 'Spartak'))

print(t.get_statistics())
