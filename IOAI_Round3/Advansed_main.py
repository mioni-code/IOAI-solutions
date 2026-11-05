import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

train = pd.read_csv('training_file.csv')
test = pd.read_csv('test_file.csv')

X_train = train.drop(columns=['id', 'target'])
y_train = train['target']
X_test = test.drop(columns=['id'])

model = GradientBoostingClassifier(
    n_estimators=200, 
    learning_rate=0.1, 
    max_depth=5, 
    random_state=42
)

print("Training in progress...")
model.fit(X_train, y_train)

predictions = model.predict(X_test)
output_filename = 'ryabokon_prediction.csv'
submission = pd.DataFrame({
    'id': test['id'],
    'target': predictions
})

submission.to_csv(output_filename, index=False)
print(f"Process completed. File '{output_filename}' has been created.")

print("\n" + "="*30)
print("RESULTS SUMMARY:")
print("="*30)
counts = submission['target'].value_counts()
print(f"Total rows: {len(submission)}")
print(f"Zeros (0): {counts.get(0, 0)}")
print(f"Ones  (1): {counts.get(1, 0)}")

print("\nFirst 10 predictions:")
print(submission.head(10))
print("="*30)