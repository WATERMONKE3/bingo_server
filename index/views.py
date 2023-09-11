from django.shortcuts import render
from index.models import *
import csv
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.
def home(request):
    return render(request, 'lp.html')

def bingo(request):
    return render(request, 'bingo.html')

def raffle(request):
    raffle_entries = RaffleEntry.objects.all()
    context = {
        'raffle_entries': raffle_entries
    }
    return render(request, 'raffle.html')

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
