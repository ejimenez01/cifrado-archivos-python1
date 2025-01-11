from cryptography.fernet import Fernet
import os

def generate_key():
    """Genera una clave de cifrado y la guarda en un archivo."""
    key = Fernet.generate_key()
    with open("clave.key", "wb") as key_file:
        key_file.write(key)
    print("Clave generada y guardada en 'clave.key'.")


def load_key():
    """Carga la clave desde el archivo 'clave.key'."""
    if not os.path.exists("clave.key"):
        print("Error: No se encontró el archivo 'clave.key'. Genera una clave primero.")
        return None
    with open("clave.key", "rb") as key_file:
        return key_file.read()


def encrypt_file(filename):
    """Cifra un archivo con la clave cargada."""
    key = load_key()
    if not key:
        return
    fernet = Fernet(key)

    try:
        with open(filename, "rb") as file:
            data = file.read()

        encrypted_data = fernet.encrypt(data)

        with open(filename + ".enc", "wb") as enc_file:
            enc_file.write(encrypted_data)

        print(f"Archivo '{filename}' cifrado exitosamente como '{filename}.enc'.")
    except FileNotFoundError:
        print(f"Error: El archivo '{filename}' no existe.")


def decrypt_file(encrypted_filename):
    """Descifra un archivo cifrado con la clave cargada."""
    key = load_key()
    if not key:
        return
    fernet = Fernet(key)

    try:
        with open(encrypted_filename, "rb") as enc_file:
            encrypted_data = enc_file.read()

        decrypted_data = fernet.decrypt(encrypted_data)

        original_filename = encrypted_filename.replace(".enc", "")
        with open(original_filename, "wb") as dec_file:
            dec_file.write(decrypted_data)

        print(f"Archivo '{encrypted_filename}' descifrado exitosamente como '{original_filename}'.")
    except FileNotFoundError:
        print(f"Error: El archivo '{encrypted_filename}' no existe.")
    except Exception as e:
        print(f"Error al descifrar el archivo: {e}")


# Menú principal
if __name__ == "__main__":
    while True:
        print("\n=== Menú de Cifrado y Descifrado ===")
        print("1. Generar clave")
        print("2. Cifrar archivo")
        print("3. Descifrar archivo")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            generate_key()
        elif opcion == "2":
            filename = input("Introduce el nombre del archivo a cifrar: ")
            encrypt_file(filename)
        elif opcion == "3":
            encrypted_filename = input("Introduce el nombre del archivo cifrado: ")
            decrypt_file(encrypted_filename)
        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")
