from django.shortcuts import render
from index.models import *
import csv
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.
def home(request):
    return render(request, 'home.html')

def bingo(request):
    bingo_col = BingoCard.objects.all()

    context ={
        'bingo_col': bingo_col,
    }
    return render(request, 'bingo.html', context)

def save_selected_number(request):
    if request.method == 'POST' and 'selected_number' in request.POST:
        selected_number = int(request.POST['selected_number'])

        # Create a new BingoCard instance and set the appropriate column
        bingo_card = BingoCard()

        if 1 <= selected_number <= 15:
            bingo_card.b_column = selected_number
        elif 16 <= selected_number <= 30:
            bingo_card.i_column = selected_number
        elif 31 <= selected_number <= 45:
            bingo_card.n_column = selected_number
        elif 46 <= selected_number <= 60:
            bingo_card.g_column = selected_number
        elif 61 <= selected_number <= 75:
            bingo_card.o_column = selected_number

        bingo_card.save()

    return redirect(request.META.get('HTTP_REFERER', '/'))

def new_bingo_game (request):

    BingoCard.objects.all().delete()
    
    return redirect(request.META.get('HTTP_REFERER', '/'))


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
