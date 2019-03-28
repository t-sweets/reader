from flask import Flask, request, jsonify
from escpos import printer
from receipt import ReceiptManager
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

device = printer.Serial('/dev/tty.SM1-21-SerialPortDevB')
printer = ReceiptManager(device)


@app.route('/receipt', methods=['POST'])
def post_json():
    data = request.get_json()

    printer.header(
        icon=data["icon"],
        date=data["date"]
    )
    for item in data['items']:
        printer.item(item["name"], item["unit"], item["pcs"], item["price"])

    if data["payment_method"] is "cash":
        printer.footer(
            data["total_price"],
            cash=data["cash"],
            change=data["change"])
    else:
        printer.footer(
            data["total_price"],
            payment_method=data["payment_method"],
            customer_id=data["customer_id"],
            balance=data["balance"]
        )
    return jsonify(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3001)
