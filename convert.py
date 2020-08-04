import sys
import argparse
import os
import json

parser = argparse.ArgumentParser(description='Process a beatsaber song.')
parser.add_argument('basedir', metavar='FileDir', type=str,
                    help='a folder to convert to beatswiper format')

args = parser.parse_args()
basedir = args.basedir

difftrans = {
    "Easy":         0,
    "Normal":       1,
    "Hard":         2,
    "Expert":       3,
    "ExpertPlus":   4,
}
directiontrans = [
    2,
    6,
    4,
    0,
    3,
    1,
    5,
    7,
    8
]



def convToBeatSwiperJson(info, song, diff):

    print(f"\n[+] Making song data: {diff}")

    metaout = {"UniqeNumber": 37,
               "Song_Title": "", # This
               "Song_Description": "Amanotes;test", 
               "Song_AuthorName": "", # This
               "Song_FolderName": "", # This
               "Pack_FolderIndex": 0,
               "PackFolderName": "Modified",
               "BPM": 0,                         # This
               "status_Availability": 1,
               "available_Difficulties": [ # This
                   1,
                   3,
                   4
               ],
               "coinUnlockValue": [
                   800,
                   900,
                   1200
               ],
               "levelUnlockValue": [
                   0,
                   0,
                   0
               ],
               "isUnlocked": True,                  # This
               "priority": 549,
               "version": 1,
               "downloadedVersion": 0,
               "leaderboardID": "CgkIpPv3hdYLEAIQJQ",
               "totalTime_Seconds": 0}                # This
    
    # =================================
    # straight read json & transfer

    metaout["Song_Title"] = info["_songName"]
    metaout["Song_AuthorName"] = info["_songAuthorName"]
    metaout["BPM"] = float(info["_beatsPerMinute"])

    # =================================
    # calc and trasfer

    foldername = info["_songName"].replace(" ", "_").replace("'", "".replace('"', ""))
    time = round(song["_notes"][-1]["_time"] + 1)

    songdiff = [difftrans[x] for x in [info["_difficultyBeatmapSets"][0]["_difficultyBeatmaps"][y]["_difficulty"] for y in range(len(info["_difficultyBeatmapSets"][0]["_difficultyBeatmaps"]))]]
    # whoo wee, what a chonker


    metaout["Song_FolderName"] = foldername
    metaout["totalTime_Seconds"] = time
    metaout["available_Difficulties"] = songdiff

    # =================================
    # Song stuff!
    # wierd because beatswiper uses a json list but without the brackets

    songout = []

    for i, x in enumerate(song["_notes"]):
        songout.append({
                "Amanotes_NoteNumber": i,
                "name": "",
                "row_number": x["_lineLayer"] + 1,
                "line_number": x["_lineIndex"] + 1,
                "direction_number": directiontrans[x["_cutDirection"]],
                "time": x["_time"],
                "number": 0,
                "colorKind": x["_type"],
                "pool_Index": 0
        })
    try:
        os.mkdir(f"{basedir}/../{foldername}")
        print(f"[+] Making directory: {foldername}")
    except:
        pass

    print(f"[+] Writing song data: {foldername}/{diff}")
    songfile = open(f"{basedir}/../{foldername}/{diff}.txt", "w").write("")
    songfile = open(f"{basedir}/../{foldername}/{diff}.txt", "a")
    for i, x in enumerate(songout):
        songfile.write(json.dumps(x) + "\n")
    songfile.close()

    print(f"[+] Writing song info: {foldername}/info.txt")
    infofile = open(f"{basedir}/../{foldername}/info.txt", "w")
    json.dump(metaout, infofile)


def main():
    
    if not os.path.isdir(basedir):
        print("not a dir")
        exit()

    files = []
    for (dirpath, dirnames, filenames) in os.walk(basedir):
        files.extend(filenames)
        break

    infostr = "Info.dat"

    if not "Info.dat" in files:
        if not "info.dat" in files:
            print("Directory structure is wrong")
            exit()
        infostr = "info.dat"
        
    

    with open(f"{basedir}/{infostr}") as info:
        infojson = json.load(info)
    

    for x in infojson["_difficultyBeatmapSets"][0]["_difficultyBeatmaps"]:

        with open(f'{basedir}/{x["_beatmapFilename"]}') as song:
            songjson = json.load(song)

        convToBeatSwiperJson(infojson, songjson, x["_difficulty"])
        

if __name__ == "__main__":
    main()