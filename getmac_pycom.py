from network import LoRa
import ubinascii

lora = LoRa(mode=LoRa.LORAWAN)
print(ubinascii.hexlify(lora.mac()).upper().decode('utf-8'))

#thismoduledoesn't work with the OS it works the pycom console 