from django.shortcuts import render
from index.models import *
import csv
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.
def home(request):
    return render(request, 'lp.html')

def save_winner(request):
    if request.method == 'POST':
        winner_number = request.POST.get('winner_number')
        if winner_number:
            if RaffleEntry.objects.filter(ticket_number=winner_number).exists():
                raffle_entry = RaffleEntry.objects.get(ticket_number=winner_number)
                if not Winner.objects.filter(ticket_number=winner_number).exists():
                    winner = Winner(
                        ticket_number=raffle_entry.ticket_number,
                        name=raffle_entry.name,
                        phone_number=raffle_entry.phone_number,
                        address=raffle_entry.address
                    )
                    request.session['winner_number'] = winner_number
                    winner.save()
                    raffle_entry.delete()

    return redirect('raffle')
def raffle(request):
    winner_number = request.session.get('winner_number', 0)
    raffle_entries = RaffleEntry.objects.all()
    ticket_numbers = [raffle_entry.ticket_number for raffle_entry in raffle_entries]
    context = {
        'winner_number': winner_number,
        'ticket_numbers': ticket_numbers,
    }
    return render(request, 'raffle.html', context)

def import_raffle_entries(request):
    # Path to your CSV file
    csv_file_path = 'C:/Users/licaros.jazfer/Documents/GitHub/bingo_server/dummy_data.csv'

    try:
        # Open and read the CSV file
        with open(csv_file_path, 'r') as csv_file:
            csv_data = csv.reader(csv_file)
            next(csv_data, None)  # Skip the header row if it exists

            for row in csv_data:
                ticket_number, name, phone_number, address = row
                
                # Check if an entry with the same ticket number already exists
                if not RaffleEntry.objects.filter(ticket_number=ticket_number).exists():
                    raffle_entry = RaffleEntry(
                        ticket_number=ticket_number,
                        name=name,
                        phone_number=phone_number,
                        address=address
                    )
                    raffle_entry.save()

        return redirect('home')
    except FileNotFoundError:
        print("File not found")
        # Handle the case where the CSV file does not exist
        return redirect('home')