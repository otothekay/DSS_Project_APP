import networkx as nx
import math
import csv
import matplotlib.pyplot as plt

def network_from_xy_csv(input_filename ,connection_radius):
    """Using input_filename as the input, returns a NetworkX graph object G,
        as well as the lists of coordinates (one featuring all X values, the other featuring Y).
        Nodes are generated based on the number of points, and arcs are generated based on the
        connection radius of nodes. Any nodes that do not connect to the main body are dropped.
        This function uses matplotlib to plot the raw data geographically, and provides an
        additional plot of the data showing the arcs created. Requires importation of NetworkX
        as nx, matplotlib.pyplot as plt, and csv.

        Args:
        input_filename(CSV): The file to access the X and Y coordinates from. CSV file should
            be structured as follows:
            "x","y",
            x[0],y[0],
            x[1],y[1],
            .
            .
            .
        connection_radius(int): The radius around each node in which it will form arcs with
            surrounding nodes.

        Returns:
        G(nx.Graph object)
        X(List): X coordinates
        Y(List): Y coordinates
    """
    # This block creates X and Y coordinate lists by interpreting the CSV file.
    sensor_X_coords = []
    sensor_Y_coords = []
    with open(input_filename) as f:
        inreader = csv.reader(f)
        inreader = list(inreader)
        with open(input_filename) as f:
            inreader = csv.reader(f)
            inreader = list(inreader)
            if 'x' in inreader[0]:
                x_index = inreader[0].index('x')
            if 'X' in inreader[0]:
                x_index = inreader[0].index('X')
            if 'y' in inreader[0]:
                y_index = inreader[0].index('y')
            if 'Y' in inreader[0]:
                y_index = inreader[0].index('Y')
            for line in range(1 ,len(inreader)):
                sensor_X_coords.append(float(inreader[line][x_index]))
                sensor_Y_coords.append(float(inreader[line][y_index]))

    # This block creates the two plots and initializes graph object using the coordinate lists.
    print('Total sensors deployed: ' ,len(sensor_X_coords))
    fig, axes = plt.subplots(1 ,2)

    G = nx.Graph()
    G.add_nodes_from(range(len(sensor_X_coords)))

    # This block creates and adds arcs based on connection radius
    for i in range(len(sensor_X_coords)):
        for j in range(len(sensor_X_coords)):
            if (math.sqrt((sensor_X_coords[i ]- sensor_X_coords[j]) ** 2 + (
                    sensor_Y_coords[i] - sensor_Y_coords[j]) ** 2)) <= connection_radius and (i != j):
                G.add_edge(i, j)
                line_start = [sensor_X_coords[i], sensor_X_coords[j]]
                line_end = [sensor_Y_coords[i], sensor_Y_coords[j]]
                axes[1].plot(line_start, line_end, color='gray', linestyle='dashed', zorder=1)

    # This block drops any nodes that are unconnected(have a degree of 0)
    for i in list(G.nodes):
        if G.degree(i) == 0:
            j = list(G.nodes).index(i)
            G.remove_node(i)
            del sensor_X_coords[j]
            del sensor_Y_coords[j]
    print('Surviving Nodes: ', len(list(G.nodes)))

    axes[0].scatter(sensor_X_coords, sensor_Y_coords, zorder=2)
    axes[1].scatter(sensor_X_coords, sensor_Y_coords, zorder=2)
    axes[0].set_title('Initial Plot of Sensors')
    axes[0].set_ylabel('Y')
    axes[0].set_xlabel('X')
    axes[1].set_title('Sensors Connected')
    axes[1].set_ylabel('Y')
    axes[1].set_xlabel('X')
    fig.tight_layout()

    figs = plt.gcf()  # added this to extract the figure out of this function

    return G, sensor_X_coords, sensor_Y_coords, figs  # added figs to the return of this function

if __name__ == "__main__":
    print("CSV in_reader is loaded successfully")

else:
    pass
