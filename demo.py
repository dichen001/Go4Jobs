import os, time, pickle
import numpy as np
import pandas as pd
import pandas.core.algorithms as algos

from sklearn import linear_model, naive_bayes, tree, svm
from sklearn.neighbors import NearestNeighbors
from random import randint, random, shuffle

from ABCD import ABCD

base_dir = os.getcwd()
input_csv = os.path.join(base_dir, 'ds_challenge_v2_1_data.csv')
pre_processed_csv = os.path.join(base_dir, 'processed.csv')
vector_csv = os.path.join(base_dir, 'vectors.csv')

"preprocessing"


def preprocess(input_path):
    # Import data & Parse the date columns.
    df = pd.read_csv(input_path, index_col=0, parse_dates=[4,5,6,10])

    # Replace date with time intervals
    df['bgc_interval'] = (df['bgc_date'] - df['signup_date']).dt.days
    df['vehicle_interval'] = (df['vehicle_added_date'] - df['signup_date']).dt.days
    df['trip_interval'] = (df['first_completed_date'] - df['signup_date']).dt.days

    # Get the binary class for whether the driver started a 1st trip or not.
    df['started'] = df['trip_interval'] >= 0

    # Clean the data by filling the empty cells.
    for i in ['signup_os', 'signup_channel', 'vehicle_make', 'vehicle_model']:
        df[i].fillna('other', inplace=True)
    for i in ['vehicle_year', 'bgc_interval', 'vehicle_interval', 'trip_interval']:
        df[i].fillna(-1, inplace=True)

    # Drop uninformative trips
    df.drop(['signup_date', 'bgc_date', 'vehicle_added_date', 'first_completed_date', 'trip_interval'], axis=1, inplace=True)

    # save the processed csv
    df.to_csv(os.path.join(os.getcwd(), "processed.csv"))


"convert data into nominal vector features"


def get_feture_vectors(input_path):
    df = pd.read_csv(input_path, index_col=0)
    print df.head(10)
    # save mappings from categorical to nominal
    mappings = {}
    for header in list(df):
        mapping = {}
        value_count = df[header].value_counts().index.tolist()
        for id, name in enumerate(value_count):
            mapping[name] = id
        mappings[header] = mapping
        df[header] = df[header].map(lambda x: mapping[x])

    # Aggregation
    for header in ['vehicle_make', 'vehicle_model', 'vehicle_year', 'bgc_interval', 'vehicle_interval']:
        # bins = algos.quantile(np.unique(df[header]), np.linspace(0, 1, 6))
        # df[header] = pd.tools.tile._bins_to_cuts(df[header], bins, include_lowest=True)
        mx = np.ma.masked_equal(df[header].values, 0, copy=True)
        bins = algos.quantile(df[header].values[~mx.mask], np.linspace(0, 1, 6))
        bins = np.insert(bins, 0, 0)
        bins[1] = bins[1] - (bins[1] / 2)
        df[header] = pd.tools.tile._bins_to_cuts(df[header], bins, include_lowest=True)

        # save the aggregation mapping
        mapping = {}
        for id, name in enumerate(df[header].unique().categories._values):
            mapping[name] = id
        mappings['aggregated_'+header] = mapping
        df[header] = df[header].map(lambda x: mapping[x])

    df.to_csv(vector_csv)
    return mappings, df.iloc[:, :-1].values, df.iloc[:, -1].values


"split data according to target label"


def split_two(corpus, label, target_label):
    pos = []
    neg = []
    for i, lab in enumerate(label):
        if lab == target_label:
            pos.append(i)
        else:
            neg.append(i)
    positive = corpus[pos]
    negative = corpus[neg]
    # positive = [corpus[i] for i in pos]
    # negative = [corpus[i] for i in neg]
    return {'pos': positive, 'neg': negative}


"smote"


def smote(data, num, k=5):
    corpus = []
    nbrs = NearestNeighbors(n_neighbors=k + 1, algorithm='ball_tree').fit(data)
    distances, indices = nbrs.kneighbors(data)
    for i in range(0, num):
        mid = randint(0, len(data) - 1)
        nn = indices[mid, randint(1, k)]
        datamade = []
        for j in range(0, len(data[mid])):
            gap = random()
            datamade.append((data[nn, j] - data[mid, j]) * gap + data[mid, j])
        corpus.append(datamade)
    corpus = np.array(corpus)
    return corpus


"SVM"


def do_classification(train_data, test_data, train_label, test_label, clf=''):
    if not clf:
        clf = tree.DecisionTreeClassifier()
    clf.fit(train_data, train_label)
    prediction = clf.predict(test_data)
    abcd = ABCD(before=test_label, after=prediction)
    F2 = np.array([k.stats()[-1] for k in abcd()])
    F1 = np.array([k.stats()[-2] for k in abcd()])
    P = np.array([k.stats()[1] for k in abcd()])
    R = np.array([k.stats()[0] for k in abcd()])
    label2 = list(set(test_label))
    if 'pos' in label2[0]:
        label1 = 0
    else:
        label1 = 1
    try:
        return P[label1], R[label1], F1[label1], F2[label1]
    except:
        pass


"cross validation"


def cross_val(clf='', data=[], label=[], target_label='', iterations=5, folds=5, issmote='no', title=''):
    "split for cross validation"

    def cross_split(corpus, folds, index):
        i_major = []
        i_minor = []
        l = len(corpus)
        for i in range(0, folds):
            if i == index:
                i_minor.extend(range(int(i * l / folds), int((i + 1) * l / folds)))
            else:
                i_major.extend(range(int(i * l / folds), int((i + 1) * l / folds)))
        return corpus[i_minor], corpus[i_major]

    "generate training set and testing set"

    def train_test(pos, neg, folds, index, issmote="smote", neighbors=5):
        pos_test, pos_train = cross_split(pos, folds=folds, index=index)
        neg_test, neg_train= cross_split(neg, folds=folds, index=index)
        if issmote == "smote":
            num = int((len(pos_train) + len(neg_train)) / 2)
            pos_train = smote(pos_train, num, k=neighbors)
            neg_train = neg_train[np.random.choice(len(neg_train), num, replace=False)]
        data_train = np.vstack((pos_train, neg_train))
        data_test = np.vstack((pos_test, neg_test))
        label_train = ['pos'] * len(pos_train) + ['neg'] * len(neg_train)
        label_test = ['pos'] * len(pos_test) + ['neg'] * len(neg_test)

        "Shuffle"
        tmp = range(0, len(label_train))
        shuffle(tmp)
        data_train = data_train[tmp]
        label_train = np.array(label_train)[tmp]

        tmp = range(0, len(label_test))
        shuffle(tmp)
        data_test = data_test[tmp]
        label_test = np.array(label_test)[tmp]

        return data_train, data_test, label_train, label_test

    # data, label = make_feature(corpus, method=feature, n_features=n_feature)
    data, label = np.array(data), np.array(label)
    split = split_two(corpus=data, label=label, target_label=target_label)
    pos = split['pos']
    neg = split['neg']

    print(str(len(pos)) + " positive-->" + str(target_label) + " in " + str(len(label)))

    start_time = time.time()
    measures = {'precision': [], 'recall': [], 'f1': [], 'f2': [] }
    for i in range(iterations):
        print 'iteration: ' + str(i)
        tmp = range(0, len(pos))
        shuffle(tmp)
        pos = pos[tmp]
        tmp = range(0, len(neg))
        shuffle(tmp)
        neg = neg[tmp]
        for index in range(folds):
            print 'folds: ' + str(index)
            data_train, data_test, label_train, label_test = \
                train_test(pos, neg, folds=folds, index=index, issmote=issmote)
            "SVM"
            p, r, f1, f2 = do_classification(data_train, data_test, label_train, label_test, clf=clf)
            measures['precision'].append(p)
            measures['recall'].append(r)
            measures['f1'].append(f1)
            measures['f2'].append(f2)
    res = measures
    print("\nTotal Runtime for [%s] in a %s-way cross val: --- %s seconds ---\n" % (title, str(folds), time.time() - start_time))
    return res


if __name__ == '__main__':
    # preprocess(input_csv)
    mapping, vectors, labels = get_feture_vectors(pre_processed_csv)

    learners = {'Decistion_Tree': tree.DecisionTreeClassifier(min_samples_split=20), \
                'SVM': svm.SVC(kernel='linear'), \
                'Logic_Regression': linear_model.LogisticRegression(C=1e5), \
                'Naive_Bayes': naive_bayes.GaussianNB()
                }

    F_final = {}
    for name, learner in learners.iteritems():
        F_final[name] = cross_val(clf=learner, data=vectors, label=labels, target_label=1, iterations=5, folds=10, issmote='no')

    with open(os.path.join(base_dir, 'no_smote_performance.pickle'), 'wb') as handle:
        pickle.dump(F_final, handle)

    print(F_final)
    print 'done'