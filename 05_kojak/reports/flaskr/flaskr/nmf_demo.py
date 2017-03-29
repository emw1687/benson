import flask
import pickle
import numpy as np

#load original data
with open('../../../../04_fletcher/data/processed/s_listings.pkl', 'rb') as picklefile:
    s_listings = pickle.load(picklefile)

#load model files
with open('../../../../04_fletcher/models/nmf_demo.pkl', 'rb') as picklefile:
    nmf, nmf_vectorizer, nmf_doc_topic, nmf_topics = pickle.load(picklefile)

#initialize flask app
app = flask.Flask(__name__)

#debug
if __name__ == '__main__':
    app.debug = True
    app.run()

@app.route('/')
def hello():
    return 'let\'s match!'

@app.route('/match_me', methods=['POST'])
def match_me():
    '''
    description: string, description of traveller
    level: ['same', 'mix', 'opposite']
            same : find host similar to traveller
            mix : find host equally similar and dissimilar to traveller
            opposite : find host dissimilar to traveller
    '''
    #read data that came with post as dict
    data = flask.request.json

    levels = {'same': 0,
              'mix': int(round(np.median(range(len(nmf_topics))), 0)),
              'opposite': len(nmf_topics)-1}

    desc = data['me']
    level = data['level']

    description_vec = nmf_vectorizer.transform(desc)

    topic_index = np.argsort(nmf.transform(description_vec))[0][::-1][levels[level]]
    #topic_index = np.argsort(nmf.transform(description_vec))[0][::-1][0]
    cluster =  nmf_topics[topic_index].title()
    #return flask.jsonify(cluster)
    return str(cluster)

    #host_index = np.argsort(nmf_doc_topic[:,topic_index])[::-1][0]
    #print s_listings['host_about'].iloc[host_index]

#shutdown server after use
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'
