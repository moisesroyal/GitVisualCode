class Clients:

    def __init__(self, table_name):
        self.table_name = table_name

        def create_client(self):
            with open (self.table_name, mode = 'a') as f:
                writer = csv.DictWriter(f, fieldnames = Client.schema())
                writer.whiterow(client.to_dict())
