from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# 1. Provide the Vault URL (can be passed via environment variable)
vault_url = "https://cashclearingai6551529325.vault.azure.net/"

# 2. Use the Managed Identity automatically
credential = DefaultAzureCredential()

# 3. Connect to the client
client = SecretClient(vault_url=vault_url, credential=credential)

# 4. Pull your DB credentials
test_val = client.get_secret("test-secret").value


print(f"Successfully retrieved test value: {test_val}")