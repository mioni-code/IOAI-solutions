import pandas as pd
from sklearn.ensemble import RandomForestClassifier

train = pd.read_csv('training_file.csv')
print(train['target'].value_counts())
print(train.describe())
test = pd.read_csv('test_file.csv')

X_train = train.drop(columns=['id', 'target']) 
y_train = train['target']
X_test = test.drop(columns=['id'])

model = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42) 
print("Starting training...")
model.fit(X_train, y_train)
print("Training completed!")

predictions = model.predict(X_test)
submission = pd.DataFrame({
    'Id': test['id'], 
    'Prediction': predictions
})

submission.to_csv('my_prediction.csv', index=False)
print("File my_prediction.csv is ready!")