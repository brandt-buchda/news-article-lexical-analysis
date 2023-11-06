from lib import constants
from lib.utility import split_date
from lib.serialize import CsvSerialize
import analyzedata
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    csv_serialize = CsvSerialize(constants.Newspapers.NEW_YORK_TIMES, constants.Paths.CSV_DIRECTORY)

    articles = csv_serialize.load_all_article_data()
    filtered_articles = [a for a in articles if int(split_date(a.get_href())[0:4]) % 5 == 0]
    data = analyzedata.compute_flesh_reading_score(filtered_articles)

    palette = sns.color_palette(palette="flare")

    plt.figure(figsize=(12, 6))
    sns.boxplot(x='year', y='flesch_score', data=data, palette=palette, hue='year', legend=False)

    plt.title('New York Times Flesch Reading Score 1985 to 2020 ')
    plt.xlabel('Year')
    plt.ylabel('Flesch Reading Score')
    plt.xticks(rotation=45)
    plt.ylim(0, 100)
    plt.show()


if __name__ == '__main__':
    main()
