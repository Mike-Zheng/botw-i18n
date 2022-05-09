#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import os
import yaml

json_name = 'zh-TW'
target_folder = 'Msg_TWzh.product.sarc'

support_category = ['ArmorHead',
                    'ArmorLower',
                    'ArmorUpper',
                    'Bullet',
                    'CapturedActor',
                    'CookEffect',
                    'DemoActorSubText',
                    'DemoNPC',
                    'Dragon',
                    'Dungeon',
                    'Enemy',
                    'GelEnemy',
                    'GiantEnemy',
                    'Guardian',
                    'Horse',
                    'HorseObject',
                    'HorseReins',
                    'HorseSaddle',
                    'Item',
                    'LastBoss',
                    'LocationMarker',
                    'MapDynamicPassive',
                    'NPC',
                    'Prey',
                    'Reference',
                    'Sandworm',
                    'SiteBoss',
                    'SpecialStatus',
                    'WeaponBow',
                    'WeaponLargeSword',
                    'WeaponShield',
                    'WeaponSmallSword',
                    'WeaponSpear']

# files = [val for sublist in [[os.path.join(i[0], j) for j in i[2] if j.endswith(
#     '.msyt')] for i in os.walk('./'+target_folder)] for val in sublist]


def myst_to_dic(file_path):
    with open(file_path, 'r', encoding='utf8') as yaml_in:
        # yaml_object will be a list or a dict
        yaml_object = yaml.safe_load(yaml_in)
        dic = yaml_object["entries"]
        for key in dic.keys():
            try:
                dic[key] = dic[key]["contents"][0]["text"]
            except:
                print(dic[key])

        print(dic)

    # dic ={}
    # file1 = open(file_path, 'r', encoding='utf8')
    # Lines = file1.readlines()

    # count = 0

    # for line in Lines:
    #     count += 1
    #     print("Line{}: {}".format(count, line.strip()))

    return dic


def dump_json(file_name, data):
    json_string = json.dumps(data, ensure_ascii=False)
    print(json_string)
    with open(file_name+'.json', 'w', encoding='utf8') as outfile:
        outfile.write(json_string)


outputfile = {}


for category in os.listdir(target_folder):
    outputfile[category] = {}
    for file in os.listdir(target_folder+"/"+category):
        if file.endswith(".msyt"):  # and category in FolderList:
            key = file.replace(".msyt", "")
            print(key)
            if(key in support_category):
                outputfile[category][key] = myst_to_dic(
                    target_folder+"/"+category+"/"+file)
            # myst_to_dic(
            #     target_folder+"/"+category+"/"+file)
            # myst_to_dic(file)


# testdic = myst_to_dic(files[0])


dump_json(json_name, outputfile)
