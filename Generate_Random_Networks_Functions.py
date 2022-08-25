import random
import networkx as nx
import numpy
import matplotlib.pyplot as plt
import math


def generate_network_from_two_points(left_point, right_point, connection_radius,
                                     deployment_rate=3, max_num_sensors=100, aircraft_speed=300):
    """Using input parameters, generates a random distribution of sensors between two
        geographic points that simulates an aircraft-based pass. Nodes are generated
        based on number of sensors deployed, and arcs are created based on connection
        radius between sensors.This function uses matplotlib to plot the raw data
        geographically, and provides an additional plot of the data showing the arcs
        created. Requires importation of NetworkX as nx, matplotlib.pyplot as plt,
        random, math, and numpy. This function can only model paths from left to
        right. If right to left required, generate pass and then transform.

        Args:
        left_point(list[X,Y]): Coordinate to begin pass at.
        right_point(list[X,Y]): Coordinate to end pass at.
        connection_radius(int): The radius around each node in which it will form arcs with
            surrounding nodes.
        deployment_rate(int): The average rate of sensors deployed per minute. Default of 3.
        max_num_sensors(int): The maximum number of sensors to deploy. Default of 100.
        aircraft_speed(int): Aircraft speed in kph. Default of 300.

        Returns:
        G(nx.Graph object)
        X(List): X coordinates
        Y(List): Y coordinates
    """
    # This block initializes the path based on inputs
    slope = (right_point[1] - left_point[1]) / (right_point[0] - left_point[0])  # angle of flight path from start point
    time = math.sqrt((right_point[1] - left_point[1]) ** 2 + (
                right_point[0] - left_point[0]) ** 2) / aircraft_speed  # Distance/Speed
    deployment_start_point = left_point
    total_times = 0
    sensors_deployed = 0
    left_angle = math.atan(slope) + .5 * math.pi
    right_angle = math.atan(slope) + 1.5 * math.pi
    angles = [left_angle, right_angle]
    aircraft_X = [deployment_start_point[0]]
    aircraft_Y = [deployment_start_point[1]]
    sensor_X_coords = []
    sensor_Y_coords = []

    # This block simulates the pass itself and deploys sensors along the path based on inter-deployment time
    while sensors_deployed < max_num_sensors:
        inter_time = random.expovariate(deployment_rate)
        if (sensors_deployed) >= max_num_sensors:  # Checks if max number has been reached
            break
        if slope > 0:
            if (aircraft_X[-1] >= right_point[0]) or (aircraft_Y[-1] >= right_point[1]):  # Checks if end point passed
                break
        if slope < 0:
            if (aircraft_X[-1] >= right_point[0]) or (aircraft_Y[-1] <= right_point[1]):  # Checks if end point passed
                break
        total_times += inter_time
        sensors_deployed += 1
        angle = math.atan(abs(slope))
        change_in_aircraft_X = (aircraft_speed / 60) * inter_time * math.cos(angle)
        change_in_aircraft_Y = (slope * change_in_aircraft_X)
        aircraft_X.append(aircraft_X[-1] + change_in_aircraft_X)
        aircraft_Y.append(aircraft_Y[-1] + change_in_aircraft_Y)
        sensor_launch_magnitude = numpy.random.exponential(8)  # Arbitrary distribution for magnitudes
        launch_angle = random.choice(angles)
        sensor_X = sensor_launch_magnitude * math.cos(launch_angle) + aircraft_X[-1]
        sensor_Y = sensor_launch_magnitude * math.sin(launch_angle) + aircraft_Y[-1]
        sensor_X_coords.append(sensor_X)
        sensor_Y_coords.append(sensor_Y)

    # This block creates the two plots and graph object using the coordinate lists and aircraft path
    print('Total sensors deployed: ', sensors_deployed)
    fig, axes = plt.subplots(1, 2)

    axes[0].plot(aircraft_X, aircraft_Y, color='black', linestyle='dashed', zorder=1)

    G = nx.Graph()

    # This block creates and adds arcs based on connection radius
    G.add_nodes_from(range(len(sensor_X_coords)))
    for i in range(len(sensor_X_coords)):
        for j in range(len(sensor_X_coords)):
            if (math.sqrt((sensor_X_coords[i] - sensor_X_coords[j]) ** 2 + (
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


def generate_center_out_network(nodes, connection_radius, origin=(0, 0)):
    """Using input parameters, generates a random distribution of sensors at one
        geographic point that simulates a center-out distribution. Nodes are generated
        based on number of sensors deployed, and arcs are created based on connection
        radius between sensors.This function uses matplotlib to plot the raw data
        geographically, and provides an additional plot of the data showing the arcs
        created. Requires importation of NetworkX as nx, matplotlib.pyplot as plt,
        random, math, and numpy.

        Args:
        nodes(int): The number of nodes to distribute
        connection_radius(int): The radius around each node in which it will form arcs with
            surrounding nodes.

        Returns:
        G(nx.Graph object)
        X(List): X coordinates
        Y(List): Y coordinates
    """
    # This block generates coordinate lists
    sensor_X_coords = []
    sensor_Y_coords = []
    for i in range(nodes):
        random_angle = 2 * math.pi * random.random()
        launch_distance = numpy.random.exponential(5)  # Arbitrary distribution
        x_coord = launch_distance * math.cos(random_angle) + origin[0]
        y_coord = launch_distance * math.sin(random_angle) + origin[1]
        sensor_X_coords.append(x_coord)
        sensor_Y_coords.append(y_coord)

    # This block initializes plots and graph object using coordinate lists
    print('Total sensors deployed: ', len(sensor_X_coords))
    fig, axes = plt.subplots(1, 2)

    G = nx.Graph()
    G.add_nodes_from(range(len(sensor_X_coords)))

    # This block creates and adds arcs based on connection radius
    for i in range(len(sensor_X_coords)):
        for j in range(len(sensor_X_coords)):
            if (math.sqrt((sensor_X_coords[i] - sensor_X_coords[j]) ** 2 + (
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



print("Generate Random Networks Functions are Uploaded")