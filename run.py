# run.py
from app import create_app
from dash_app.app import initialize_dash_app

app = create_app()

# Initialize the Dash app
dash_app = initialize_dash_app(app)

@app.route('/dash/')
def serve_dash():
    return dash_app.index()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)









