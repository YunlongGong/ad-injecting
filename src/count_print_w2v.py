# -*- coding:utf-8 -*-


from get_data import *
from ad import *
import jieba.analyse
import gensim.models.doc2vec
from scipy import spatial
import numpy as np


def count_print_w2v(url):
    top_k_article_initial = 20
    top_k_article = 8
    top_k_ad_initial = 5
    top_k_ad = 3
    model = gensim.models.Word2Vec.load('C:\Project\Python\model\word2vec_from_weixin\word2vec_wx')
    article_content = get_data(url)
    article_vec = get_mean_vec(model, article_content, top_k_article_initial, top_k_article)
    article_ad_dist = []
    for ad_i in ad:
        ad_i_vec = get_mean_vec(model, ad_i, top_k_ad_initial, top_k_ad)
        cos_dist_i = 1 - spatial.distance.cosine(ad_i_vec, article_vec)
        article_ad_dist.append((cos_dist_i, ad_i))
    article_ad_dist = sorted(article_ad_dist, key = lambda article_ad_dist : article_ad_dist[0], reverse=True)
    row_length = 80
    column_index_list = list(range(1, (int(len(article_content) / row_length) + 2)))
    print('-' * 150)
    print("url: " + url)
    print('-' * 150)
    for i in column_index_list:
        print(article_content[(i - 1) * row_length : i * row_length])
    print('-' * 150)
    for i in article_ad_dist:
        print(i)


def get_mean_vec(model, sentence, top_k_initial, top_k):
    tags_raw = jieba.analyse.extract_tags(sentence, topK=top_k_initial, withWeight=False, allowPOS=())
    tags = []
    tags_list = []
    for i in tags_raw:
        if i in model:
            tags.append(i)
            tags_list.append(model[i])
        if len(tags) == top_k:
            break
    tags_array = np.array(tags_list)
    vec = np.mean(tags_array, axis=0)
    return vec