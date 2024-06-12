
import os

AZURE_STORAGE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=projetoporto;AccountKey=+SpE/HO6ZMv2VXJ+GQEYhdriMpfpA45BcyvHOc2u65BVDb3UiHi8+JqwTmOpf8kTw9IO4+2IaA9r+AStPJf6wg==;EndpointSuffix=core.windows.net"
AZURE_STORAGE_CONTAINER_NAME = "your-container-name"
SECRET_KEY = os.urandom(32)  # Use a chave secreta consistente em produção
