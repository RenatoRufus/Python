import colorama
from colorama import Fore, Back, Style

# No Ubuntu/Linux, o autoreset é tecnicamente opcional,
# mas é mantido para garantir que o estilo não "vaze"
# se a saída for redirecionada ou para maior compatibilidade.
colorama.init(autoreset=True) 

def mostrar_cores():
    """Mostra exemplos de diferentes cores de texto e fundo."""
    print("## Demonstração de Cores com Colorama")
    print("-" * 40)
    print(f"{Fore.RED}Este texto está em vermelho.")
    print(f"{Fore.GREEN}Este texto está em verde.")
    print(f"{Fore.YELLOW}Este texto está em amarelo.")
    print(f"{Fore.BLUE}Este texto está em azul.")
    print(f"{Fore.MAGENTA}Este texto está em magenta.")
    print(f"{Fore.CYAN}Este texto está em ciano.")
    print(f"{Fore.WHITE}Este texto está em branco (cor padrão).")
    print(f"{Fore.BLACK}{Back.WHITE}Este texto é preto com fundo branco.")
    print(f"{Fore.LIGHTRED_EX}Este é um vermelho claro/brilhante.")
    print(f"{Style.BRIGHT}{Fore.BLUE}Este texto está em azul e em negrito/brilhante.")
    print(f"{Style.DIM}Este texto está em modo 'dim'/fraco.")
    print(f"{Style.RESET_ALL}O estilo e a cor voltaram ao normal.")
    print("-" * 40)

def gerar_tabela_ascii():
    """Gera e exibe uma tabela completa de caracteres ASCII (0-127)."""
    
    print(f"\n## {Fore.CYAN}📑 Tabela ASCII Completa (0-127) {Style.RESET_ALL}")
    
    # Cabeçalho da tabela
    header = f"| {Style.BRIGHT}{Fore.YELLOW}DEC{Style.RESET_ALL} | {Style.BRIGHT}{Fore.YELLOW}HEX{Style.RESET_ALL} | {Style.BRIGHT}{Fore.YELLOW}Caractere{Style.RESET_ALL} | {Style.BRIGHT}{Fore.YELLOW}Descrição{Style.RESET_ALL} "
    separator = "=" * (len(header) + 4)

    print(separator)
    print(header)
    print(separator)

    # Lista de descrições para caracteres de controle não imprimíveis (0-31 e 127)
    descricoes_controle = {
        0: "Null (NUL)", 1: "Start of Header (SOH)", 2: "Start of Text (STX)", 3: "End of Text (ETX)", 
        4: "End of Transmit (EOT)", 5: "Enquiry (ENQ)", 6: "Acknowledge (ACK)", 7: "Bell (BEL)", 
        8: "Backspace (BS)", 9: "Horizontal Tab (HT)", 10: "Line Feed (LF)", 11: "Vertical Tab (VT)", 
        12: "Form Feed (FF)", 13: "Carriage Return (CR)", 14: "Shift Out (SO)", 15: "Shift In (SI)", 
        16: "Data Link Escape (DLE)", 17: "Device Control 1 (DC1)", 18: "Device Control 2 (DC2)", 
        19: "Device Control 3 (DC3)", 20: "Device Control 4 (DC4)", 21: "Negative Ack. (NAK)", 
        22: "Synchronous Idle (SYN)", 23: "End of Transmit Block (ETB)", 24: "Cancel (CAN)", 
        25: "End of Medium (EM)", 26: "Substitute (SUB)", 27: "Escape (ESC)", 28: "File Sep. (FS)", 
        29: "Group Sep. (GS)", 30: "Record Sep. (RS)", 31: "Unit Sep. (US)", 32: "Espaço (SPACE)",
        127: "Delete (DEL)"
    }

    # Loop para gerar a tabela de 0 a 127
    for i in range(128):
        dec = str(i).center(3)
        hex_val = hex(i)[2:].upper().zfill(2).center(3)
        
        # Define a cor e a descrição baseadas no tipo de caractere
        if i in descricoes_controle:
            descricao = descricoes_controle[i]
            if i in range(0, 32) or i == 127:
                 # Caracteres de controle não imprimíveis
                char_display = "CTL" 
                cor = Fore.RED + Style.DIM
            else: # i == 32 (Espaço)
                char_display = " "
                cor = Fore.YELLOW
        else:
            # Caracteres imprimíveis
            char_display = chr(i)
            descricao = "Imprimível"
            cor = Fore.GREEN

        
        # Formata a linha
        line = f"| {cor}{dec}{Style.RESET_ALL} | {cor}{hex_val}{Style.RESET_ALL} | {cor}{char_display.center(9)}{Style.RESET_ALL} | {cor}{descricao.ljust(15)}{Style.RESET_ALL} "
        print(line)

        # Adiciona uma linha divisória para agrupar visualmente, tornando a tabela mais legível
        if i % 16 == 15 or i == 32: 
            print(separator)
            
    print(f"\n{Fore.MAGENTA}A tabela ASCII padrão vai de 0 a 127. {Style.RESET_ALL}")
    

# --- Execução Principal ---
if __name__ == "__main__":
    mostrar_cores()
    generar_tabela_ascii()
    
    colorama.deinit()