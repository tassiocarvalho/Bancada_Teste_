import matplotlib.pyplot as plt
import numpy as np

# Dados organizados por tensão
# Formato: [peso (g), rpm]
dados_10v = [
    [14, 3500], [20, 4000], [24, 4550], [27, 4660], [32, 4910], [36, 5200], 
    [38, 5400], [41, 5610], [43, 5770], [47, 5880], [50, 6120], [52, 6270], 
    [54, 6440], [57, 6600], [59, 6640], [61, 6720], [62, 6820], [65, 7000], 
    [66, 7040], [67, 7080], [69, 7190], [70, 7220], [72, 7340]
]

dados_10_5v = [
    [14, 3400], [21, 4150], [25, 4470], [30, 4700], [32, 4950], [36, 5190], 
    [39, 5450], [42, 5700], [45, 5820], [48, 6020], [50, 6200], [53, 6120], 
    [56, 6310], [58, 6600], [60, 6750], [62, 6820], [64, 7000], [66, 7100], 
    [68, 7150], [70, 7200], [71, 7330], [72, 7350], [74, 7400], [76, 7460], 
    [78, 7520]
]

dados_11v = [
    [14, 3300], [22, 3900], [26, 4560], [30, 4760], [34, 5020], [38, 5260], 
    [40, 5480], [43, 5720], [46, 5850], [50, 6060], [52, 6190], [54, 6360], 
    [56, 6500], [58, 6660], [60, 6720], [63, 6810], [65, 6920], [67, 7070], 
    [69, 7130], [70, 7210], [71, 7320], [72, 7400], [74, 7460], [77, 7530], 
    [78, 7620]
]

dados_11_5v = [
    [14, 3600], [21, 3910], [25, 4500], [30, 4820], [33, 5090], [37, 5320], 
    [40, 5530], [44, 5710], [46, 5940], [48, 6050], [52, 6270], [54, 6390], 
    [56, 6540], [58, 6680], [61, 6800], [64, 6920], [65, 7010], [66, 7110], 
    [68, 7200], [70, 7340], [71, 7380], [73, 7430], [75, 7480], [76, 7550], 
    [78, 7620]
]

dados_12v = [
    [15, 3600], [20, 4100], [24, 4400], [28, 4680], [32, 4900], [37, 5390], 
    [40, 5630], [42, 5890], [46, 6010], [48, 6210], [51, 6370], [54, 6490], 
    [56, 6600], [58, 6720], [60, 6840], [63, 6920], [65, 7020], [66, 7210], 
    [68, 7240], [70, 7260], [71, 7400], [74, 7430], [76, 7480], [78, 7630], 
    [79, 7660], [81, 7690], [82, 7710], [82, 7810]
]

# Dados de corrente organizados por tensão
# Formato: [corrente (A), peso (g), rpm]
dados_corrente_10v = [
    [0.2, 14, 3500], [0.25, 20, 4000], [0.3, 24, 4550], [0.35, 27, 4660], 
    [0.4, 32, 4910], [0.45, 36, 5200], [0.5, 38, 5400], [0.55, 41, 5610], 
    [0.6, 43, 5770], [0.65, 47, 5880], [0.7, 50, 6120], [0.75, 52, 6270], 
    [0.8, 54, 6440], [0.85, 57, 6600], [0.9, 59, 6640], [0.95, 61, 6720], 
    [1.0, 62, 6820], [1.05, 65, 7000], [1.1, 66, 7040], [1.15, 67, 7080], 
    [1.2, 69, 7190], [1.25, 70, 7220], [1.3, 72, 7340]
]

dados_corrente_10_5v = [
    [0.2, 14, 3400], [0.25, 21, 4150], [0.3, 25, 4470], [0.35, 30, 4700], 
    [0.4, 32, 4950], [0.45, 36, 5190], [0.5, 39, 5450], [0.55, 42, 5700], 
    [0.6, 45, 5820], [0.65, 48, 6020], [0.7, 50, 6200], [0.75, 53, 6120], 
    [0.8, 56, 6310], [0.85, 58, 6600], [0.9, 60, 6750], [0.95, 62, 6820], 
    [1.0, 64, 7000], [1.05, 66, 7100], [1.1, 68, 7150], [1.15, 70, 7200], 
    [1.2, 71, 7330], [1.25, 72, 7350], [1.3, 74, 7400], [1.35, 76, 7460], 
    [1.4, 78, 7520]
]

dados_corrente_11v = [
    [0.2, 14, 3300], [0.25, 22, 3900], [0.3, 26, 4560], [0.35, 30, 4760], 
    [0.4, 34, 5020], [0.45, 38, 5260], [0.5, 40, 5480], [0.55, 43, 5720], 
    [0.6, 46, 5850], [0.65, 50, 6060], [0.7, 52, 6190], [0.75, 54, 6360], 
    [0.8, 56, 6500], [0.85, 58, 6660], [0.9, 60, 6720], [0.95, 63, 6810], 
    [1.0, 65, 6920], [1.05, 67, 7070], [1.1, 69, 7130], [1.15, 70, 7210], 
    [1.2, 71, 7320], [1.25, 72, 7400], [1.3, 74, 7460], [1.35, 77, 7530], 
    [1.4, 78, 7620]
]

dados_corrente_11_5v = [
    [0.2, 14, 3600], [0.25, 21, 3910], [0.3, 25, 4500], [0.35, 30, 4820], 
    [0.4, 33, 5090], [0.45, 37, 5320], [0.5, 40, 5530], [0.55, 44, 5710], 
    [0.6, 46, 5940], [0.65, 48, 6050], [0.7, 52, 6270], [0.75, 54, 6390], 
    [0.8, 56, 6540], [0.85, 58, 6680], [0.9, 61, 6800], [0.95, 64, 6920], 
    [1.0, 65, 7010], [1.05, 66, 7110], [1.1, 68, 7200], [1.15, 70, 7340], 
    [1.2, 71, 7380], [1.25, 73, 7430], [1.3, 75, 7480], [1.35, 76, 7550], 
    [1.4, 78, 7620]
]

dados_corrente_12v = [
    [0.2, 15, 3600], [0.25, 20, 4100], [0.3, 24, 4400], [0.35, 28, 4680], 
    [0.4, 32, 4900], [0.45, 37, 5390], [0.5, 40, 5630], [0.55, 42, 5890], 
    [0.6, 46, 6010], [0.65, 48, 6210], [0.7, 51, 6370], [0.75, 54, 6490], 
    [0.8, 56, 6600], [0.85, 58, 6720], [0.9, 60, 6840], [0.95, 63, 6920], 
    [1.0, 65, 7020], [1.05, 66, 7210], [1.1, 68, 7240], [1.15, 70, 7260], 
    [1.2, 71, 7400], [1.25, 74, 7430], [1.3, 76, 7480], [1.35, 78, 7630], 
    [1.4, 79, 7660], [1.45, 81, 7690], [1.5, 82, 7710], [1.55, 82, 7810]
]

# Função para separar dados
def separar_dados(dados):
    pesos = [ponto[0] for ponto in dados]
    rpms = [ponto[1] for ponto in dados]
    return pesos, rpms

def separar_dados_corrente(dados):
    correntes = [ponto[0] for ponto in dados]
    pesos = [ponto[1] for ponto in dados]
    rpms = [ponto[2] for ponto in dados]
    return correntes, pesos, rpms

# Separar dados de peso x RPM
peso_10v, rpm_10v = separar_dados(dados_10v)
peso_10_5v, rpm_10_5v = separar_dados(dados_10_5v)
peso_11v, rpm_11v = separar_dados(dados_11v)
peso_11_5v, rpm_11_5v = separar_dados(dados_11_5v)
peso_12v, rpm_12v = separar_dados(dados_12v)

# Separar dados de corrente
corrente_10v, _, _ = separar_dados_corrente(dados_corrente_10v)
corrente_10_5v, _, _ = separar_dados_corrente(dados_corrente_10_5v)
corrente_11v, _, _ = separar_dados_corrente(dados_corrente_11v)
corrente_11_5v, _, _ = separar_dados_corrente(dados_corrente_11_5v)
corrente_12v, _, _ = separar_dados_corrente(dados_corrente_12v)

# GRÁFICO 1: Peso vs RPM (original)
plt.figure(figsize=(12, 8))

plt.plot(rpm_10v, peso_10v, 'o-', color='blue', label='10V', linewidth=2, markersize=6)
plt.plot(rpm_10_5v, peso_10_5v, 's-', color='green', label='10.5V', linewidth=2, markersize=6)
plt.plot(rpm_11v, peso_11v, '^-', color='red', label='11V', linewidth=2, markersize=6)
plt.plot(rpm_11_5v, peso_11_5v, 'd-', color='orange', label='11.5V', linewidth=2, markersize=6)
plt.plot(rpm_12v, peso_12v, 'v-', color='purple', label='12V', linewidth=2, markersize=6)

plt.xlabel('RPM', fontsize=14, fontweight='bold')
plt.ylabel('Peso (g)', fontsize=14, fontweight='bold')
plt.title('Relação Peso vs RPM por Tensão', fontsize=16, fontweight='bold')
plt.grid(True, alpha=0.3, linestyle='--')
plt.legend(fontsize=12, loc='lower right')
plt.xlim(3000, 8000)
plt.ylim(10, 85)

plt.tight_layout()
plt.show()

# GRÁFICO 2: Peso vs Corrente
plt.figure(figsize=(12, 8))

# Extrair pesos para cada corrente
_, peso_corrente_10v, _ = separar_dados_corrente(dados_corrente_10v)
_, peso_corrente_10_5v, _ = separar_dados_corrente(dados_corrente_10_5v)
_, peso_corrente_11v, _ = separar_dados_corrente(dados_corrente_11v)
_, peso_corrente_11_5v, _ = separar_dados_corrente(dados_corrente_11_5v)
_, peso_corrente_12v, _ = separar_dados_corrente(dados_corrente_12v)

plt.plot(corrente_10v, peso_corrente_10v, 'o-', color='blue', label='10V', linewidth=2, markersize=6)
plt.plot(corrente_10_5v, peso_corrente_10_5v, 's-', color='green', label='10.5V', linewidth=2, markersize=6)
plt.plot(corrente_11v, peso_corrente_11v, '^-', color='red', label='11V', linewidth=2, markersize=6)
plt.plot(corrente_11_5v, peso_corrente_11_5v, 'd-', color='orange', label='11.5V', linewidth=2, markersize=6)
plt.plot(corrente_12v, peso_corrente_12v, 'v-', color='purple', label='12V', linewidth=2, markersize=6)

plt.xlabel('Corrente (A)', fontsize=14, fontweight='bold')
plt.ylabel('Peso (g)', fontsize=14, fontweight='bold')
plt.title('Relação Peso vs Corrente por Tensão', fontsize=16, fontweight='bold')
plt.grid(True, alpha=0.3, linestyle='--')
plt.legend(fontsize=12, loc='lower right')
plt.xlim(0, 1.8)
plt.ylim(10, 85)

plt.tight_layout()
plt.show()

# GRÁFICO 3: Corrente vs RPM
plt.figure(figsize=(12, 8))

# Extrair RPMs para cada corrente
_, _, rpm_corrente_10v = separar_dados_corrente(dados_corrente_10v)
_, _, rpm_corrente_10_5v = separar_dados_corrente(dados_corrente_10_5v)
_, _, rpm_corrente_11v = separar_dados_corrente(dados_corrente_11v)
_, _, rpm_corrente_11_5v = separar_dados_corrente(dados_corrente_11_5v)
_, _, rpm_corrente_12v = separar_dados_corrente(dados_corrente_12v)

plt.plot(corrente_10v, rpm_corrente_10v, 'o-', color='blue', label='10V', linewidth=2, markersize=6)
plt.plot(corrente_10_5v, rpm_corrente_10_5v, 's-', color='green', label='10.5V', linewidth=2, markersize=6)
plt.plot(corrente_11v, rpm_corrente_11v, '^-', color='red', label='11V', linewidth=2, markersize=6)
plt.plot(corrente_11_5v, rpm_corrente_11_5v, 'd-', color='orange', label='11.5V', linewidth=2, markersize=6)
plt.plot(corrente_12v, rpm_corrente_12v, 'v-', color='purple', label='12V', linewidth=2, markersize=6)

plt.xlabel('Corrente (A)', fontsize=14, fontweight='bold')
plt.ylabel('RPM', fontsize=14, fontweight='bold')
plt.title('Relação Corrente vs RPM por Tensão', fontsize=16, fontweight='bold')
plt.grid(True, alpha=0.3, linestyle='--')
plt.legend(fontsize=12, loc='lower right')
plt.xlim(0, 1.8)
plt.ylim(3000, 8000)

plt.tight_layout()
plt.show()

# ANÁLISE ESTATÍSTICA EXPANDIDA
print("\n=== ANÁLISE ESTATÍSTICA EXPANDIDA ===")
tensoes_nome = ["10V", "10.5V", "11V", "11.5V", "12V"]
todos_dados = [dados_10v, dados_10_5v, dados_11v, dados_11_5v, dados_12v]
todos_dados_corrente = [dados_corrente_10v, dados_corrente_10_5v, dados_corrente_11v, dados_corrente_11_5v, dados_corrente_12v]

for i, (nome, dados, dados_corrente) in enumerate(zip(tensoes_nome, todos_dados, todos_dados_corrente)):
    pesos = [d[0] for d in dados]
    rpms = [d[1] for d in dados]
    correntes = [d[0] for d in dados_corrente]
    
    print(f"\n{nome}:")
    print(f"  Peso mínimo: {min(pesos)}g")
    print(f"  Peso máximo: {max(pesos)}g")
    print(f"  RPM mínimo: {min(rpms)} RPM")
    print(f"  RPM máximo: {max(rpms)} RPM")
    print(f"  Corrente mínima: {min(correntes):.2f}A")
    print(f"  Corrente máxima: {max(correntes):.2f}A")
    print(f"  Eficiência (RPM/g no ponto máximo): {max(rpms)/max(pesos):.1f}")
    print(f"  Eficiência (RPM/A no ponto máximo): {max(rpms)/max(correntes):.1f}")
    print(f"  Pontos de dados: {len(dados)}")

# Análise de eficiência energética
print("\n=== ANÁLISE DE EFICIÊNCIA ENERGÉTICA ===")
for i, (nome, dados_corrente) in enumerate(zip(tensoes_nome, todos_dados_corrente)):
    tensao = float(nome.replace('V', ''))
    corrente_max = max([d[0] for d in dados_corrente])
    rpm_max = max([d[2] for d in dados_corrente])
    potencia_max = tensao * corrente_max
    
    print(f"\n{nome}:")
    print(f"  Potência máxima: {potencia_max:.2f}W")
    print(f"  Eficiência (RPM/W): {rpm_max/potencia_max:.1f}")