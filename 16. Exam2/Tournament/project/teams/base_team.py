from abc import ABC, abstractmethod
from math import floor
from typing import List

from project.equipment.base_equipment import BaseEquipment


class BaseTeam(ABC):

    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins = 0
        self.equipment: List[BaseEquipment] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Team name cannot be empty!")
        self.__name = value
        
    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")
        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")
        self.__advantage = value

    @abstractmethod
    def win(self):
        ...

    def get_statistics(self):
        equipment_price = 0
        equipment = [e for e in self.equipment]
        avg_team_protection = 0
        for price in equipment:
            equipment_price += price.price
            avg_team_protection += price.protection
        return f"Name: {self.name}\n" \
                 f"Country: {self.country}\n" \
                 f"Advantage: {self.advantage} points\n" \
                 f"Budget: {self.budget:.2f}EUR\n" \
                 f"Wins: {self.wins}\n" \
                 f"Total Equipment Price: {equipment_price:.2f}\n" \
                 f"Average Protection: {int(floor(avg_team_protection))}\n"




