import requests
import base64
import argparse

def gerar_e_baixar_imagem(prompt, caminho_arquivo='imagem.png', width=512, height=512):
    url = 'http://192.168.3.70:7861/sdapi/v1/txt2img'
    payload = {
        "prompt": prompt,
        "steps": 20,
        "width": width,
        "height": height
    }
    resposta = requests.post(url, json=payload)
    resposta.raise_for_status()
    resultado = resposta.json()
    # A imagem vem em base64
    imagem_base64 = resultado['images'][0]
    imagem_bytes = base64.b64decode(imagem_base64)
    with open(caminho_arquivo, 'wb') as f:
        f.write(imagem_bytes)
    print(f"Imagem salva em {caminho_arquivo}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gere e baixe uma imagem do Stable Diffusion.")
    parser.add_argument('--prompt', type=str, required=True, help='Prompt para a imagem')
    parser.add_argument('--output', type=str, default='imagem.png', help='Caminho do arquivo de saída')
    parser.add_argument('--width', type=int, default=512, help='Largura da imagem')
    parser.add_argument('--height', type=int, default=512, help='Altura da imagem')
    args = parser.parse_args()

    gerar_e_baixar_imagem(
        prompt=args.prompt,
        caminho_arquivo=args.output,
        width=args.width,
        height=args.height
    )
