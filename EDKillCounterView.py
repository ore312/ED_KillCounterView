import json
import sys
import os
import pyperclip

def readJson(pPath):
    aStr = ""
    with open(pPath, mode="r", encoding="utf-8") as aFNo:
        aStr = aFNo.read()
    aStr = '{"data":' + aStr + '}'
    return json.loads(aStr)

def getFactionToFac(pFac):
    aOut = ""
    aCon = pFac.split(" ")
    for aC in aCon:
        aOut += aC[0:1]
    return aOut

def cnvJsonToTxt(pJson):
    aKill = pJson.get("KillCount")
    aBunty = pJson.get("Bounty")
    aBond = pJson.get("Bond")

    aOfKill = pJson.get("OfKillCount")
    aOfBunty = pJson.get("OfBounty")
    aOfBond = pJson.get("OfBond")

    if aKill == 0 and aBunty == 0 and aBond == 0 and \
            aOfKill == 0 and aOfBunty == 0 and aOfBond == 0:
        return ""

    aOut = ""
    aOut += "System  : " + str(pJson.get("SystemName")) + "\n"
    aOut += "Faction : " + getFactionToFac(pJson.get("FactionName")) + "\n"
    if not(aKill == 0 and aBunty == 0 and aBond == 0):
        aOut += ">> Ship <<" + "\n"
        aOut += "    Kill : " + str("{:,}".format(aKill)) + "\n"
        # aOut += "    Kill   : " + str("{:,}".format(aKill)) + "\n"
        # aOut += "    Bounty : " + str("{:,}".format(aBunty)) + "\n"
        # aOut += "    Bond   : " + str("{:,}".format(aBond)) + "\n"
    if not(aOfKill == 0 and aOfBunty == 0 and aOfBond == 0):
        aOut += ">> On Foot <<" + "\n"
        aOut += "    Kill : " + str("{:,}".format(aOfKill)) + "\n"
        # aOut += "    Kill   : " + str("{:,}".format(aOfKill)) + "\n"
        # aOut += "    Bounty : " + str("{:,}".format(aOfBunty)) + "\n"
        # aOut += "    Bond   : " + str("{:,}".format(aOfBond)) + "\n"
    return aOut + "\n"

def main():
    if not(len(sys.argv) > 1):
        print("引き数がありません")
        return
    if os.path.exists(sys.argv[1]) != True:
        print("指定されたパスが存在しません")
        return

    aJson = readJson(sys.argv[1])
    if aJson == None:
        print("jsonオブジェクトへの変換に失敗しました")

    aStr = ""
    for aJ in aJson.get("data"):
        aStr += cnvJsonToTxt(aJ)
    print(aStr)
    pyperclip.copy("```\n" + aStr + "```")

if __name__ == "__main__":
    main()
