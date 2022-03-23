from matplotlib import pyplot as plt


def laptime_over_race_plot(race, driver1, driver1_color, driver2, driver2_color, plot_title):
    driver1_ = race.laps.pick_driver(driver1)
    driver2_ = race.laps.pick_driver(driver2)

    fig, ax = plt.subplots()
    ax.plot(driver1_['LapNumber'], driver1_['LapTime'], driver1_color)
    ax.plot(driver2_['LapNumber'], driver2_['LapTime'], driver2_color)
    ax.set_title(plot_title)
    ax.set_xlabel("Lap Number")
    ax.set_ylabel("Lap Time")
    plt.show()


def speed_over_lap_plot(session, driver1, driver1_color, driver2, driver2_color, plot_title):
    driver1_fastest = session.laps.pick_driver(driver1).pick_fastest()
    driver1_car_data = driver1_fastest.get_car_data()
    driver2_fastest = session.laps.pick_driver(driver2).pick_fastest()
    driver2_car_data = driver2_fastest.get_car_data()
    driver1_time = driver1_car_data['Time']
    driver1_speed = driver1_car_data['Speed']
    driver2_time = driver2_car_data['Time']
    driver2_speed = driver2_car_data['Speed']

    fig, ax = plt.subplots()
    ax.plot(driver1_time, driver1_speed, driver1_color)
    ax.plot(driver2_time, driver2_speed, driver2_color)
    ax.set_title(plot_title)
    ax.set_xlabel("Time")
    ax.set_ylabel("Speed [Km/h]")
    ax.legend()
    plt.show()


def lap_telemetry_plot(plot_title, session, driver1, driver1_color, driver2=None, driver2_color=None):
    driver1_fastest_lap = session.laps.pick_driver(driver1).pick_fastest()
    driver1_car_data = driver1_fastest_lap.get_car_data()
    driver1_time = driver1_car_data['Time']
    driver1_throttle = driver1_car_data['Throttle']
    driver1_brake = driver1_car_data['Brake'] * 100

    if driver2:
        driver2_fastest_lap = session.laps.pick_driver(driver2).pick_fastest()
        driver2_car_data = driver2_fastest_lap.get_car_data()
        driver2_time = driver2_car_data['Time']
        driver2_throttle = driver2_car_data['Throttle']
        driver2_brake = driver2_car_data['Brake'] * 100
        driver1_throttle_color = driver1_color
        driver1_brake_color = driver1_color
    else:
        driver1_throttle_color = "green"
        driver1_brake_color = "red"

    fig, axs = plt.subplots(2)
    axs[0].plot(driver1_time, driver1_throttle, driver1_throttle_color)
    axs[1].plot(driver1_time, driver1_brake, driver1_brake_color)

    if driver2:
        axs[0].plot(driver2_time, driver2_throttle, driver2_color)
        axs[1].plot(driver2_time, driver2_brake, driver2_color)

    axs[0].set_title(plot_title)
    axs[1].set_xlabel("Time")
    axs[0].set_ylabel("%")
    axs[1].set_ylabel("%")
    plt.show()

