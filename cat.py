from IPython.display import Image
from urllib.request import urlopen

url = "https://cdn.pixabay.com/photo/2016/02/10/16/37/cat-1192026_960_720.jpg"
image = Image(urlopen(url).read())
display(image)

//ㅁㄴㅇㄹ