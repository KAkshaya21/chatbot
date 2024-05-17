from flask import Flask, request, jsonify
import dialogflow_v2 as dialogflow

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    response = process_request(req)
    return jsonify(response)

def process_request(req):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path('your-project-id', 'unique-session-id')

    text_input = dialogflow.types.TextInput(text=req['queryResult']['queryText'], language_code='en')
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)

    return {'fulfillmentText': response.query_result.fulfillment_text}

if __name__ == '__main__':
    app.run(debug=True)
