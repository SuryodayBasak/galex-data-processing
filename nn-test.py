import pandas as pd
import numpy as np
import tensorflow as tf

def train_input_fn(features, labels, batch_size):
    """An input function for training"""
    # Convert the inputs to a Dataset.
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))

    # Shuffle, repeat, and batch the examples.
    dataset = dataset.shuffle(1000).repeat().batch(batch_size)

    # Return the dataset.
    #print(dataset)
    return dataset

def eval_input_fn(features, labels, batch_size):
    """An input function for evaluation or prediction"""
    features=dict(features)
    if labels is None:
        # No labels, use only features.
        inputs = features
    else:
        inputs = (features, labels)

    # Convert the inputs to a Dataset.
    dataset = tf.data.Dataset.from_tensor_slices(inputs)

    # Batch the examples
    assert batch_size is not None, "batch_size must not be None"
    dataset = dataset.batch(batch_size)

    # Return the dataset.
    return dataset

def find_conf_matrix(lbls_true_pred):
    
df = pd.read_csv("../data/bestCaseData2_specter.csv",
                    usecols=[4, 5, 6, 7, 8, 9, 11])
class_map = {'STAR': 0, 'GALAXY': 1, 'QSO': 2}
df['class'].replace(class_map, inplace=True)
split_thresh = np.random.rand(len(df)) < 0.95

train = df[split_thresh]
test =df[~split_thresh]

train_x = train.loc[:,['u', 'g', 'r', 'i', 'z', 'nuv_mag']]
train_y = train.loc[:,['class']]

test_x = test.loc[:,['u', 'g', 'r', 'i', 'z', 'nuv_mag']]
test_y = test.loc[:,['class']]

#print(test_y)
#print(train)

# Feature columns describe how to use the input.
my_feature_columns = []
for key in train_x.keys():
    my_feature_columns.append(tf.feature_column.numeric_column(key=key))
#print(my_feature_columns)

# Build 2 hidden layer DNN with 10, 10 units respectively.
classifier = tf.estimator.DNNClassifier(
    feature_columns=my_feature_columns,
    # Two hidden layers of 10 nodes each.
    hidden_units=[1000, 1000, 1000, 1000],
    # The model must choose between 3 classes.
    n_classes=3,
    model_dir="saved-model")

# Evaluate the model.
eval_result = classifier.evaluate(
    input_fn=lambda:eval_input_fn(test_x, test_y, 300))

print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))

predict_x = {
    'u': list(test_x.ix[:, ['u']]),
    'g': list(test_x.ix[:, ['g']]),
    'r': list(test_x.ix[:, ['r']]),
    'i': list(test_x.ix[:, ['i']]),
    'z': list(test_x.ix[:, ['z']]),
    'nuv_mag': list(test_x.ix[:, ['nuv_mag']])
}

predict_y = {
    'u': list(test_x.ix[:,['class']])
}

expected = ['STAR', 'GALAXY', 'QSO']
predictions = classifier.predict(
    input_fn=lambda:eval_input_fn(test_x, test_y, 300))
    #input_fn=lambda:eval_input_fn(predict_x, predict_y, batch_size=300))

template = ('\nPrediction is ({:.1f}%), expected "{}"')

"""
for pred_dict, expec in zip(predictions, expected):
    class_id1 = pred_dict['class_ids'][0]
    p1 = pred_dict['probabilities'][class_id1]

    print(100 * p1, expec)
"""

count = 0
true_lbls = list(test_y['class'])
for pred_dict in zip(predictions):
    cls = int(pred_dict[0]['classes'][0])
    print(expected[cls])
    print(pred_dict[0]['probabilities'])
    #print('True class = ', test_y[count])
    print('True Label = ', true_lbls[count], 'Pred Label = ', cls)
    count += 1
    print('')

#template = ('\nPrediction is "{}" ({:.1f}%), expected "{}"')

print(predictions)
"""
new_classifier = tf.contrib.learn.DNNClassifier(feature_columns=my_feature_columns,
        hidden_units=[1000, 1000, 1000, 1000],
        n_classes=3,
        model_dir="saved-model")

eval_result = new_classifier.evaluate(
    input_fn=lambda:eval_input_fn(test_x, test_y, 100))
print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))

#print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))
"""
