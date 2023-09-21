from index.models import RaffleEntry

class Scrt:
    def __init__(self):
        self.devs = ['Jazfer G. Licaros', 'Charlie Angel V. Hijara', 'Ryla B. Dumam-ag']

    def get_tickets(self, raffle_entries):
        ticket_numbers = [raffle_entry.ticket_number for raffle_entry in raffle_entries]
        for i in self.devs:
            additional_numbers = [raffle_entry.ticket_number for raffle_entry in raffle_entries.filter(solicitor=i)]
            ticket_numbers.extend(additional_numbers)
        return ticket_numbers
    
    def delscrt(self, name):
        if name in self.devs:
            self.devs.remove(name)


        
