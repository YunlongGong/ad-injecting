# -*- coding:utf-8 -*-


from get_data import *
from ad import *
import gensim.models.doc2vec
from scipy import spatial


def count_print_d2v(url):
    model = gensim.models.Doc2Vec.load('C:\Project\Python\model\model_doc2vec\corpus.zhwiki.doc.model')
    article_content = get_data(url)
    article_vec = model.infer_vector(article_content)
    article_ad_dist = []
    for ad_i in ad:
        ad_i_vec = model.infer_vector(ad_i)
        cos_dist_i = 1 - spatial.distance.cosine(article_vec, ad_i_vec)
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