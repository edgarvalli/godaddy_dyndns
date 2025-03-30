from config import Config
from tools import log, get_public_ip
from godaddypy import Client, Account

class GodaddyAPI:
    def __init__(self):
        self.config = Config()
        self.api_key = self.config.GODADDY_API_KEY
        self.api_secret = self.config.GODADDY_API_SECRET
        

    def godaddy_client(self):
        return Client(Account(api_key=self.api_key, api_secret=self.api_secret))
    
    def update_a_record(self, domain: str, record_name:str, last_public_ip:str):
        
        client = self.godaddy_client()

        # Configura los parámetros del dominio
        new_ip = get_public_ip()   # Reemplaza con la nueva IP

        if new_ip == last_public_ip:
            return log('No hay cambios en la IP. No se actualizará el registro.')
        
        else:

            self.config.set_public_ip(domain, new_ip)

            # Actualizar el registro A
            try:
                # Obtener los registros actuales
                records = client.get_records(domain, record_type='A', name=record_name)
                
                if records:
                    # Actualizar el primer registro A encontrado (puedes modificar esto si tienes múltiples)
                    record = records[0]
                    record['data'] = new_ip
                    
                    # Enviar la actualización
                    update_result = client.update_record(domain, record)
                    message = 'Registro A actualizado correctamente. Nueva IP: {}'.format(new_ip)
                    log(message)
                else:
                    # Si no existe el registro, crearlo
                    new_record = {
                        'data': new_ip,
                        'name': record_name,
                        'ttl': 600,
                        'type': 'A'
                    }
                    add_result = client.add_record(domain, new_record)
                    log(f"Registro A creado con IP: {new_ip}")
                    
            except Exception as e:
                log(f"Error al actualizar el registro A: {str(e)}")