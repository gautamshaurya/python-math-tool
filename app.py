from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
    try:
        a = request.args.get('a', type=float)
        b = request.args.get('b', type=float)

        if a is None or b is None:
            return jsonify({"error": "Please provide both 'a' and 'b' in query parameters"}), 400

        return jsonify({
            "a": a,
            "b": b,
            "sum": a + b
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
