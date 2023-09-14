from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.student_loan import StudentLoan
from project.loans.mortgage_loan import MortgageLoan


class BankApp:

    VALID_LOANS = {
        "StudentLoan": StudentLoan,
        "MortgageLoan": MortgageLoan,
    }

    VALID_CLIENTS = {
        "Student": Student,
        "Adult": Adult,
    }

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []
        self.not_granted = []

    def get_client_by_id(self, client_id):
        client = [c for c in self.clients if c.client_id == client_id]
        if client:
            return client[0]
        return None

    def get_client_by_type(self, client_type):
        client = [c.client_id for c in self.loans if self.VALID_CLIENTS == client_type]
        if client:
            return client[0]
        return None

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_LOANS:
            raise Exception("Invalid loan type!")
        loan = self.VALID_LOANS[loan_type]
        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):

        if client_type not in self.VALID_CLIENTS:
            raise Exception("Invalid client type!")

        if len(self.clients) == self.capacity:
            return "Not enough bank capacity."

        client = self.VALID_CLIENTS[client_type](client_name, client_id, income)
        self.clients.append(client)

        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):

        client = [c.client_id for c in self.clients if c.client_id == client_id][0]
        client_type = self.get_client_by_type(loan_type)

        if not client_type:
            raise Exception("Inappropriate loan type!")

        self.loans.remove(client_type)
        self.VALID_LOANS[loan_type].append(client)

    def remove_client(self, client_id: str):

        client = self.get_client_by_id(client_id)

        if not client:
            raise Exception("No such client!")

        if client in self.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        pass
        # client = [c.increase_interest_rate for c in self.loans]
        # return f"Successfully changed {len(client)} loans."

    def increase_clients_interest(self, min_rate: float):
        pass
        # client = [c for c in self.clients if c.interest < min_rate]
        # return f"Number of clients affected: {len(client)}."

    def get_statistics(self):
        result = ""
        result += f"Active Clients: {len(self.clients)}\n"
        result += f"Total Income: {sum([c.income for c in self.clients]):.2f}\n"
        result += f"Granted Loans: {len([c for c in self.loans])}, Total Sum: {sum([c.amount for c in self.loans]):.2f}\n"
        result += f"Available Loans: {len([c for c in self.not_granted])}, Total Sum: {sum([c for c in self.not_granted]):.2f}\n"
        result += f"Average Client Interest Rate: {len(self.clients)}"

        return result

bank = BankApp(3)

print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))
print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))


print(bank.add_client('Student', 'Peter Simmons', '1234567891', 500))
print(bank.add_client('Adult', 'Samantha Peters', '1234567000', 1000))
print(bank.add_client('Student', 'Simon Mann', '1234567999', 700))
print(bank.add_client('Student', 'Tammy Smith', '1234567555', 700))

print(bank.grant_loan('StudentLoan', '1234567891'))
print(bank.grant_loan('MortgageLoan', '1234567000'))
print(bank.grant_loan('MortgageLoan', '1234567000'))

print(bank.remove_client('1234567999'))

print(bank.increase_loan_interest('StudentLoan'))
print(bank.increase_loan_interest('MortgageLoan'))

print(bank.increase_clients_interest(1.2))
print(bank.increase_clients_interest(3.5))

print(bank.get_statistics())
