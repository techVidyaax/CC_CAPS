from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample bus and route data
buses = [
    {'id': 1, 'name': 'SETC'},
    {'id': 2, 'name': 'RedBus'},
]

routes = [
    {'id': 1, 'start': 'Coimbatore', 'end': 'Salem', 'duration': '3 hours'},
    {'id': 2, 'start': 'Chennai', 'end': 'Trichy', 'duration': '4 hours'},
]

tickets = []

@app.route('/')
def home():
    success_message = request.args.get('success')
    return render_template('home.html', buses=buses, routes=routes, success_message=success_message)

@app.route('/book_ticket/<int:bus_id>/<int:route_id>', methods=['GET', 'POST'])
def book_ticket(bus_id, route_id):
    bus = next(b for b in buses if b['id'] == bus_id)
    route = next(r for r in routes if r['id'] == route_id)

    if request.method == 'POST':
        passenger_name = request.form['passenger_name']
        seat_number = request.form['seat_number']
        ticket = {
            'bus': bus['name'],
            'route': f"{route['start']} to {route['end']}",
            'passenger': passenger_name,
            'seat': seat_number,
        }
        tickets.append(ticket)
        
        # Redirect to homepage with success message
        return redirect(url_for('home', success="Your ticket has been successfully booked ✅"))

    return render_template('book_ticket.html', bus=bus, route=route)

@app.route('/view_bookings')
def view_bookings():
    return render_template('view_bookings.html', tickets=tickets)

@app.route('/ticket_booked')
def ticket_booked():
    return render_template('ticket_booked.html', tickets=tickets)

if __name__ == "__main__":
    app.run(debug=True)
