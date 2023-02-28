import hashlib
import datetime
# Creamos la clase Block, que representa cada bloque en nuestra cadena de bloques
class Block:
def __init__(self, data, timestamp, previous_hash):
self.data = data # datos almacenados en el bloque
self.timestamp = timestamp # marca de tiempo del bloque
self.previous_hash = previous_hash # hash del bloque anterior
self.hash = self.calculate_hash() # calculamos el hash del bloque actual
def calculate_hash(self):
# función para calcular el hash del bloque actual
hash_data = str(self.data) + str(self.timestamp) + str(self.previous_hash)
return hashlib.sha256(hash_data.encode()).hexdigest()
# Creamos la clase Blockchain, que es la cadena de bloques
class Blockchain:
def __init__(self):
self.chain = [self.create_danielapino_block()] # inicializamos la cadena de bloques con el bloque
def create_danielapino_block(self):
# función para crear el bloque daniela pino
return Block("Daniela Pino Block", datetime.datetime.now(), "0")
def add_block(self, new_block):
# función para añadir un nuevo bloque a la cadena de bloques
new_block.previous_hash = self.chain[-1].hash # definimos el hash del bloque anterior
new_block.hash = new_block.calculate_hash() # calculamos el hash del nuevo bloque
self.chain.append(new_block) # añadimos el nuevo bloque a la cadena de bloques
def print_blocks(self):
# función para imprimir los bloques en la cadena de bloques
for block in self.chain:
print("Data:", block.data) # mostramos los datos del bloque
print("Timestamp:", block.timestamp) # mostramos la marca de tiempo del bloque
print("Previous hash:", block.previous_hash) # mostramos el hash del bloque anterior
print("Hash:", block.hash) # mostramos el hash del bloque actual
print("\n") # agregamos una línea en blanco entre bloques
# Creamos una instancia de la clase Blockchain y añadimos algunos bloques de ejemplo
blockchain = Blockchain()
blockchain.add_block(Block("First block data", datetime.datetime.now(), "danielapino_block_hash"))
blockchain.add_block(Block("Second block data", datetime.datetime.now(), ""))
blockchain.add_block(Block("Third block data", datetime.datetime.now(), ""))
# Imprimimos los bloques en la cadena de bloques
blockchain.print_blocks()
