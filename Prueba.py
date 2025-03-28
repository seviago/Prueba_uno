precio_final_invierno = 3  # UE
descuento_invierno = 15  # %
precio_original_invierno = precio_final_invierno / (1 - descuento_invierno / 100)

precio_final_verano = 30  # €
descuento_verano = 5  # %
precio_original_verano = precio_final_verano / (1 - descuento_verano / 100)

es_mejor_invierno = precio_final_invierno < precio_final_verano

print(f"Precio original en invierno: {precio_original_invierno:.2f} UE")
print(f"Precio original en verano: {precio_original_verano:.2f} €")
print(f"¿Es mejor comprar en invierno? {es_mejor_invierno}")