from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>DevOps Docker Task</title>
        </head>
        <body>
            <h1>DevOps Docker Application</h1>

            <h2>Student Information</h2>

            <p><strong>Student Name:</strong> Neha Maqbool </p>
            <p><strong>Student ID:</strong> Juw 32797 </p>
            <p><strong>Course:</strong> DevOps</p>

            <h2>This application is running inside a Docker container.</h2>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)