"""Module Value Objects."""
from flunt.notifiable import Notifiable
from flunt.contract import Contract


class Name(Notifiable):
    """Class Value Object Name."""

    def __init__(self, first_name, last_name):
        """Found 'Constructor'."""
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name

        self.contract = (
            Contract()
            .requires(self.first_name, 'first name')
            .requires(self.last_name, 'last name')
            .has_min_len(
                value=self.first_name,
                minimum=3,
                field='first_name',
                message='invalid first name'
            )
            .has_min_len(
                value=self.last_name,
                minimum=3,
                field='last_name',
                message='invalid last name'
            )
        )

        self.add_notifications_of_contract(self.contract)


nome = Name('Emerson', 'Delatorre')
if not nome.is_valid():
    for notification in nome.get_notifications():
        print(notification)
