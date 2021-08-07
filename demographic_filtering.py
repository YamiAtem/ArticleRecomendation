import pandas

articles = pandas.read_csv('data/articles_data.csv')

articles = articles.sort_values(['total_events'], ascending=[False])

output = articles[["url", "title", "text", "lang", "total_events"]].head(20).values.tolist()