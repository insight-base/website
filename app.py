from flask import Flask, render_template

app = Flask(__name__)

# Route for the landing page
@app.route('/')
def index():
    # You can pass dynamic data here, like latest project stats
    services = [
        {"title": "Descriptive", "desc": "Understand what happened with clean dashboards."},
        {"title": "Diagnostic", "desc": "Learn why it happened using root-cause analysis."},
        {"title": "Predictive", "desc": "Anticipate what is likely to happen with ML models."},
        {"title": "Prescriptive", "desc": "Decide what to do next with optimization."}
    ]
    return render_template('index.html', services=services)

if __name__ == '__main__':
    app.run(debug=True)
