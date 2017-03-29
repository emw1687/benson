import flask
import pickle
import numpy as np
import os


#-----MODEL-----#
#load original data
with open('../../../../04_fletcher/data/processed/s_listings.pkl', 'rb') as picklefile:
    s_listings = pickle.load(picklefile)

#load model files
with open('../../../../04_fletcher/models/nmf_demo.pkl', 'rb') as picklefile:
    nmf, nmf_vectorizer, nmf_doc_topic, nmf_topics = pickle.load(picklefile)


#-----URLS AND WEB PAGES-----#
#initialize flask app
app = flask.Flask(__name__)
app.secret_key = os.urandom(24).encode('hex')

# Homepage
@app.route('/')
def viz_page():
    """
    Homepage: serve our visualization page, awesome.html
    """
    return flask.render_template("nmf_demo.html")

@app.route('/', methods=['POST'])
def match_me():
    '''
    description: string, description of traveller
    level: ['same', 'mix', 'opposite']
            same : find host similar to traveller
            mix : find host equally similar and dissimilar to traveller
            opposite : find host dissimilar to traveller
    '''
    #read data that came with post as dict
    desc = [str(flask.request.form['text'])]
    level = flask.request.form['range']

    levels = {'1': 0,
              '0.5': int(round(np.median(range(len(nmf_topics))), 0)),
              '0': len(nmf_topics)-1}

    description_vec = nmf_vectorizer.transform(desc)

    topic_index = np.argsort(nmf.transform(description_vec))[0][::-1][levels[level]]

    cluster =  nmf_topics[topic_index].title()
    flask.flash(str(cluster))

    host_index = np.argsort(nmf_doc_topic[:,topic_index])[::-1][0]
    flask.flash(s_listings['host_about'].iloc[host_index])
    return flask.redirect(flask.url_for('viz_page'))

#-----RUN WEB APP SERVER-----#
#debug
if __name__ == '__main__':
    app.debug = True
    app.run()

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
