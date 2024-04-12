from flask import Flask, request, jsonify
from processor.control_unit.model import Model

app = Flask(__name__)
model = Model()

@app.route('/inference', methods=['POST'])
def process_prompt():
    data = request.json  
    prompt = data.get('prompt', 'No prompt provided')

    res=model.inference(prompt=prompt)
    return jsonify({'message': f'{res}'})

if __name__ == '__main__':
    app.run(debug=True)
