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

    '''
    #read data that came with sliders post
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
    '''
    city_master = {'austin': 'Austin',
                    'newyorkcity': 'New York',
                    'neworleans': 'New Orleans',
                    'chicago': 'Chicago',
                    'denver': 'Denver',
                    'portland': 'Portland',
                    'seattle': 'Seattle',
                    'sanfrancisco': 'San Francisco',
                    'sandiego': 'San Diego',
                    'boston': 'Boston',
                    'losangeles': 'Los Angeles',
                    'nashville': 'Nashville',
                    'washingtondc': 'Washington, DC',
                    'oakland': 'Oakland, CA'
                    }

    topic_master = {'1_taco': 'Taco',
                    '2_subway': 'Subways',
                    '3_car': 'Cars',
                    '4_museum': 'Museum',
                    '5_farmer': "Farmers' Market",
                    '6_campus': 'Campus',
                    '7_diverse': 'Diverse',
                    '8_art': 'Art',
                    '9_nightlife': 'Nightlife',
                    '10_attractions': 'Attractions',
                    '11_golf': 'Golf',
                    '12_outdoors': 'Outdoors',
                    '13_streetcars': 'Streetcars',
                    '14_water': 'Water',
                    '15_breweries': 'Breweries',
                    '16_bikes': 'Bikes'
                    }

    #read data that came with textbox post
    neighborhood_name = flask.request.form['neighborhood']
    #city_name = flask.request.form['city']

    #def find_dist(neighborhood_name, city_name):
    def find_dist(neighborhood_name):
        neighborhood_index = df_loc[df_loc['neighborhood']==neighborhood_name].index[0]
        neighborhood_dist = np.array(df_doc_topics.iloc[neighborhood_index])

        dists = {}
        for i in range(len(df_doc_topics)):
            dists[i] = cosine(df_doc_topics.ix[i].T, np.array(neighborhood_dist))
        max_keys = sorted(dists, key=dists.get)#[:num_comps]
        comps = []
        count = 0
        for key in max_keys:
            if count <= 10:
                if zipped[key][0] != neighborhood_name:
                    comps.append(zipped[key])
                    count += 1
        return comps

    '''
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
    '''

    comps = find_dist(neighborhood_name)
    n1 = str(comps[0][0])
    n2 = str(comps[1][0])
    n3 = str(comps[2][0])
    n4 = str(comps[3][0])
    n5 = str(comps[4][0])
    n6 = str(comps[5][0])
    n7 = str(comps[6][0])
    n8 = str(comps[7][0])
    n9 = str(comps[8][0])
    n10 = str(comps[9][0])
    c1 = city_master[str(comps[0][1])]
    c2 = city_master[str(comps[1][1])]
    c3 = city_master[str(comps[2][1])]
    c4 = city_master[str(comps[3][1])]
    c5 = city_master[str(comps[4][1])]
    c6 = city_master[str(comps[5][1])]
    c7 = city_master[str(comps[6][1])]
    c8 = city_master[str(comps[7][1])]
    c9 = city_master[str(comps[8][1])]
    c10 = city_master[str(comps[9][1])]
    max_topic = comps[0][2]
    #max_topic_index = 0
    #max_topic_index = float(nmf_topics.index(zipped[max_topic]))
    #comps, max_topic_index, max_topic = find_comps(scores_distribution)
    #topic = 5.0;

    #return data
    flask.flash(comps)
    return flask.render_template("kojak_results.html", neighborhood_name=neighborhood_name, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, c9=c9, c10=c10, n1=n1, n2=n2, n3=n3, n4=n4, n5=n5, n6=n6, n7=n7, n8=n8, n9=n9, n10=n10, max_topic=max_topic)
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
