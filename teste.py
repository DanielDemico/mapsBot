from geopy.geocoders import Nominatim
import time
from pegarEnd import dataframes


geolocator = Nominatim(user_agent="coordinate_collector")

# Lista de endereços para geocodificação
coordenadas = []
for dataframe in dataframes:
    for linha in dataframe.apply( lambda x: f"{x['City']}", axis=1):
    
        try:
            location = geolocator.geocode(linha)
            if location:
                coordenadas.append((linha, location.latitude, location.longitude))
                print(f"{linha}: {location.latitude}, {location.longitude}")
            else:
                print(f"{linha}: Não encontrado")
            time.sleep(1.2)  # Evitar bloqueios por uso excessivo
        except Exception as e:
            print(f"Erro com {linha}: {e}")

# Salvar no banco ou em um arquivo
print("Coordenadas coletadas:", coordenadas)