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

# Train the Model.
classifier.train(
    input_fn=lambda:train_input_fn(train_x, train_y, 300),
    steps=1000)

# Evaluate the model.
eval_result = classifier.evaluate(
    input_fn=lambda:eval_input_fn(test_x, test_y, 300))

print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))
