#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import os
import yaml
import time

folders_array = [['Msg_CNzh.product.sarc', 'zh-CN'],
                 ['Msg_EUde.product.sarc', 'de-EU'],
                 ['Msg_EUen.product.sarc', 'en-EU'],
                 ['Msg_EUes.product.sarc', 'es-EU'],
                 ['Msg_EUfr.product.sarc', 'fr-EU'],
                 ['Msg_EUit.product.sarc', 'it-EU'],
                 ['Msg_EUnl.product.sarc', 'nl-EU'],
                 ['Msg_EUru.product.sarc', 'ru-EU'],
                 ['Msg_JPja.product.sarc', 'ja-JP'],
                 ['Msg_KRko.product.sarc', 'ko-KR'],
                 ['Msg_TWzh.product.sarc', 'zh-TW'],
                 ['Msg_USen.product.sarc', 'en-US'],
                 ['Msg_USes.product.sarc', 'es-US'],
                 ['Msg_USfr.product.sarc', 'fr-US']]

# files = [val for sublist in [[os.path.join(i[0], j) for j in i[2] if j.endswith(
#     '.msyt')] for i in os.walk('./'+target_folder)] for val in sublist]


def myst_to_dic(file_path):
    with open(file_path, 'r', encoding='utf8') as yaml_in:
        # yaml_object will be a list or a dict
        yaml_object = yaml.safe_load(yaml_in)
        dic = yaml_object["entries"]
        for key in dic.keys():
            try:
                if ('text' in dic[key]["contents"][0]):
                    dic[key] = dic[key]["contents"][0]["text"]
                elif ('text' in dic[key]["contents"][1]):
                    dic[key] = dic[key]["contents"][1]["text"]
                else:
                    dic[key] = dic[key]["contents"][2]["text"]
            except:
                dic[key] = ''

        # print(dic)

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
    # print(json_string)
    with open(file_name+'.json', 'w', encoding='utf8') as outfile:
        outfile.write(json_string)


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


for item in folders_array:

    json_name = item[1]
    target_folder = item[0]

    outputfile = {}
    for category in os.listdir(target_folder):
        outputfile[category] = {}
        for file in os.listdir(target_folder+"/"+category):
            if file.endswith(".msyt"):  # and category in FolderList:
                key = file.replace(".msyt", "")
                # print(key)
                if(key in support_category):
                    outputfile[category][key] = myst_to_dic(
                        target_folder+"/"+category+"/"+file)

    dump_json(json_name, outputfile)
