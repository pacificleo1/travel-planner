from fpdf import FPDF

def generate_pdf(itinerary):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, f"Your Schedule for {itinerary['days']} days in {itinerary['destination']}", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", size=12)
    for day in range(itinerary['days']):
        pdf.cell(0, 10, f"Day {day + 1}", ln=True, style="B")
        pdf.cell(0, 10, f"Breakfast: {itinerary['restaurants'][day]['name']}", ln=True)
        pdf.cell(0, 10, f"Sight 1: {itinerary['sights'][day]['name']}", ln=True)
        pdf.cell(0, 10, f"Lunch: {itinerary['restaurants'][day+1]['name']}", ln=True)
        pdf.cell(0, 10, f"Shopping: {itinerary['markets'][0]['name']}", ln=True)
        pdf.ln(10)

    pdf_path = "trip_schedule.pdf"
    pdf.output(pdf_path)
    return pdf_path
