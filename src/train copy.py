import argparse
# from html import parser
# import os
# import pandas as pd
# import mlflow
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.model_selection import train_test_split
from dateutil import parser
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient


def main():
    # 1. Parse Arguments
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--training_data", type=str, help="Path to training data")
    # parser.add_argument("--n_estimators", type=int, default=100)
    # args = parser.parse_args()

    # print(f"Training data path: {args.training_data}")
    # print(f"Number of estimators: {args.n_estimators}")

    dt = parser.parse("2026-02-14 10:30")
    print("Parsed date:", dt)
    
    import os

    # 1. Provide the Vault URL (can be passed via environment variable)
    vault_url = os.environ.get("KEY_VAULT_URL", "https://cashclearingai6551529325.vault.azure.net/")

    # 2. Use the Managed Identity automatically
    credential = DefaultAzureCredential()

    # 3. Connect to the client
    client = SecretClient(vault_url=vault_url, credential=credential)

    # 4. Pull your DB credentials
    test_val = client.get_secret("test-secret").value
    

    print(f"Successfully retrieved test value: {test_val}")
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