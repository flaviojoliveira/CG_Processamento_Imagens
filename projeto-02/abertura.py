from PIL import Image
#from utils import in_file
import os

# abrindo nossa imagem
image = Image.open("data/input/bandeira.jpeg")

# exibir a imagem
image.show()

docker run -d -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce