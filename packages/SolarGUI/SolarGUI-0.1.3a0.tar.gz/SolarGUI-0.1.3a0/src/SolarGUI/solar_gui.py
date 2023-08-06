"""
Created on May 22 00:40:38 2022
"""
import sys
import tkinter as tk

# added try/except because pip bundle and main file do not work with same imports

try:
    from . import show_planet as sp
    from . import tk_functions as tk_f
    from .celestial_objects import (Sun, Mercury, Venus, Earth, Moon, Mars, Jupiter,
                                    Saturn, Uranus, Neptune, Pluto)
except ImportError:
    import show_planet as sp
    import tk_functions as tk_f
    from celestial_objects import (Sun, Mercury, Venus, Earth, Moon, Mars, Jupiter,
                                   Saturn, Uranus, Neptune, Pluto)


# TODO: Get a good font
# TODO: adjust/create designs in tkinter windows
# TODO: make a planets vs Earth/Jupiter/Sun comparison dropdown menu as well
# TODO: Segregate moons, dwarf planets, planets and other type of celestial objects.
# TODO: Design adjustments of the GUI
# TODO: Separate button/menu for physical/orbital and other parameters.
# TODO: Some interesting plots (optional).
# TODO: Random facts button.
# TODO: Add citations
# TODO: Add a section of papers that study different properties of the celestial objects.

def main():

    ###################################################################################
    # Initialization
    ###################################################################################

    # set the width and height of the original window
    _w, _h = 800, 300
    # main is the master name in which all work is going to be done
    root_window = tk.Tk()
    # set the title of the GUI window
    root_window.title('SolarGUI')
    # set the size of the GUI window
    root_window.geometry(f'{_w}x{_h}')

    # do not let the window be resized
    root_window.minsize(_w, _h)

    [root_window.grid_columnconfigure(index=i, weight=1) for i in range(9)]

    ##################################################################################
    # Working
    ##################################################################################

    welcome_label = tk.Label(master=root_window,
                             text='Welcome to Solar Explorer. Please select a button.')
    welcome_label.grid(row=0, column=0, columnspan=9, pady=10, ipady=10)

    tk_f.planet_button(window=root_window, text='Sun',
                       function=lambda: sp.show_planet(window=root_window, text='Sun',
                                                       planet_class=Sun()), column=0)

    tk_f.planet_button(window=root_window, text='Mercury',
                       function=lambda: sp.show_planet(window=root_window,
                                                       text='Mercury',
                                                       planet_class=Mercury()), column=1)

    tk_f.planet_button(window=root_window, text='Venus',
                       function=lambda: sp.show_planet(window=root_window, text='Venus',
                                                       planet_class=Venus()), column=2)

    tk_f.planet_button(window=root_window, text='Earth',
                       function=lambda: sp.show_planet(window=root_window, text='Earth',
                                                       planet_class=Earth()), column=3)

    tk_f.planet_button(window=root_window, text='Mars',
                       function=lambda: sp.show_planet(window=root_window, text='Mars',
                                                       planet_class=Mars()), column=4)

    tk_f.planet_button(window=root_window, text='Jupiter',
                       function=lambda: sp.show_planet(window=root_window,
                                                       text='Jupiter',
                                                       planet_class=Jupiter()), column=5)

    tk_f.planet_button(window=root_window, text='Saturn',
                       function=lambda: sp.show_planet(window=root_window,
                                                       text='Saturn',
                                                       planet_class=Saturn()), column=6)

    tk_f.planet_button(window=root_window, text='Uranus',
                       function=lambda: sp.show_planet(window=root_window,
                                                       text='Uranus',
                                                       planet_class=Uranus()), column=7)

    tk_f.planet_button(window=root_window, text='Neptune',
                       function=lambda: sp.show_planet(window=root_window,
                                                       text='Neptune',
                                                       planet_class=Neptune()), column=8)

    tk_f.planet_button(window=root_window, text='Moon',
                       function=lambda: sp.show_planet(window=root_window,
                                                       text='Moon',
                                                       planet_class=Moon()),
                       column=0, row=2)

    tk_f.planet_button(window=root_window, text='Pluto',
                       function=lambda: sp.show_planet(window=root_window,
                                                       text='Pluto',
                                                       planet_class=Pluto()),
                       column=1, row=2)

    ##################################################################################
    # Show it
    ##################################################################################
    root_window.mainloop()


# taken from
# https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way-entry_points-and
# -scripts/

if __name__ == '__main__':
    try:
        sys.exit(main())
    except TypeError:
        pass
