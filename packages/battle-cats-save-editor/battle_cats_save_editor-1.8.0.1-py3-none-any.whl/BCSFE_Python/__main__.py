import sys, os
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)

import feature_handler
import serialise_save
import parse_save
import helper
import argparse
import adb_handler
import patcher

def main():
    helper.check_update()
    arg_handler(sys.argv[1:])

def normal_start_up():
    options = ["Select a save file from file", "Get the save data from the game automatically using adb", "Load save data from json", "Download save data with transfer and confirmation codes"]
    helper.create_list(options)
    option = input(f"Enter an option (1 to {len(options)}):")
    path = None
    if option == "1":
        path = helper.sel_save()
    elif option == "2":
        path = adb_handler.adb_pull_handler()
    elif option == "3":
        print("Select save data json file")
        js_path = helper.sel_file("Select save data json file", [("Json", "*.json")])
        path = helper.load_json_handler(js_path)
    elif option == "4":
        path = helper.download_save()
    else:
        print("Please enter a recognised option:")
        return normal_start_up()
    return path

def arg_handler(args):
    parser = argparse.ArgumentParser(description='A Battle Cats Save File Editor')

    parser.add_argument("--save_path", type=str, metavar="save-path", help="The path to your save data")
    parser.add_argument("--download", action="store_true", help="Flag to download save data from ponos servers")
    parser.add_argument("--pull", action="store_true", help="Flag to pull save data from the game")
    parser.add_argument("--export_json", type=str, metavar="output-path", help="Export the save data to a .json file with a path")
    parser.add_argument("--load_json", type=str, metavar="json-path", help="Load a json save data file as save data with a path")
    
    args_dict = vars(parser.parse_args(args))

    path = args_dict["save_path"]
    if not path:
        if args_dict["download"]:
            path = helper.download_save()
        elif args_dict["pull"]:
            path = adb_handler.adb_pull_handler()
        elif args_dict["load_json"]:
            path = helper.load_json_handler(args_dict["load_json"])
        else:
            path = normal_start_up()
    if not path:
        return

    data = helper.load_save_file(path)
    save_stats = data["save_stats"]
    save_data = data["save_data"]
    game_version_c = data["game_version"]

    if args_dict["export_json"]:
        serialise_save.export_json(save_stats, args_dict["export_json"])
        return
    if path.endswith(".json"):
        input("Your save data seems to be in json format. Please use to import json option if you want to load json data.\nPress enter to continue...:")
    while True:
        save_stats = parse_save.start_parse(save_data, game_version_c)
        save_data = patcher.patch_save_data(save_data, game_version_c)
        save_stats = feature_handler.menu(save_stats, path)
        save_data = serialise_save.start_serialize(save_stats)
        save_data = patcher.patch_save_data(save_data, game_version_c)
    

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()