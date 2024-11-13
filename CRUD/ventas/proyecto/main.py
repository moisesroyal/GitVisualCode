import csv
import os


CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
CLIENT_TABLE = '.clients.csv'
clients = []


def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Usuario ya en cliente\'s lista')


def list_clients():
    print('uid |  name  | company  | email  | position ')
    print('*' * 50)

    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx, 
            name=client['name'], 
            company=client['company'], 
            email=client['email'], 
            position=client['position']))


def update_client(client_id, updated_client):
    global clients

    if len(clients) - 1 >= client_id:
        clients[client_id] = updated_client
    else:
        print('Usuario no en cliente\'s lista')


def delete_client(client_id):
    global clients

    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx] 
            break


def search_client(client_name):
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True


def _get_client_field(field_name, message='Que es el cliente {}?'):
    field = None

    while not field:
        field = input(message.format(field_name))

    return field


def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }

    return client


def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)


def _save_clients_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
        os.rename(tmp_table_name, CLIENT_TABLE)


def _print_welcome():
    print('Bienvenido a platzi ventas')
    print('*' * 50)
    print('Que quieres hacer hoy?:')
    print('[C]Crear cliente')
    print('[L]Lista de clientes')
    print('[A]Actualizar cliente')
    print('[E]Eliminar cliente')
    print('[B]Buscar cliente')


if __name__ == '__main__':
    _initialize_clients_from_storage()
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = _get_client_from_user()

        create_client(client)
    elif command == 'L':
        list_clients()
    elif command == 'A':
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()

        update_client(client_id, updated_client)
    elif command == 'E':
        client_id = int(_get_client_field('id'))

        delete_client(client_id)
    elif command == 'B':
        client_name = _get_client_field('name')
        found = search_client(client_name)
        
        if found:
            print('El cliente esta en la\'s lista')
        else:
            print('El cliente: {} No está en nuestra\'s lista'.format(client_name))
    else:
        print('Comando Invalido')

    _save_clients_to_storage()
