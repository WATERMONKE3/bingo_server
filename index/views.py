from django.shortcuts import render
from index.models import *
import csv
from django.contrib import messages
from django.shortcuts import redirect
import random
import time
from django.http import JsonResponse
# Create your views here.
def home(request):
    return render(request, 'lp.html')


def bingo(request):
    # Get the selected_numbers_array from the session or initialize it as an empty list
    selected_numbers_array = request.session.get('selected_numbers_array', [])
    selected_number = request.session.get('selected_number', 0)

    # bingo_col = BingoCard.objects.all()
    numbers = list(range(1, 76))

    # Remove selected numbers from the numbers list
    numbers = [num for num in numbers if num not in selected_numbers_array]

    if selected_number not in selected_numbers_array:
        selected_numbers_array.append(selected_number)
        request.session['selected_numbers_array'] = selected_numbers_array


    context = {
        'bingo_col': bingo_col,
        'selected_number': selected_number,
        'numbers': numbers,
        'rows': rows,
    }

    return render(request, 'bingo.html', context)



def save_selected_number(request):
    if request.method == 'POST' and 'selected_number' in request.POST:
        selected_number = int(request.POST['selected_number'])

        # Store selected number in session
        request.session['selected_number'] = selected_number

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

    return redirect('bingo')

def new_bingo_game(request):
    if 'selected_number' in request.session:
        del request.session['selected_number']

    if 'selected_numbers_array' in request.session:
        del request.session['selected_numbers_array']

    BingoCard.objects.all().delete()
    
    return redirect(request.META.get('HTTP_REFERER', '/'))


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
    context = {}
    winner_number = request.session.get('winner_number', 0)
    if winner_number:
        current_winner = Winner.objects.get(ticket_number=winner_number)
        winners = Winner.objects.all().order_by('date')
        context.update({'winners': winners, 'current_winner': current_winner})
    raffle_entries = RaffleEntry.objects.all()
    ticket_numbers = [raffle_entry.ticket_number for raffle_entry in raffle_entries]
    context.update({'ticket_numbers': ticket_numbers, 'winner_number': winner_number})
    
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
                ticket_number, name, phone_number, address, solicitor = row
                
                # Check if an entry with the same ticket number already exists
                if not RaffleEntry.objects.filter(ticket_number=ticket_number).exists():
                    raffle_entry = RaffleEntry(
                        ticket_number=ticket_number,
                        name=name,
                        phone_number=phone_number,
                        address=address,
                        solicitor=solicitor
                    )
                    raffle_entry.save()
        request.session['winner_number'] = 0
        return redirect('home')
    except FileNotFoundError:
        print("File not found")
        # Handle the case where the CSV file does not exist
        return redirect('home')
    
