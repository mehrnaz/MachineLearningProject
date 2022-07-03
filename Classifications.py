from sklearn import metrics, tree, svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import os
from imblearn.ensemble import BalancedBaggingClassifier, BalancedRandomForestClassifier

def prec_rec_f1_for_both(confusion_matrix, y_test, pred):
    print('Precision score (blacklisted):', metrics.precision_score(y_test, pred))
    print('Recall score (blacklisted):', metrics.recall_score(y_test, pred))
    print('F1 score (blacklisted):', metrics.f1_score(y_test, pred))
    tp = confusion_matrix[0][0]
    fp = confusion_matrix[1][0]
    fn = confusion_matrix[0][1]
    prec = tp / (tp + fp)
    rec = tp / (tp + fn)
    f1 = 2 * ((prec * rec) / (prec + rec))
    print('Precision score (legitimate):', prec)
    print('Recall score (legitimate):', rec)
    print('F1 score (legitimate):', f1)


def print_eval(classifier_name, y_test, pred):
    print("------", classifier_name, "------")
    # print(list(pred).count(0), " ", list(pred).count(1), " ", len(pred))
    print('Test accuracy score: ', metrics.accuracy_score(y_test, pred))
    print(metrics.confusion_matrix(y_test, pred))
    prec_rec_f1_for_both(metrics.confusion_matrix(y_test, pred), y_test, pred)
    print('Macro averaged F1:', metrics.f1_score(y_test, pred, average='macro'))
    print('Micro averaged F1:', metrics.f1_score(y_test, pred, average='micro'))


def test_classifier(data, reduceLegitimate, numOfLegitimate, interesting_col, label, classifier, classifier_name):
    if reduceLegitimate:
        data = pd.concat((data.loc[data['Blacklisted'] == 1], data.loc[data['Blacklisted'] == 0].sample(numOfLegitimate)))
    x = data[interesting_col]
    y = data[label]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
    cl = classifier.fit(x_train, y_train.values.ravel())
    pred = cl.predict(x_test)
    print_eval(classifier_name, y_test, pred)


p = os.path.join(".", "processedData", "data_csv_all_points_noDNSqueries.csv")
data = pd.read_csv(p)
dataReduced = pd.concat((data.loc[data['Blacklisted'] == 1], data.loc[data['Blacklisted'] == 0].sample(1500)))
interesting_col = ["shortLife_nchanges", "shortLife_avgReq", "dailySimilarity",
                           "repeatingPatterns_nChanges", "repeatingPatterns_avgReq", "repeatingPatterns_stdChangeLen",
                           "accessRatio_idle", "accessRatio_active", "NumberOfDistinctIps", "AverageTTL",
                           "StdDevOfTTL", "NumOfDistTTL", "NumOfTTLChange", "SpecTTL01", "SpecTTL110", "SpecTTL10100",
                           "SpecTTL100300", "SpecTTL300900", "SpecTTL900inf",
                           "PercOfNumChars", "PercOfLengthOfLMS"]

label = ["Blacklisted"]

randFor = RandomForestClassifier()
decTree = tree.DecisionTreeClassifier()
balancedTree = BalancedBaggingClassifier()
balancedForest = BalancedRandomForestClassifier()



test_classifier(data, True, 1500, interesting_col, label, randFor, "Random forest")
test_classifier(data, True, 1500, interesting_col, label, decTree, "Decision tree")
test_classifier(data, True, 1500, interesting_col, label, balancedForest, "Random forest Balanced")
test_classifier(data, True, 1500, interesting_col, label, balancedTree, "Decision tree Balanced")


x = data[interesting_col]
y = data[label]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

randFor = RandomForestClassifier()
decTree = tree.DecisionTreeClassifier()
balancedTree = BalancedBaggingClassifier()
balancedForest = BalancedRandomForestClassifier()

test_classifier(data, False, 2000, interesting_col, label, randFor, "Random forest")
test_classifier(data, False, 2000, interesting_col, label, decTree, "Decision tree")
test_classifier(data, False, 2000, interesting_col, label, balancedForest, "Random forest Balanced")
test_classifier(data, False, 2000, interesting_col, label, balancedTree, "Decision tree Balanced")