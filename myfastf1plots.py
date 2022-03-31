from matplotlib import pyplot as plt


class MyFastF1Plots:
    def laptime_plot(self, session, driver1, driver1_color, driver2=None, driver2_color=None, plot_title=None):
        driver1_ = session.laps.pick_driver(driver1)

        fig, ax = plt.subplots()
        ax.plot(driver1_['LapNumber'], driver1_['LapTime'], driver1_color)

        if driver2:
            driver2_ = session.laps.pick_driver(driver2)
            ax.plot(driver2_['LapNumber'], driver2_['LapTime'], driver2_color)

        if not plot_title:
            plot_title = driver1

        if driver2 and plot_title == driver1:
            plot_title = plot_title + " vs " + driver2

        ax.set_title(plot_title)
        ax.set_xlabel("Lap Number")
        ax.set_ylabel("Lap Time")

    def speed_plot(self, session, driver1, driver1_color, driver2=None, driver2_color=None, plot_title=None):
        driver1_fastest = session.laps.pick_driver(driver1).pick_fastest()
        driver1_car_data = driver1_fastest.get_car_data()
        driver1_time = driver1_car_data['Time']
        driver1_speed = driver1_car_data['Speed']

        fig, ax = plt.subplots()
        ax.plot(driver1_time, driver1_speed, driver1_color)

        if driver2:
            driver2_fastest = session.laps.pick_driver(driver2).pick_fastest()
            driver2_car_data = driver2_fastest.get_car_data()
            driver2_time = driver2_car_data['Time']
            driver2_speed = driver2_car_data['Speed']
            ax.plot(driver2_time, driver2_speed, driver2_color)

        if not plot_title:
            plot_title = driver1

        if driver2 and plot_title == driver1:
            plot_title = plot_title + " vs " + driver2

        ax.set_title(plot_title)
        ax.set_xlabel("Time")
        ax.set_ylabel("Speed [Km/h]")
        ax.legend()

    def telemetry_plot(self, session, driver1, driver1_color, driver2=None, driver2_color=None, plot_title=None):
        driver1_fastest_lap = session.laps.pick_driver(driver1).pick_fastest()
        driver1_car_data = driver1_fastest_lap.get_car_data()
        driver1_time = driver1_car_data['Time']
        driver1_speed = driver1_car_data['Speed']
        driver1_throttle = driver1_car_data['Throttle']
        driver1_brake = driver1_car_data['Brake'] * 100

        if not driver2:
            driver1_throttle_color = "green"
            driver1_brake_color = "red"
        else:
            driver1_throttle_color = driver1_color
            driver1_brake_color = driver1_color

        fig, axs = plt.subplots(3)
        axs[0].plot(driver1_time, driver1_speed, driver1_color)
        axs[1].plot(driver1_time, driver1_throttle, driver1_throttle_color)
        axs[2].plot(driver1_time, driver1_brake, driver1_brake_color)

        if driver2:
            driver2_fastest_lap = session.laps.pick_driver(driver2).pick_fastest()
            driver2_car_data = driver2_fastest_lap.get_car_data()
            driver2_time = driver2_car_data['Time']
            driver2_speed = driver2_car_data['Speed']
            driver2_throttle = driver2_car_data['Throttle']
            driver2_brake = driver2_car_data['Brake'] * 100
            axs[0].plot(driver2_time, driver2_speed, driver2_color)
            axs[1].plot(driver2_time, driver2_throttle, driver2_color)
            axs[2].plot(driver2_time, driver2_brake, driver2_color)

        if not plot_title:
            plot_title = driver1

        if driver2 and plot_title == driver1:
            plot_title = plot_title + " vs " + driver2

        axs[0].set_title(plot_title)
        axs[0].set_ylabel("Speed [Km/h]")
        axs[1].set_ylabel("%")
        axs[2].set_ylabel("%")
        axs[2].set_xlabel("Time")

    def show_plots(self):
        plt.show()
