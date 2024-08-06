import gradio as gr
from traveldesk import TravelDesk

# Initialize TravelDesk
desk = TravelDesk()

def add_trip(vehicle_number, seating_capacity, pick_up_location, drop_location, departure_time):
    try:
        desk.add_trip(vehicle_number, int(seating_capacity), pick_up_location, drop_location, int(departure_time))
        return f"Trip added successfully: {vehicle_number} from {pick_up_location} to {drop_location} at {departure_time}"
    except Exception as e:
        return f"Error adding trip: {str(e)}"

def show_trips(pick_up_location, after_time, before_time):
    try:
        trips = desk.show_trips(pick_up_location, int(after_time), int(before_time))
        if not trips:
            return "No trips found for the given criteria."
        return "\n".join([f"Trip: {t.get_vehicle().get_vehicle_number()} to {t.get_drop_location()} at {t.get_departure_time()}" for t in trips])
    except Exception as e:
        return f"Error showing trips: {str(e)}"

def book_trip(pick_up_location, drop_location, vehicle_number, departure_time):
    try:
        trip = desk.book_trip(pick_up_location, drop_location, vehicle_number, int(departure_time))
        if trip:
            return f"Trip booked successfully: {vehicle_number} from {pick_up_location} to {drop_location} at {departure_time}"
        else:
            return "Booking failed. Trip not found or fully booked."
    except Exception as e:
        return f"Error booking trip: {str(e)}"

# Create Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Travel Desk Application")
    
    with gr.Tab("Add Trip"):
        vehicle_number = gr.Textbox(label="Vehicle Number")
        seating_capacity = gr.Number(label="Seating Capacity")
        pick_up_location = gr.Textbox(label="Pick-up Location")
        drop_location = gr.Textbox(label="Drop Location")
        departure_time = gr.Number(label="Departure Time")
        add_button = gr.Button("Add Trip")
        add_output = gr.Textbox(label="Result")
        add_button.click(add_trip, inputs=[vehicle_number, seating_capacity, pick_up_location, drop_location, departure_time], outputs=add_output)

    with gr.Tab("Show Trips"):
        show_pick_up = gr.Textbox(label="Pick-up Location")
        after_time = gr.Number(label="After Time")
        before_time = gr.Number(label="Before Time")
        show_button = gr.Button("Show Trips")
        show_output = gr.Textbox(label="Trips")
        show_button.click(show_trips, inputs=[show_pick_up, after_time, before_time], outputs=show_output)

    with gr.Tab("Book Trip"):
        book_pick_up = gr.Textbox(label="Pick-up Location")
        book_drop = gr.Textbox(label="Drop Location")
        book_vehicle = gr.Textbox(label="Vehicle Number")
        book_time = gr.Number(label="Departure Time")
        book_button = gr.Button("Book Trip")
        book_output = gr.Textbox(label="Booking Result")
        book_button.click(book_trip, inputs=[book_pick_up, book_drop, book_vehicle, book_time], outputs=book_output)

if __name__ == "__main__":
    demo.launch()