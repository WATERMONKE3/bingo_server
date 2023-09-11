from django.shortcuts import render
from index.models import *
import csv
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.
def home(request):
    return render(request, 'home.html')

def bingo(request):
    return render(request, 'bingo.html')

def save_bingo_number (request):
    if request.method == 'POST' and 'number' in request.POST:
        number = int(request.POST['number'])

        # Create a new BingoCard instance and set the appropriate column
        bingo_card = BingoCard()

        if 1 <= number <= 15:
            bingo_card.b_column = str(number)
        elif 16 <= number <= 30:
            bingo_card.i_column = str(number)
        elif 31 <= number <= 45:
            bingo_card.n_column = str(number)
        elif 46 <= number <= 60:
            bingo_card.g_column = str(number)
        elif 61 <= number <= 75:
            bingo_card.o_column = str(number)

    bingo_card.save()  # Save the BingoCard instance
    print("Here are you?")
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
