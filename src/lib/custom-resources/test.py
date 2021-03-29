import os
import json

rootdir = '/Users/rverma/dev/aws-secure-environment-accelerator/src/lib/custom-resources'
rush = []
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file == 'package.json':
            with open(os.path.join(subdir, file), "r+") as jsonFile:
                dependencies, peerDependencies, devDependencies = {}, {}, {}
                data = json.load(jsonFile)
                if 'peerDependencies' in data and len(data["peerDependencies"]) > 0:
                    peerDependencies = data["peerDependencies"]
                else:
                    continue
                if 'dependencies' in data and len(data["dependencies"]) > 0:
                    dependencies = data["dependencies"]
                    if 'ts-node' in dependencies:
                        dependencies["ts-node"] = "8.8.1"
                    if '@types/jest' in dependencies:
                        dependencies["@types/jest"] = "25.2.1"
                else:
                    continue
                if 'devDependencies' in data and len(data["devDependencies"]) > 0:
                    devDependencies = data["devDependencies"]
                    if 'ts-node' in devDependencies:
                        devDependencies["ts-node"] = "8.8.1"
                    if '@types/jest' in devDependencies:
                        devDependencies["@types/jest"] = "25.2.3"
                cleaned = dict(set(peerDependencies.items()).difference(set(dependencies.items())))
                moved = devDependencies | peerDependencies
                print("peer: ", cleaned)
                print("dev: ", moved)
                data["peerDependencies"] = cleaned
                # data["devDependencies"] = moved
                jsonFile.seek(0)
                json.dump(data, jsonFile, indent=2)
                jsonFile.truncate()

# for subdir, dirs, files in os.walk(rootdir):
#     for file in files:
#         if file == 'package.json':
#             with open(os.path.join(subdir, file), "r") as jsonFile:
#                 data = json.load(jsonFile)
#
#                 temp = {}
#                 temp["projectFolder"] = "src/lib/custom-resources/"+subdir
#                 temp["packageName"] = data["name"]
#                 temp["shouldPublish"] = "true"
#                 temp["versionPolicyName"]= "locked"
#                 rush.append(temp)
#
# print(rush)