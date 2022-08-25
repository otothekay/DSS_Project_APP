import networkx as nx
import matplotlib.pyplot as plt


def text_report(G):
    """
    Generates the Network Statistics Report

    Inputs:
        G(nx.Graph() Object):  The graph about which to report statistics

    Returns:
        Figs (matplotlib.figure) : The figure to be drawn to the GUI as the report
    """
    fig, ax = plt.subplots()
    fig.text(0.15, .8, 'REPORT')
    fig.text(0.15, .6, f'You successfully launched and connected {G.order()} sensors')
    fig.text(0.15, .5, f'Your network has {G.size()} sensor connections')
    fig.text(0.15, .4, f'Your network average sensor connections is {round(2 * G.size() / G.order(), 3)}')
    fig.text(0.15, .3, f'Is your network Fully Connected? : {G.order() * (G.order() - 1) / 2 == G.size()}')
    fig.text(0.15, .2, f'Is your network Connected? : {nx.is_connected(G)}')

    ax.tick_params(bottom=False, left=False, right=False, top=False)
    ax.set_xticks([])
    ax.set_xticklabels([])
    ax.set_yticks([])
    ax.set_yticklabels([])

    figs = plt.gcf()

    return figs


def text_report_reliability(G, mean, lb, ub):
    """
    Generates the Network Statistics Report

    Inputs:
        G(nx.Graph() Object):  The graph about which to report statistics
        mean (float): the average day that network failure was achieved.
        lb (float): The lower bound of the prediction interval for network failure.
        ub (float): The upper bound of the prediction interval for network failure.

    Returns:
        Figs(matplotlib.figure): The figure to be drawn to the GUI as the report
    """
    mean = mean
    lb = lb
    ub = ub

    fig, ax = plt.subplots()
    fig.text(0.15, .8, 'REPORT')
    fig.text(0.15, .6, f'Average time unitl network failure (disconnectivity): {round(mean, 3)} days')
    fig.text(0.15, .5, f'Pred Interval for 95% of Networks - Lower Bound: {round(lb, 3)} days')
    fig.text(0.15, .4, f'Pred Interval for 95% of Networks - Upper Bound: {round(ub, 3)} days')

    ax.tick_params(bottom=False, left=False, right=False, top=False)
    ax.set_xticks([])
    ax.set_xticklabels([])
    ax.set_yticks([])
    ax.set_yticklabels([])

    figs = plt.gcf()

    return figs


print("Text Report Scripts uploaded successfully")
