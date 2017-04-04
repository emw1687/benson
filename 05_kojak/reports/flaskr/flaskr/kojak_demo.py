import flask
import pickle
import numpy as np
import os
import operator
from scipy.spatial.distance import cosine


#-----MODEL-----#
#load model files
with open ('../../../models/05_kojak_demo.pkl', 'rb') as picklefile:
    df_loc, df_doc_topics, nmf_topics = pickle.load(picklefile)

#-----URLS AND WEB PAGES-----#
#initialize flask app
app = flask.Flask(__name__)
app.secret_key = os.urandom(24).encode('hex')

# Homepage
@app.route('/')
def home_page():
    """
    Homepage: serve our input page, kojak_index.html
    """
    return flask.render_template("kojak_index.html")

# Homepage
@app.route('/results')
def results_page():
    """
    Results page: serve our visualization page, kojak_results.html
    """
    return flask.render_template("kojak_results.html", topic=topic)

@app.route('/', methods=['POST'])
def get_results():
    neighborhoods = df_loc['neighborhood'].apply(lambda u: u.encode('utf-8')).tolist()
    cities = df_loc['city'].tolist()
    topics = df_loc['topic'].tolist()
    zipped = zip(neighborhoods, cities, topics)

    #read data that came with post
    scores_list = []
    input_names = ['1_taco', '2_subway', '3_car', '4_museum', '5_farmer', \
                    '6_campus', '7_diverse', '8_art', '9_nightlife', '10_attractions', \
                    '11_golf', '12_outdoors', '13_streetcars', '14_water', '15_breweries', \
                    '16_bikes']

    for name in input_names:
        value = flask.request.form[name]
        scores_list.append(float(value.encode('utf-8')))

    flask.flash(scores_list)
    scores_array = np.array(scores_list)
    scores_distribution = scores_array/sum(scores_array)

    def find_comps(scores_distribution, num_comps=3):
        dists = {}
        comps = []
        for i in range(len(df_doc_topics)):
            dists[i] = cosine(df_doc_topics.ix[i].T, np.array(scores_distribution))
        max_keys = sorted(dists, key=dists.get)[:5]
        #print max_keys
        for key in max_keys:
            comps.append(zipped[key])
        max_topic_index = float(nmf_topics.index(zipped[max_keys[0]][2]))
        max_topic = zipped[max_keys[0]][2]
        return comps, max_topic_index, max_topic

    comps, max_topic_index, max_topic = find_comps(scores_distribution)
    #topic = 5.0;

    #return data
    flask.flash(comps)
    return flask.render_template("kojak_results.html", max_topic=max_topic, max_topic_index=max_topic_index)
    #return flask.redirect(flask.url_for("results_page"))


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
