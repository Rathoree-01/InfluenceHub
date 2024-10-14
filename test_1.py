from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    item = {
        'name': 'Sample Name',
        'description': 'Sample Description',
        'start': 'Sample Start',
        'end': 'Sample End',
        'visibility': 'Sample Visibility',
        'goals': 'Sample Goals'
    }
    return render_template('index.html', item=item)

@app.route('/spons_2', methods=['GET'])
def spons_2():
    name = request.args.get('name')
    description = request.args.get('description')
    start = request.args.get('start')
    end = request.args.get('end')
    visibility = request.args.get('visibility')
    goals = request.args.get('goals')

    # Here, you can handle the data, for example, save it to the database

    return f"Received: {name}, {description}, {start}, {end}, {visibility}, {goals}"

if __name__ == '__main__':
    app.run(debug=True)

 const url = `/spons_2?name=${encodeURIComponent(name)}`;
        
        // Redirect to the URL
        console.log(url);
        window.location.href = url;