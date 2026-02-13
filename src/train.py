import argparse
import os
import pandas as pd
import mlflow
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

def main():
    # 1. Parse Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--training_data", type=str, help="Path to training data")
    parser.add_argument("--n_estimators", type=int, default=100)
    args = parser.parse_args()

    print(f"Training data path: {args.training_data}")
    print(f"Number of estimators: {args.n_estimators}")
    # 2. Start MLflow (Azure ML tracks this automatically)
    # mlflow.autolog()
    
    # with mlflow.start_run():
    #     # 3. Load Data
    #     df = pd.read_csv(args.training_data)
    #     X = df.drop(columns=['target'])
    #     y = df['target']
        
    #     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        
    #     # 4. Train Model
    #     model = RandomForestRegressor(n_estimators=args.n_estimators)
    #     model.fit(X_train, y_train)
        
    #     # 5. Log a metric manually (optional)
    #     score = model.score(X_test, y_test)
    #     mlflow.log_metric("r2_score", score)
        
    #     # 6. Save the model
    #     mlflow.sklearn.log_model(model, "outputs/model")

if __name__ == "__main__":
    main()