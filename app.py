from flask import Flask, request

app = Flask(__name__)

# Student results data
results = {
    "dhanush": {"marks": 85, "grade": "A"},
    "ravi":    {"marks": 72, "grade": "B"},
    "priya":   {"marks": 91, "grade": "A+"},
    "kumar":   {"marks": 45, "grade": "F"},
    "sneha":   {"marks": 60, "grade": "C"},
}

@app.route('/')
def home():
    return """
    <h1>Student Result Checker</h1>
    <p>Enter student name in URL:</p>
    <p><b>/result/dhanush</b></p>
    """

@app.route('/result/<name>')
def result(name):
    name = name.lower()
    if name in results:
        data = results[name]
        status = "PASS" if data["marks"] >= 50 else "FAIL"
        return f"""
        <h1>Result for {name.title()}</h1>
        <p>Marks: {data['marks']}</p>
        <p>Grade: {data['grade']}</p>
        <p>Status: {status}</p>
        """
    else:
        return f"<h1>Student '{name}' not found!</h1>", 404

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
