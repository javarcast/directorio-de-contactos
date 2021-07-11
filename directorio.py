import csv


class Contact:
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:
    def __init__(self):
        self._contacts =[]



    def add(self, contact_user):
        self._contacts.append(contact_user)
        self._save()

    def _save(self):
        with open('contacts.csv','w',encoding="utf8") as f:
            writer = csv.writer(f)
            writer.writerow(('name','phone','email'))
            
            for contact in self._contacts:
                writer.writerow((contact.name,contact.phone,contact.email))


    def delete(self,user_name):
        index_contact = self._search_contact(user_name)
        if index_contact == -1:
            self._not_found()
        else:
            del self._contacts[index_contact]
            self._save()
    
    def update(self,user_name,user_update):
        index_contact = self._search_contact(user_name)
        if index_contact == -1:
            self._not_found()
        else:
            self._contacts[index_contact].name = user_update.name   
            self._contacts[index_contact].phone = user_update.phone
            self._contacts[index_contact].email = user_update.email
            self._save()
    
    
    def search(self,user_name):
        index_contact = self._search_contact(user_name)
        if index_contact == -1:
            self._not_found()
        else:
            self._print_contact(self._contacts[index_contact])


    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)


    def _search_contact(self,user_name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == user_name.lower():
                return idx
        return -1

    def _print_contact(self,contact):
        print('*-*-*-*-*-**--*-*-**-*-*-*-*-*-*')
        print('Nombre: {}'.format(contact.name))
        print('Telefono: {}'.format(contact.phone))
        print('Correo: {}'.format(contact.email))
        print('*-*-*-*-*-**--*-*-**-*-*-*-*-*-*')

    def _not_found(self):
        print('Contacto no encontrado.!!!')

def run():
    contact_book = ContactBook()

    with open('contacts.csv','r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0 or row==[]:
                continue
            contact_sv = Contact(row[0],row[1],row[2])
            contact_book.add(contact_sv)

    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''))

        if command == 'a':

            name = str(input('Escribe el nombre del contacto: '))
            phone = str(input('Escribe el telefono del contacto: '))
            email = str(input('Escribe el correo del contacto: '))
            contact_user = Contact(name,phone,email)
            contact_book.add(contact_user)

        elif command == 'ac':
            print('actualizar contacto')

        elif command == 'b':
            name = str(input('Ingresa el nombre del contacto a buscar: '))
            contact_book.search(name)


        elif command == 'e':
            name = str(input('Ingresa el nombre del contacto a eliminar: '))
            contact_book.delete(name)

        elif command == 'l':
            contact_book.show_all()

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    print('B I E N V I D O  A  C O N T A T O S')
    run()