from __init__ import create_app

# Call the app factory
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
