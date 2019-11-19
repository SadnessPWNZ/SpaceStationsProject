import sqlite3
from SpaceStationProject.src.Classes import Station

DATABASE_PATH = r'C:\Users\princ\Desktop\DEV\SchoolProject\SpaceStationProject\src\sample3.sqlite'

con = sqlite3.connect(DATABASE_PATH)
cursor = con.cursor()


def get_countries() -> list:
    # Get list of all countries
    countries_list = cursor.execute("""SELECT "Country of Operator/Owner" FROM List""").fetchall()
    new_list = list()
    for i in countries_list:
        new_i = i[0]
        new_list.append(new_i)

    new_list = list(set(new_list))
    return new_list


def get_stations(country: str) -> list:
    '''

    :param country: string with country
    :return: stations_list: list with objects of Station class
    List structure:
        1)NORAD ID
        2)Name of Satellite and(or) Alternative names
        3)Country of operator
        4)Operator(owner)
        5)Users
        6)Purpose

    '''
    stations_list = cursor.execute(f"""SELECT * FROM List
    WHERE "Country of Operator/Owner" = "{country}" """).fetchall()
    returns_list = []
    for i in stations_list:
        station = Station(i[0], i[1], i[2], i[3], i[4], i[5])
        returns_list.append(station)

    return returns_list


def get_stations_and_norad() -> dict:
    '''

    :return: Key - station name
             Value - Norad id
    '''
    listt = cursor.execute("""SELECT "NORAD Number", "Name of Satellite" FROM List""").fetchall()
    # print(listt)
    my_dict = dict()
    for i in listt:
        my_dict[i[1]] = i[0]

    return my_dict


def get_station(station_name: str) -> Station:
    information = cursor.execute(f"""SELECT * FROM List
    WHERE "Name of Satellite" = "{station_name}" """).fetchone()
    return Station(information[0], information[1], information[2], information[3], information[4], information[5])
