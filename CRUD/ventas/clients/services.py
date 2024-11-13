

from common.services import PVService
from clients.models import Client
class ClientService(PVService):
   
    def __init__(self,table_name):
        super().__init__(table_name)
        
    def create_client(self,client):
        
        """ with open(self.table_name,mode='a') as f:
            writer=csv.DictWriter(f,fieldnames=Client.schema())
            writer.writerow(client.to_dict())
 """
        self.create(client.to_dict(),Client.schema())
    
    def list_clients(self):
        return self.list(Client.schema())
        

    def update_client(self,updated_client):
        self.update(updated_client.to_dict(),Client.schema())
        
    """ def _save_to_disk(self,clients):
        tmp_table_name = self.table_name +'.tmp'
        with open(tmp_table_name) as f:
            writer = csv.DictWriter(f,fieldnames=Client.schema())
            writer.writerows(clients) 
    
        #ahora solo queda borrar el archivo original, luego renombrar el tmp y dejarlo con el nombre del original
        os.remove(self.table_name)
        os.rename(tmp_table_name,self.table_name)
 """

    def delete_client(self,client_uid):
        self.delete(client_uid,Client.schema())
    
