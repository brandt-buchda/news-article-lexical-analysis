from lib import constants
from lib.parsehtlm import ParseHtml
from lib.serialize import CsvSerialize
import analyzedata
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats as stats

def main():

    csv_serialize = CsvSerialize(constants.Newspapers.NEW_YORK_TIMES, constants.Paths.CSV_DIRECTORY)

    articles = csv_serialize.load_all_article_data()

    data = analyzedata.compute_flesh_reading_score(articles)

    # Set a color palette for the years
    palette = sns.color_palette("husl", n_colors=len(data['year'].unique()))

    plt.figure(figsize=(12, 6))
    sns.boxplot(x='year', y='flesch_score', data=data, palette=palette)

    plt.title('Flesch Reading Ease Score Over the Years (Box Plot)')
    plt.xlabel('Year')
    plt.ylabel('Flesch Reading Score')
    plt.xticks(rotation=45)
    plt.ylim(0, 100)
    plt.show()

if __name__ == '__main__':
    main()
