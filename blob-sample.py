from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

credential = DefaultAzureCredential(
    exclude_environment_credential=True,
    exclude_managed_identity_credential=True,
    exclude_visual_studio_code_credential=True,
    exclude_cli_credential=True,
    exclude_shared_token_cache_credential=True,
    exclude_interactive_browser_credential=False
)

blob_url = 'https://demostoragead.blob.core.windows.net/'

service_client = BlobServiceClient(
    account_url=blob_url,
    credential=credential
)

blob_client = service_client.get_blob_client(container='entry', blob='git_flow.pdf')

with open('result.pdf', 'wb') as my_blob:
    blob_data = blob_client.download_blob()
    blob_data.readinto(my_blob)

print('Done!')