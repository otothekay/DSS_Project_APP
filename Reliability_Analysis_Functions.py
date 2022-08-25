import random
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def network_degradation_test(network, survivability, days):
    """
    This is a helper function used during the implimentation of the 'average_network_durability' function. This function
    iteratively 'degrades' a network through the removal of sensors (nodes) based on a discrete time step survival probability.
    The function stops when there is either a single sensor left in the network, the network becomes disconnected, or the
    function has iterated through each day as specified as an input; which ever occurrence happens first. This is highly
    dependent on the type of type of network constructed, the sensor survivability rate, and the number of days the network
    degrades.

    For example, if the original (non-degraded) network is fully-connected, then the function can only stop once
    all but one sensor remains, or there are no longer any days to potentially degrade over.

    Another example; if the origninal (non-degraded) network is constructed and already disconnected, the function will stop
    at the first iteration.


    Input:
        network(nx.Graph object): The network object that the user has previously created, regardless of network
        construction method.

        survibability(int with range (0-100)): Represents the survival rate for a single sensor (node) per day (time step).

        days(positive int): Represents the maximum number of days (time-steps) the network will be degraded.

    Returns:
        end(int): Represents the last 't' (day) the function iterated over. This typically equals the time step when the
        network changes from connected to disconnected, however this can also represent the time step when only one node
        remains in the network, or the final time step if the network remained connected through each iteration of
        degradation.

    """
    H = network

    for t in range(1, days + 1):
        if nx.is_connected(H) == True:

            if len(H.nodes) > 1:
                for i in set(H.nodes):
                    Fails = 100 - int(survivability)
                    RandomNum = random.randint(1, 100)
                    if RandomNum > Fails:
                        pass
                    if RandomNum <= Fails:
                        new_nodes = H.remove_node(i)
                        for j in H.nodes:
                            if (i, j) in H.edges:
                                new_edges = H.remove_edge(i, j)
                                H.update(edges=new_edges, nodes=new_nodes)
            if len(H.nodes) <= 1:
                break

        if nx.is_connected(H) == False:
            break
    end = t

    return end


def average_network_durability(network, survivability, days, replications):
    """
    This function replicates the network_degradation_test over a set number of replications in order to provide the user
    with the average number of days until the network becomes disconnected (fails). The user is also provided a histogram
    for the results of the replications, as well as the prediction interval for 95% of replications.


    Inputs:
        network(nx.Graph object): See network_degradation_test docstring

        survibability(int with range (0-100)): See network_degradation_test docstring

        days(positive int): See network_degradation_test docstring

        replications(positive int): The number of times the network_degradation_test function will be applied to the
        given network with its associated sensor survivability rate and number of days it can be degraded.

    Returns:
        mean(float): The average time step (day) the network becomes disconnected.

        lb(float): The lower bound of a 95% prediction interval.

        ub(float): The upper bound of a 95% prediction interval.

        plot: The histogram displaying the results of the function, placing each network_degradation_test results into
        a bin. A 'kde' (Kernal Density Estimate) distribution curve is also provided.

    """
    N = network
    S = survivability
    D = days
    R = replications

    ave_fail_day = []

    original_network = network.copy()
    for r in range(1, R + 1):  # replications
        ave_fail_day.append(network_degradation_test(N.copy(), S, D))
        N = original_network

    mean = np.mean(ave_fail_day)
    lb = max(np.mean(ave_fail_day) - 1.96 * (np.std(ave_fail_day)), 0)
    ub = min(np.mean(ave_fail_day) + 1.96 * (np.std(ave_fail_day)), days)
    plot = sns.histplot(data=ave_fail_day, x=ave_fail_day, y=None, hue=None, weights=None, stat='count', bins='auto',
                        binwidth=1, binrange=None, discrete=None,
                        cumulative=False, common_bins=True, common_norm=True, multiple='layer', element='bars',
                        fill=True, shrink=1, kde=True, kde_kws=None,
                        line_kws=None, thresh=0, pthresh=None, pmax=None, cbar=False, cbar_ax=None, cbar_kws=None,
                        palette=None, hue_order=None,
                        hue_norm=None, color=None, log_scale=None, legend=True, ax=None).set(
        title='Failure Distribution', xlabel='Time to Failure(Days)', ylabel='Number of Runs')
    plt.grid(visible=True, which='major', axis='y')

    figs = plt.gcf()

    return mean, lb, ub, figs


print("Reliability Analysis Functions are Uploaded")