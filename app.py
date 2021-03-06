import os

from data_processing import get_list_id_videos, get_formatted_data
from graphs import show_statistic_graph
from youtubeAPI import getChannelId, getVideosStatistic


def get_youtube_channel_name():
    channel_name = input('Enter the name of the Youtube channel from which you want to get info.\n'
                         'Or PRESS ENTER to choose the default - "FootballTVUA"\n> ')
    if len(channel_name) == 0:
        channel_name = 'FootballTVUA'
    return channel_name


def app(channel_name, channel_id):
    list_of_videos_id = get_list_id_videos(channel_id)
    list_of_videos_statistic = getVideosStatistic(list_of_videos_id)
    formatted_data_for_graphs = get_formatted_data(list_of_videos_statistic)

    def menu_graphs():
        menu_choice = int(input('1 - Views\n2 - Likes\n3 - Comments\n4 - Exit\n> '))
        if menu_choice == 1:
            menu_choice = 'viewCount'
            show_statistic_graph(formatted_data_for_graphs, menu_choice, channel_name, channel_id)
            menu_graphs()
        elif menu_choice == 2:
            menu_choice = 'likeCount'
            show_statistic_graph(formatted_data_for_graphs, menu_choice, channel_name, channel_id)
            menu_graphs()
        elif menu_choice == 3:
            menu_choice = 'commentCount'
            show_statistic_graph(formatted_data_for_graphs, menu_choice, channel_name, channel_id)
            menu_graphs()
        elif menu_choice == 4 or menu_choice == 'exit' or menu_choice == 'Exit':
            os.system('exit')
        else:
            print('Try to enter the correct value\n\n\n')
            menu_graphs()

    menu_graphs()


def start():
    channel_name = get_youtube_channel_name()
    channel_id = getChannelId(channel_name)
    if not channel_id:
        print('Error. Can`t find this youtube channel.\n')
        start()
    else:
        app(channel_name, channel_id)


if __name__ == '__main__':
    start()
