import warnings
from sklearn.exceptions import ConvergenceWarning
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler

if __name__ == '__main__':
    warnings.filterwarnings('ignore', category=ConvergenceWarning)

    neurons_num = int(input())

    M_classes = [x for x in data if x[0] == 'M']
    B_classes = [x for x in data if x[0] == 'B']

    train_set = M_classes[:int(len(M_classes) * 0.7)] + B_classes[:int(len(B_classes) * 0.7)]
    test_set = M_classes[int(len(M_classes) * 0.7):] + B_classes[int(len(B_classes) * 0.7):]

    train_x = [x[1:] for x in train_set]
    train_y = [x[0] for x in train_set]
    test_x = [x[1:] for x in test_set]
    test_y = [x[0] for x in test_set]

    scaler = MinMaxScaler(feature_range=(-1, 1))
    scaler.fit(train_x)

    classifier = MLPClassifier(neurons_num, activation='relu', learning_rate_init=0.001, max_iter=20, random_state=0)
    classifier.fit(scaler.transform(train_x), train_y)
    

    tp, fp, tn, fn = 0, 0, 0, 0
    predictions = classifier.predict(scaler.transform(test_x))
    for pred, true in zip(predictions, test_y):
        if true == 'M':
            if pred == true:
                tp += 1
            else:
                fn = +1
        else:
            if pred == true:
                tn += 1
            else:
                fp += 1

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)

    train_set_precision, train_set_recall = tp / (tp + fp), tp / (tp + fn)

    print(f'Preciznost so trenirachkoto mnozhestvo: {train_set_precision}')
    print(f'Odziv so trenirachkoto mnozhestvo: {train_set_recall}')
    #print(f'Preciznost so testirachkoto mnozhestvo: {test_set_precision}')
    #print(f'Preciznost so testirachkoto mnozhestvo: {test_set_recall}')
