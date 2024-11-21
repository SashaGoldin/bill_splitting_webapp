from flask.views import MethodView
from wtforms import Form
from flatmates_bill.flat import Bill, Flatmate
from flatmates_bill.reports import PdfReport, FileSharer
from flask import Flask, render_template

app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template("index.html")


class BillFormPage(MethodView):
    pass


class ResultsPage(MethodView):
    pass


class BillForm(Form):
    pass


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill_form_page'))

app.run(debug=True)

# amount = float(input("Hey user, enter the bill amount: "))
# period = input("What is the bill period? E.g. December 2020: ")
#
# name1 = input("What is your name? ")
# days_in_house1 = int(input(f"How many days did {name1} stay in the house during the bill period? "))
#
# name2 = input("What is the name of the other flatmate? ")
# days_in_house2 = int(input(f"How many days did {name2} stay in the house during the bill period? "))
#
# the_bill = Bill(amount, period)
# flatmate1 = Flatmate(name1, days_in_house1)
# flatmate2 = Flatmate(name2, days_in_house2)
#
# print(f"{flatmate1.name} pays: ", flatmate1.pays(the_bill, flatmate2))
# print(f"{flatmate2.name} pays: ", flatmate2.pays(the_bill, flatmate1))
#
# pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
# pdf_report.generate(flatmate1, flatmate2, the_bill)
#
# file_sharer = FileSharer(filepath=pdf_report.filename)
# print(file_sharer.share())
