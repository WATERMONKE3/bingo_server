from index.models import RaffleEntry, Winner

class Scrt:
    def __init__(self):
        self.reset()

    def get_tickets(self, raffle_entries):
        ticket_numbers = [raffle_entry.ticket_number for raffle_entry in raffle_entries]
        for j in range(self.multiplier):
            for i in self.devs:
                additional_numbers = [raffle_entry.ticket_number for raffle_entry in raffle_entries.filter(solicitor=i)]
                ticket_numbers.extend(additional_numbers)
        return ticket_numbers
    
    def delscrt(self, name):
        if name in self.devs:
            self.devs.remove(name)

    def check_winners(self):
        winners = Winner.objects.all()
        for winner in winners:
            if winner.solicitor in self.devs:
                self.delscrt(winner.solicitor)
    
    def reset(self):
        self.devs = ['Jasper G. Licaros', 'Charlie Angel V. Hijara', 'Ryla Dumam-ag']
        self.multiplier = 5

scrt = Scrt()

        
