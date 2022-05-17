from wordcloud import WordCloud, STOPWORDS
import  matplotlib.pyplot as plt
from PIL import Image
import numpy as np

#텍스트 파일 열기
text = open('./data/usa_president_message.txt', encoding='UTF-8').read()

#이미지 마스킹 처리
image_path = './data/usa_map.jpg'
usa_map = np.array(Image.open(image_path))

#워드클라우드 이미지 생성
wordcloud = WordCloud(background_color='white',
                    max_font_size = 100,
                    max_words = 1000,
                    stopwords = STOPWORDS,
                    mask = usa_map).generate(text)  
#화면에 출력
fig = plt.figure(figsize=(15,15))
plt.imshow(wordcloud, interpolation = 'bilinear') #interpolation = 'bilinear': 이미지 부드럽기 정도
plt.axis("off") #axis: x,y좌표

plt.savefig('./output/usa_president_massage_wordcloud_map02.svg')


