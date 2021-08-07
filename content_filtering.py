from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas

articles = pandas.read_csv('data/articles_data.csv')
articles = articles[articles['title'].notna()]

count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(articles['title'])

cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

articles = articles.reset_index()
indices = pandas.Series(articles.index, index=articles['contentId'])


def get_recommendations(contentId):
    idx = indices[int(contentId)]
    sim_scores = list(enumerate(cosine_sim2[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    article_indices = [i[0] for i in sim_scores]
    return articles[["url", "title", "text", "lang", "total_events"]].iloc[article_indices].values.tolist()
