reservations = {}

def make_reservation():
    name = input('Enter your name: ')
    date = input('Enter the reservation date (dd/mm/yyyy): ')

    if date not in reservations:
        reservations[date] = []

    reservations[date].append(name)
    print('Reservation made successfully.')

def show_reservations():
    date = input('Enter the date to view reservations (dd/mm/yyyy): ')

    if date in reservations:
        print('Reservations for', date + ':')
        for name in reservations[date]:
            print(name)
    else:
        print('No reservations for the specified date.')

make_reservation()
show_reservations()