import numpy as np
import matplotlib.pyplot as plt


def show_plots(data, nb):
    data_tmp = data[data['price'] < nb]
    count, bins_count = np.histogram(data_tmp['price'], bins=100)

    # finding the PDF of the histogram using count values
    pdf = count / sum(count)

    # using numpy np.cumsum to calculate the CDF
    # We can also find using the PDF values by looping and adding

    cdf = np.cumsum(pdf)

    # plotting PDF and CDF
    plt.plot(bins_count[1:], pdf, color="red", label="PDF")
    plt.plot(bins_count[1:], cdf, label="CDF")
    plt.legend()
    plt.show()