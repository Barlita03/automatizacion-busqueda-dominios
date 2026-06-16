import whois
import time
import sys
import os

def check_domain(domain):
    try:
        w = whois.whois(domain)
        if w.domain_name is None and w.creation_date is None:
            return True
        return False
    except Exception as e:
        return True

def main():
    input_file = 'propuestas_dominios_3.txt'
    output_file = 'dominios_disponibles_3.md'
    
    if not os.path.exists(input_file):
        print(f"Error: No se encontró el archivo {input_file}.")
        sys.exit(1)
        
    with open(input_file, 'r', encoding='utf-8') as f:
        domains = [line.strip() for line in f if line.strip()]
        
    available_domains = []
    
    print(f"Iniciando verificación de {len(domains)} dominios de UNA SOLA PALABRA...")
    
    for i, domain in enumerate(domains):
        print(f"[{i+1}/{len(domains)}] Verificando {domain}...", end=" ")
        sys.stdout.flush()
        
        is_available = check_domain(domain)
        if is_available:
            print("DISPONIBLE")
            available_domains.append(domain)
        else:
            print("OCUPADO")
            
        time.sleep(2)
        
    print(f"\nFinalizado. {len(available_domains)} dominios de una sola palabra disponibles.")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Dominios de UNA SOLA PALABRA Disponibles\n\n")
        f.write("Los siguientes dominios de una palabra inventada (neologismos) fueron verificados y están libres:\n\n")
        if available_domains:
            for d in available_domains:
                f.write(f"- {d}\n")
        else:
            f.write("Lamentablemente, no se encontraron dominios disponibles. Las palabras únicas son difíciles de conseguir.\n")
            
    print(f"Resultados guardados en {output_file}")

if __name__ == "__main__":
    main()
